import pytest
from dataset import Dataset, Gender, Ethnicity, EducationLevel, Decision
import pandas as pd


def test_age():
    dataset = Dataset()
    dataset.age = 65.0
    assert dataset.age == 65.0

    with pytest.raises(ValueError):
        dataset.age = 95.0


def test_gender():
    dataset = Dataset()
    dataset.gender = Gender.MALE.value
    assert dataset.gender == Gender.MALE.value

    with pytest.raises(ValueError):
        dataset.gender = 3


def test_ethnicity():
    dataset = Dataset()
    dataset.ethnicity = Ethnicity.CAUCASIAN.value
    assert dataset.ethnicity == Ethnicity.CAUCASIAN.value

    with pytest.raises(ValueError):
        dataset.ethnicity = 5


def test_education_level():
    dataset = Dataset()
    dataset.education_level = EducationLevel.BACHELORS.value
    assert dataset.education_level == EducationLevel.BACHELORS.value

    with pytest.raises(ValueError):
        dataset.education_level = 4


def test_bmi():
    dataset = Dataset()
    dataset.bmi = 25.0
    assert dataset.bmi == 25.0

    with pytest.raises(ValueError):
        dataset.bmi = 50.0


def test_smoking():
    dataset = Dataset()
    dataset.smoking = Decision.YES.value
    assert dataset.smoking == Decision.YES.value

    with pytest.raises(ValueError):
        dataset.smoking = 2

def test_alcohol_consumption():
    dataset = Dataset()
    dataset.alcohol_consumption = 10.0
    assert dataset.alcohol_consumption == 10.0

    with pytest.raises(ValueError):
        dataset.alcohol_consumption = 25.0

def test_physical_activity():
    dataset = Dataset()
    dataset.physical_activity = 5.0
    assert dataset.physical_activity == 5.0

    with pytest.raises(ValueError):
        dataset.physical_activity = 15.0

def test_diet_quality():
    dataset = Dataset()
    dataset.diet_quality = 8.0
    assert dataset.diet_quality == 8.0

    with pytest.raises(ValueError):
        dataset.diet_quality = 15.0

def test_sleep_quality():
    dataset = Dataset()
    dataset.sleep_quality = 7.0
    assert dataset.sleep_quality == 7.0

    with pytest.raises(ValueError):
        dataset.sleep_quality = 3.0

def test_family_history_alzheimers():
    dataset = Dataset()
    dataset.family_history_alzheimers = Decision.NO.value
    assert dataset.family_history_alzheimers == Decision.NO.value

    with pytest.raises(ValueError):
        dataset.family_history_alzheimers = 2

def test_cardiovascular_disease():
    dataset = Dataset()
    dataset.cardiovascular_disease = Decision.YES.value
    assert dataset.cardiovascular_disease == Decision.YES.value

    with pytest.raises(ValueError):
        dataset.cardiovascular_disease = 2

def test_diabetes():
    dataset = Dataset()
    dataset.diabetes = Decision.NO.value
    assert dataset.diabetes == Decision.NO.value

    with pytest.raises(ValueError):
        dataset.diabetes = 2

def test_depression():
    dataset = Dataset()
    dataset.depression = Decision.YES.value
    assert dataset.depression == Decision.YES.value

    with pytest.raises(ValueError):
        dataset.depression = 2

def test_head_injury():
    dataset = Dataset()
    dataset.head_injury = Decision.NO.value
    assert dataset.head_injury == Decision.NO.value

    with pytest.raises(ValueError):
        dataset.head_injury = 2

def test_hypertension():
    dataset = Dataset()
    dataset.hypertension = Decision.YES.value
    assert dataset.hypertension == Decision.YES.value

    with pytest.raises(ValueError):
        dataset.hypertension = 2

def test_systolic_bp():
    dataset = Dataset()
    dataset.systolic_bp = 130.0
    assert dataset.systolic_bp == 130.0

    with pytest.raises(ValueError):
        dataset.systolic_bp = 180.0

def test_diastolic_bp():
    dataset = Dataset()
    dataset.diastolic_bp = 85.0
    assert dataset.diastolic_bp == 85.0

    with pytest.raises(ValueError):
        dataset.diastolic_bp = 120.0

def test_cholesterol_total():
    dataset = Dataset()
    dataset.cholesterol_total = 200.0
    assert dataset.cholesterol_total == 200.0

    with pytest.raises(ValueError):
        dataset.cholesterol_total = 350.0

def test_cholesterol_ldl():
    dataset = Dataset()
    dataset.cholesterol_ldl = 120.0
    assert dataset.cholesterol_ldl == 120.0

    with pytest.raises(ValueError):
        dataset.cholesterol_ldl = 250.0

def test_cholesterol_hdl():
    dataset = Dataset()
    dataset.cholesterol_hdl = 60.0
    assert dataset.cholesterol_hdl == 60.0

    with pytest.raises(ValueError):
        dataset.cholesterol_hdl = 150.0

def test_cholesterol_triglycerides():
    dataset = Dataset()
    dataset.cholesterol_triglycerides = 200.0
    assert dataset.cholesterol_triglycerides == 200.0

    with pytest.raises(ValueError):
        dataset.cholesterol_triglycerides = 450.0

def test_mmse():
    dataset = Dataset()
    dataset.mmse = 25.0
    assert dataset.mmse == 25.0

    with pytest.raises(ValueError):
        dataset.mmse = 35.0

def test_functional_assessment():
    dataset = Dataset()
    dataset.functional_assessment = 7.0
    assert dataset.functional_assessment == 7.0

    with pytest.raises(ValueError):
        dataset.functional_assessment = 15.0

def test_memory_complaints():
    dataset = Dataset()
    dataset.memory_complaints = Decision.NO.value
    assert dataset.memory_complaints == Decision.NO.value

    with pytest.raises(ValueError):
        dataset.memory_complaints = 2

def test_behavioral_problems():
    dataset = Dataset()
    dataset.behavioral_problems = Decision.YES.value
    assert dataset.behavioral_problems == Decision.YES.value

    with pytest.raises(ValueError):
        dataset.behavioral_problems = 2

def test_adl():
    dataset = Dataset()
    dataset.adl = 8.0
    assert dataset.adl == 8.0

    with pytest.raises(ValueError):
        dataset.adl = 15.0

def test_confusion():
    dataset = Dataset()
    dataset.confusion = Decision.NO.value
    assert dataset.confusion == Decision.NO.value

    with pytest.raises(ValueError):
        dataset.confusion = 2

def test_disorientation():
    dataset = Dataset()
    dataset.disorientation = Decision.YES.value
    assert dataset.disorientation == Decision.YES.value

    with pytest.raises(ValueError):
        dataset.disorientation = 2

def test_personality_changes():
    dataset = Dataset()
    dataset.personality_changes = Decision.NO.value
    assert dataset.personality_changes == Decision.NO.value

    with pytest.raises(ValueError):
        dataset.personality_changes = 2

def test_difficulty_completing_tasks():
    dataset = Dataset()
    dataset.difficulty_completing_tasks = Decision.YES.value
    assert dataset.difficulty_completing_tasks == Decision.YES.value

    with pytest.raises(ValueError):
        dataset.difficulty_completing_tasks = 2

def test_forgetfulness():
    dataset = Dataset()
    dataset.forgetfulness = Decision.NO.value
    assert dataset.forgetfulness == Decision.NO.value

    with pytest.raises(ValueError):
        dataset.forgetfulness = 2


def test_get_dataframe():
    dataset = Dataset()
    dataset.age = 65.0
    dataset.gender = Gender.MALE.value
    dataset.ethnicity = Ethnicity.CAUCASIAN.value
    dataset.education_level = EducationLevel.BACHELORS.value
    dataset.bmi = 25.0
    dataset.smoking = Decision.NO.value
    dataset.alcohol_consumption = 5.0
    dataset.physical_activity = 3.0
    dataset.diet_quality = 7.0
    dataset.sleep_quality = 8.0
    dataset.family_history_alzheimers = Decision.NO.value
    dataset.cardiovascular_disease = Decision.NO.value
    dataset.diabetes = Decision.NO.value
    dataset.depression = Decision.NO.value
    dataset.head_injury = Decision.NO.value
    dataset.hypertension = Decision.NO.value
    dataset.systolic_bp = 120.0
    dataset.diastolic_bp = 80.0
    dataset.cholesterol_total = 180.0
    dataset.cholesterol_ldl = 100.0
    dataset.cholesterol_hdl = 50.0
    dataset.cholesterol_triglycerides = 150.0
    dataset.mmse = 28.0
    dataset.functional_assessment = 5.0
    dataset.memory_complaints = Decision.NO.value
    dataset.behavioral_problems = Decision.NO.value
    dataset.adl = 6.0
    dataset.confusion = Decision.NO.value
    dataset.disorientation = Decision.NO.value
    dataset.personality_changes = Decision.NO.value
    dataset.difficulty_completing_tasks = Decision.NO.value
    dataset.forgetfulness = Decision.NO.value

    df = dataset.get_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert df["Age"][0] == 65.0
    assert df["Gender"][0] == Gender.MALE.value
    assert df["Ethnicity"][0] == Ethnicity.CAUCASIAN.value
    assert df["EducationLevel"][0] == EducationLevel.BACHELORS.value
    assert df["BMI"][0] == 25.0
    assert df["Smoking"][0] == Decision.NO.value
    assert df["AlcoholConsumption"][0] == 5.0
    assert df["PhysicalActivity"][0] == 3.0
    assert df["DietQuality"][0] == 7.0
    assert df["SleepQuality"][0] == 8.0
    assert df["FamilyHistoryAlzheimers"][0] == Decision.NO.value
    assert df["CardiovascularDisease"][0] == Decision.NO.value
    assert df["Diabetes"][0] == Decision.NO.value
    assert df["Depression"][0] == Decision.NO.value
    assert df["HeadInjury"][0] == Decision.NO.value
    assert df["Hypertension"][0] == Decision.NO.value
    assert df["SystolicBP"][0] == 120.0
    assert df["DiastolicBP"][0] == 80.0
    assert df["CholesterolTotal"][0] == 180.0
    assert df["CholesterolLDL"][0] == 100.0
    assert df["CholesterolHDL"][0] == 50.0
    assert df["CholesterolTriglycerides"][0] == 150.0
    assert df["MMSE"][0] == 28.0
    assert df["FunctionalAssessment"][0] == 5.0
    assert df["MemoryComplaints"][0] == Decision.NO.value
    assert df["BehavioralProblems"][0] == Decision.NO.value
    assert df["ADL"][0] == 6.0
    assert df["Confusion"][0] == Decision.NO.value
    assert df["Disorientation"][0] == Decision.NO.value
    assert df["PersonalityChanges"][0] == Decision.NO.value
    assert df["DifficultyCompletingTasks"][0] == Decision.NO.value
    assert df["Forgetfulness"][0] == Decision.NO.value
