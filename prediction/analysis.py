import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas
import seaborn as sns
import pandas as pd
from PySide6.QtWidgets import QProgressDialog, QApplication


def analyze(patient_df: pd.DataFrame, prediction_result: int, progress: QProgressDialog) -> None:
    """
    Analyzes a patient's data by generating and saving visualizations of key features
    in comparison to existing Alzheimer's disease dataset categories.

    This function performs the following steps:
    1. Loads the Alzheimer's disease dataset from a CSV file.
    2. Extracts the first patient's data from the provided DataFrame.
    3. Adds the diagnosis prediction to the patient's data.
    4. For each specified feature ('FunctionalAssessment', 'ADL', 'MMSE'):
        a. Creates a swarm plot to visualize the distribution of the feature across
           different diagnosis categories.
        b. Highlights the current patient's feature value on the plot.
        c. Annotates the plot with the label 'Current Patient'.
        d. Saves the plot as an image file.
        e. Updates the progress dialog to reflect the completion of each plot.

    Args:
        patient_df (pd.DataFrame): A DataFrame containing the new patient's data. It is expected
                                   to include columns such as 'PatientID', 'DoctorInCharge',
                                   'FunctionalAssessment', 'ADL', and 'MMSE'.
        prediction_result (int): The diagnosis prediction result for the patient, typically
                                 encoded as an integer corresponding to specific diagnosis categories.
        progress (QProgressDialog): A QProgressDialog instance to provide visual feedback on the
                                    progress of the analysis, updating as each plot is generated.

    Returns:
        None

    Saves:
        - Three plot images named 'plot_FunctionalAssessment.png', 'plot_ADL.png', and
          'plot_MMSE.png' in the current working directory.

    Raises:
        FileNotFoundError: If the 'alzheimers_disease_data.csv' file is not found in the specified
                           directory ('data').
        KeyError: If expected columns are missing from the `patient_df` DataFrame.
        Exception: For any other errors that may occur during the analysis or plotting process.
    """
    try:
        # Load the Alzheimer's disease dataset
        df = pd.read_csv(os.path.join("data", "alzheimers_disease_data.csv"))
        print("Alzheimer's disease dataset loaded successfully.")

        # Extract the first patient's data
        patient_features = patient_df
        patient_data = patient_features.iloc[0].copy()
        patient_data['Diagnosis'] = prediction_result
        print("Patient data extracted and diagnosis prediction added.")

        # Define the list of important features to analyze
        feature_list = ['FunctionalAssessment', 'ADL', 'MMSE']

        for feature in feature_list:
            plt.figure(figsize=(10, 6))

            # Create a swarm plot for the feature across diagnosis categories
            sns.swarmplot(data=df, y=feature, x='Diagnosis', color='skyblue', alpha=0.7)

            # Highlight the current patient's feature value
            sns.scatterplot(
                x=[prediction_result],
                y=[patient_data[feature]],
                color='red',
                edgecolor='black',  # Add edge color
                s=200,               # Increase size
                marker='D',          # Diamond marker
                label='Current Patient',
                zorder=10            # Ensure it's on top
            )

            # Annotate the plot with the label 'Current Patient'
            plt.annotate(
                'Current Patient',
                xy=(prediction_result, patient_data[feature]),
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=12,
                color='red',
                weight='bold'
            )

            # Set plot titles and labels
            plt.title(f'{feature} by Diagnosis Categories with Current Patient', fontsize=16)
            plt.xlabel('Diagnosis', fontsize=14)
            plt.ylabel(feature, fontsize=14)
            plt.legend()
            plt.tight_layout()

            # Save the plot as an image file
            plt.savefig(f'prediction/plot_{feature}.png')
            plt.close()
            print(f"Plot for '{feature}' saved as 'prediction/plot_{feature}.png'.")

            # Update the progress dialog
            progress.setValue(progress.value() + 1)
            QApplication.processEvents()

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
        raise

    except KeyError as key_error:
        print(f"Error: Missing expected column - {key_error}")
        raise

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise