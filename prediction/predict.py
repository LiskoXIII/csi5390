import pandas as pd
import joblib
from catboost import CatBoostClassifier


#using the same preprocess objects that were used to train the model
def load_preprocessing_objects():
    min_max_scaler = joblib.load("min_max_scaler.joblib")
    standard_scaler = joblib.load("standard_scaler.joblib")
    return min_max_scaler, standard_scaler


#preprocess the new patient data in the same way the dataset was preprocessed during training
def preprocess_new_data(new_data, min_max_scaler, standard_scaler):
    columns = ['Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality', 'SystolicBP',
               'DiastolicBP', 'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides',
               'MMSE', 'FunctionalAssessment', 'ADL']

    # making sure that all data is present
    if not all(col in new_data.columns for col in columns):
        raise ValueError("Missing required columns in the input data.")

    # perform preprocessing on the data before prediction
    new_data[columns] = min_max_scaler.transform(new_data[columns])
    new_data[columns] = standard_scaler.transform(new_data[columns])

    return new_data

#load the trained model
def load_model():
    model = CatBoostClassifier()
    model.load_model("catboost_model.cbm")
    return model

def make_prediction(dataframe):
    min_max_scaler, standard_scaler = load_preprocessing_objects()

    model = load_model()

    patient_data = dataframe

    # drop columns not needed in prediction
    patient_data.drop(['PatientID', 'DoctorInCharge'], axis=1, inplace=True, errors='ignore')

    processed_data = preprocess_new_data(patient_data, min_max_scaler, standard_scaler)

    predictions = model.predict(processed_data)

    diagnosis = pd.DataFrame()
    diagnosis['Diagnosis_Prediction'] = predictions
    diagnosis.to_csv("predictions.csv", index=False)
    print("Predictions saved to 'predictions.csv'")