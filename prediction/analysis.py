import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("../data/alzheimers_disease_data.csv")

    sns.swarmplot(data=df, y='FunctionalAssessment', x='Diagnosis')
    plt.title(f'Distribution of Functional Assessment Scores by Diagnosis Categories')
    plt.show()

    sns.swarmplot(data=df, y='ADL', x='Diagnosis')
    plt.title(f'Activities of Daily Living score by Diagnosis Categories')
    plt.show()

    sns.swarmplot(data=df, y='MMSE', x='Diagnosis')
    plt.title(f'Mini-Mental State Examination score by Diagnosis Categories')
    plt.show()

    sns.countplot(data=df, x='Diagnosis', hue='BehavioralProblems')
    plt.title(f'Distribution of Behavioral Problems by Diagnosis Categories')
    plt.show()

    sns.countplot(data=df, x='Diagnosis', hue='MemoryComplaints')
    plt.title(f'Distribution of Memory Complaints by Diagnosis Categories')
    plt.show()