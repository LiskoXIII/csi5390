import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import classification_report
from catboost import CatBoostClassifier


def preprocessing():
    df = pd.read_csv("../data/alzheimers_disease_data.csv")

    df.drop(['PatientID', 'DoctorInCharge'], axis=1, inplace=True)

    for column in df.columns:
        unique_values = df[column].unique()
        print(f"Unique values in column '{column}':")
        print(unique_values)
        print()

    columns = ['Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality', 'SystolicBP',
               'DiastolicBP', 'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides',
               'MMSE', 'FunctionalAssessment', 'ADL']

    # normalize the columns
    min_max_scaler = MinMaxScaler()
    df[columns] = min_max_scaler.fit_transform(df[columns])

    # standardize the columns
    standard_scaler = StandardScaler()
    df[columns] = standard_scaler.fit_transform(df[columns])

    return df

def build_model(df):
    # split data into features and target
    X = df.drop(columns=['Diagnosis'])
    y = df['Diagnosis']

    # split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    cat = CatBoostClassifier(iterations=100, learning_rate=0.01)
    cat.fit(X_train, y_train)
    y_pred = cat.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)

if __name__ == '__main__':
    data = preprocessing()
    data.info()
    build_model(data)