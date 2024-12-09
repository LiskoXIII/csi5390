"""
Citation of the dataset:

@misc{rabie_el_kharoua_2024,
title={Alzheimer's Disease Dataset},
url={https://www.kaggle.com/dsv/8668279},
DOI={10.34740/KAGGLE/DSV/8668279},
publisher={Kaggle},
author={Rabie El Kharoua},
year={2024}
}
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import classification_report
from catboost import CatBoostClassifier
import joblib

def preprocessing() -> pd.DataFrame:
    """
    Cleans and scales the Alzheimer's disease dataset, preparing it for model training.

    This function performs the following steps:
    1. Loads the dataset from a CSV file.
    2. Removes unnecessary columns (`PatientID`, `DoctorInCharge`).
    3. Prints unique values for each remaining column for exploratory purposes.
    4. Scales specified numerical features using Min-Max and Standard scaling.
    5. Saves the fitted scalers to disk for future use in predictions.

    Returns:
        pd.DataFrame: A preprocessed DataFrame ready for training machine learning models.
    """
    # Load the dataset
    df = pd.read_csv("../data/alzheimers_disease_data.csv")

    # Drop unnecessary columns
    df.drop(['PatientID', 'DoctorInCharge'], axis=1, inplace=True)

    # Print unique values for each column
    for column in df.columns:
        unique_values = df[column].unique()
        print(f"Unique values in column '{column}':")
        print(unique_values)
        print()

    # Specify columns to scale
    columns_to_scale = [
        'Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality',
        'SleepQuality', 'SystolicBP', 'DiastolicBP', 'CholesterolTotal',
        'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides',
        'MMSE', 'FunctionalAssessment', 'ADL'
    ]

    # Initialize scalers
    min_max_scaler = MinMaxScaler()
    standard_scaler = StandardScaler()

    # Apply Min-Max scaling
    df[columns_to_scale] = min_max_scaler.fit_transform(df[columns_to_scale])

    # Apply Standard scaling
    df[columns_to_scale] = standard_scaler.fit_transform(df[columns_to_scale])

    # Save the scalers for future use
    joblib.dump(min_max_scaler, "min_max_scaler.joblib")
    joblib.dump(standard_scaler, "standard_scaler.joblib")
    print("Scalers saved as 'min_max_scaler.joblib' and 'standard_scaler.joblib'.")

    return df

def build_model(df: pd.DataFrame) -> None:
    """
    Trains a CatBoost classifier on the provided dataset and evaluates its performance.

    This function performs the following steps:
    1. Separates features and target variable from the DataFrame.
    2. Splits the data into training and testing sets.
    3. Initializes and trains a CatBoostClassifier.
    4. Makes predictions on the test set.
    5. Prints a classification report of the model's performance.
    6. Saves the trained model to disk for future use.

    Args:
        df (pd.DataFrame): The preprocessed DataFrame containing features and the target variable 'Diagnosis'.

    Returns:
        None
    """
    # Separate features (X) and target variable (y)
    X = df.drop(columns=['Diagnosis'])
    y = df['Diagnosis']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        shuffle=True
    )
    print("Data split into training and testing sets.")

    # Initialize the CatBoostClassifier with specified hyperparameters
    cat = CatBoostClassifier(
        iterations=100,
        learning_rate=0.01,
        verbose=0
    )
    print("CatBoostClassifier initialized.")

    # Train the model on the training data
    cat.fit(X_train, y_train)
    print("Model training completed.")

    # Make predictions on the test set
    y_pred = cat.predict(X_test)
    print("Predictions on test set completed.")

    # Generate and print the classification report
    report = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(report)

    # Save the trained model to disk for future use
    cat.save_model("catboost_model.cbm")
    print("Model saved as 'catboost_model.cbm'.")

    # Optionally, save the test data for later evaluation or analysis
    joblib.dump((X_test, y_test, y_pred), "model_evaluation_data.joblib")
    print("Test data and predictions saved as 'model_evaluation_data.joblib'.")

if __name__ == '__main__':
    data = preprocessing()
    data.info()
    build_model(data)