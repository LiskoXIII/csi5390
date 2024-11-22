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
    assert df['age'][0] == 65.0
    assert df['gender'][0] == Gender.MALE.value
    assert df['ethnicity'][0] == Ethnicity.CAUCASIAN.value
    assert df['education_level'][0] == EducationLevel.BACHELORS.value
    assert df['bmi'][0] == 25.0
    assert df['smoking'][0] == Decision.NO.value
    assert df['alcohol_consumption'][0] == 5.0
    assert df['physical_activity'][0] == 3.0
    assert df['diet_quality'][0] == 7.0
    assert df['sleep_quality'][0] == 8.0
    assert df['family_history_alzheimers'][0] == Decision.NO.value
    assert df['cardiovascular_disease'][0] == Decision.NO.value
    assert df['diabetes'][0] == Decision.NO.value
    assert df['depression'][0] == Decision.NO.value
    assert df['head_injury'][0] == Decision.NO.value
    assert df['hypertension'][0] == Decision.NO.value
    assert df['systolic_bp'][0] == 120.0
    assert df['diastolic_bp'][0] == 80.0
    assert df['cholesterol_total'][0] == 180.0
    assert df['cholesterol_ldl'][0] == 100.0
    assert df['cholesterol_hdl'][0] == 50.0
    assert df['cholesterol_triglycerides'][0] == 150.0
    assert df['mmse'][0] == 28.0
    assert df['functional_assessment'][0] == 5.0
    assert df['memory_complaints'][0] == Decision.NO.value
    assert df['behavioral_problems'][0] == Decision.NO.value
    assert df['adl'][0] == 6.0
    assert df['confusion'][0] == Decision.NO.value
    assert df['disorientation'][0] == Decision.NO.value
    assert df['personality_changes'][0] == Decision.NO.value
    assert df['difficulty_completing_tasks'][0] == Decision.NO.value
    assert df['forgetfulness'][0] == Decision.NO.value