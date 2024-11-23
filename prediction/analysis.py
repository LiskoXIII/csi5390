import matplotlib.pyplot as plt
import pandas
import seaborn as sns
import pandas as pd


def analyze(patient_df, prediction_df):
    df = pd.read_csv("../data/alzheimers_disease_data.csv")
    patient_features = patient_df
    predictions = prediction_df

    patient_diagnosis = predictions.loc[0, "Diagnosis_Prediction"]
    patient_data = patient_features.iloc[0].copy()
    patient_data['Diagnosis'] = patient_diagnosis

    # most important features to use
    feature_list = ['FunctionalAssessment', 'ADL', 'MMSE']

    for feature in feature_list:
        plt.figure(figsize=(10, 6))

        sns.swarmplot(data=df, y=feature, x='Diagnosis', color='skyblue', alpha=0.7)

        sns.scatterplot(
            x=[patient_diagnosis],
            y=[patient_data[feature]],
            color='red',
            edgecolor='black',  # Add edge color
            s=200,  # Increase size
            marker='D',  # Diamond marker
            label='Current Patient',
            zorder=10  # Ensure it's on top
        )

        plt.annotate(
            'Current Patient',
            xy=(patient_diagnosis, patient_data[feature]),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=12,
            color='red',
            weight='bold'
        )

        plt.title(f'{feature} by Diagnosis Categories with Current Patient', fontsize=16)
        plt.xlabel('Diagnosis', fontsize=14)
        plt.ylabel(feature, fontsize=14)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f'plot_{feature}.png')
        plt.close()