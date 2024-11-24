import os
import pandas as pd
import joblib
from catboost import CatBoostClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from typing import Tuple

def load_preprocessing_objects() -> Tuple[MinMaxScaler, StandardScaler]:
    """
    Loads the Min-Max and Standard scalers used during the training phase.

    This function retrieves the scaler objects from the 'prediction' directory,
    ensuring that the same preprocessing transformations can be applied to new data
    during prediction.

    Returns:
        Tuple[MinMaxScaler, StandardScaler]: A tuple containing the loaded MinMaxScaler
        and StandardScaler instances.
    """
    # Define the directory where scaler objects are stored
    scaler_dir = "prediction"

    # Paths to the scaler files
    min_max_path = os.path.join(scaler_dir, "min_max_scaler.joblib")
    standard_path = os.path.join(scaler_dir, "standard_scaler.joblib")

    # Load the Min-Max scaler
    try:
        min_max_scaler = joblib.load(min_max_path)
        print(f"Min-Max scaler loaded from '{min_max_path}'.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Min-Max scaler file not found at '{min_max_path}'.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading Min-Max scaler: {e}")

    # Load the Standard scaler
    try:
        standard_scaler = joblib.load(standard_path)
        print(f"Standard scaler loaded from '{standard_path}'.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Standard scaler file not found at '{standard_path}'.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading Standard scaler: {e}")

    return min_max_scaler, standard_scaler


def preprocess_new_data(
    new_data: pd.DataFrame,
    min_max_scaler: MinMaxScaler,
    standard_scaler: StandardScaler
) -> pd.DataFrame:
    """
    Preprocesses new patient data using predefined Min-Max and Standard scalers.

    Args:
        new_data (pd.DataFrame): DataFrame containing new patient data.
        min_max_scaler (MinMaxScaler): Fitted Min-Max scaler from training.
        standard_scaler (StandardScaler): Fitted Standard scaler from training.

    Returns:
        pd.DataFrame: Scaled DataFrame ready for prediction.

    Raises:
        ValueError: If required columns are missing.
        AttributeError: If scalers lack the `transform` method.
    """
    required_columns = [
        'Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality',
        'SleepQuality', 'SystolicBP', 'DiastolicBP', 'CholesterolTotal',
        'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides',
        'MMSE', 'FunctionalAssessment', 'ADL'
    ]

    # Check for missing columns
    missing = [col for col in required_columns if col not in new_data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Ensure scalers have the transform method
    if not all(hasattr(scaler, 'transform') for scaler in [min_max_scaler, standard_scaler]):
        raise AttributeError("One or more scalers do not have a 'transform' method.")

    # Apply scaling
    scaled_data = min_max_scaler.transform(new_data[required_columns])
    scaled_data = standard_scaler.transform(scaled_data)
    new_data[required_columns] = scaled_data

    return new_data


def load_model() -> CatBoostClassifier:
    """
    Loads the pre-trained CatBoost classifier from the specified file.

    This function initializes a CatBoostClassifier instance and loads the trained model
    parameters from the 'catboost_model.cbm' file located in the 'prediction' directory.
    The loaded model is then returned for use in making predictions.

    Returns:
        CatBoostClassifier: The loaded CatBoost classifier ready for making predictions.

    Raises:
        FileNotFoundError: If the model file 'catboost_model.cbm' does not exist in the 'prediction' directory.
        Exception: If there is an error while loading the model.
    """
    try:
        # Initialize the CatBoostClassifier
        model = CatBoostClassifier()

        # Define the path to the trained model
        model_path = os.path.join("prediction", "catboost_model.cbm")

        # Load the trained model from the specified path
        model.load_model(model_path)
        print(f"Model loaded successfully from '{model_path}'.")

        return model

    except FileNotFoundError:
        raise FileNotFoundError(f"The model file was not found at '{model_path}'. Please ensure the file exists.")

    except Exception as e:
        raise Exception(f"An error occurred while loading the model: {e}")

def make_prediction(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Generates diagnosis predictions for new patient data using a pre-trained CatBoost model.

    This function performs the following steps:
    1. Loads the preprocessing scalers (Min-Max and Standard scalers) used during training.
    2. Loads the pre-trained CatBoost classifier.
    3. Preprocesses the input patient data to ensure it is in the correct format for prediction.
    4. Applies the preprocessing transformations to the patient data.
    5. Uses the trained model to make predictions on the processed data.
    6. Returns a DataFrame containing the diagnosis predictions.

    Args:
        dataframe (pd.DataFrame): A DataFrame containing new patient data. Expected to include features
                                  such as 'Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity',
                                  'DietQuality', 'SleepQuality', 'SystolicBP', 'DiastolicBP',
                                  'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL',
                                  'CholesterolTriglycerides', 'MMSE', 'FunctionalAssessment',
                                  'ADL', along with 'PatientID' and 'DoctorInCharge' columns which
                                  will be dropped if present.

    Returns:
        pd.DataFrame: A DataFrame with a single column 'Diagnosis_Prediction' containing the predicted
                      diagnosis for each patient in the input DataFrame.

    Raises:
        ValueError: If the input DataFrame is missing required columns necessary for prediction.
        FileNotFoundError: If the scaler or model files are not found in the expected directory.
        Exception: For any other errors that occur during the prediction process.
    """
    # Load preprocessing scalers
    min_max_scaler, standard_scaler = load_preprocessing_objects()

    # Load the pre-trained CatBoost model
    model = load_model()

    # Create a copy of the input data to avoid modifying the original DataFrame
    patient_data = dataframe.copy()

    # Drop columns not needed for prediction
    patient_data.drop(['PatientID', 'DoctorInCharge'], axis=1, inplace=True, errors='ignore')

    # Preprocess the patient data using the loaded scalers
    processed_data = preprocess_new_data(patient_data, min_max_scaler, standard_scaler)

    # Make predictions using the trained model
    predictions = model.predict(processed_data)

    # Create a DataFrame to store the predictions
    diagnosis = pd.DataFrame()
    diagnosis['Diagnosis_Prediction'] = predictions

    # Return the predictions DataFrame
    return diagnosis