
from enum import Enum
import pandas as pd

class Gender(Enum):
    """
    Enum class representing gender.

    Attributes:
        MALE (int): Represents male gender with a value of 0.
        FEMALE (int): Represents female gender with a value of 1.
    """
    MALE = 0
    FEMALE = 1

class Ethnicity(Enum):
    """
    Enum class representing different ethnicities.

    Attributes:
        CAUCASIAN (int): Represents Caucasian ethnicity.
        AFRICAN_AMERICAN (int): Represents African American ethnicity.
        ASIAN (int): Represents Asian ethnicity.
        OTHER (int): Represents other ethnicities not specified.
    """
    CAUCASIAN = 0
    AFRICAN_AMERICAN = 1
    ASIAN = 2
    OTHER = 3

class EducationLevel(Enum):
    """
    Enum class representing different levels of education.

    Attributes:
        NONE (int): Represents no formal education.
        HIGH_SCHOOL (int): Represents a high school level education.
        BACHELORS (int): Represents a bachelor's degree level education.
        HIGHER (int): Represents education higher than a bachelor's degree.
    """
    NONE = 0
    HIGH_SCHOOL = 1
    BACHELORS = 2
    HIGHER = 3

class Decision(Enum):
    """
    An enumeration representing a binary decision.

    Attributes:
        NO (int): Represents a negative decision with a value of 0.
        YES (int): Represents an affirmative decision with a value of 1.
    """
    NO = 0
    YES = 1


class Dataset:
    """
    A class to represent a dataset for various health and cognitive parameters.
    Attributes
    """

    def __init__(self):
        self._age = None
        self._gender = None
        self._ethnicity = None
        self._education_level = None
        self._bmi = None
        self._smoking = None
        self._alcohol_consumption = None
        self._physical_activity = None
        self._diet_quality = None
        self._sleep_quality = None
        self._family_history_alzheimers = None
        self._cardiovascular_disease = None
        self._diabetes = None
        self._depression = None
        self._head_injury = None
        self._hypertension = None
        self._systolic_bp = None
        self._diastolic_bp = None
        self._cholesterol_total = None
        self._cholesterol_ldl = None
        self._cholesterol_hdl = None
        self._cholesterol_triglycerides = None
        self._mmse = None
        self._functional_assessment = None
        self._memory_complaints = None
        self._behavioral_problems = None
        self._adl = None
        self._confusion = None
        self._disorientation = None
        self._personality_changes = None
        self._difficulty_completing_tasks = None
        self._forgetfulness = None
        self._diagnosis = None
        self._doctor_in_charge = None


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: float):
        if 60.0 <= value <= 90.0:
            self._age = value
        else:
            raise ValueError("Age must be float and between 60.0 and 90.0")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value: int):
        if value in Gender._value2member_map_:            
            self._gender = value
        else:
            raise ValueError("Gender must be 0 (Male) or 1 (Female)")

    @property
    def ethnicity(self):
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, value: int):
        if value in Ethnicity._value2member_map_:
            self._ethnicity = value
        else:
            raise ValueError("Ethnicity must be one of the following: 0 (Caucasian), 1 (African American), 2 (Asian), 3 (Other)")

    @property
    def education_level(self):
        return self._education_level

    @education_level.setter
    def education_level(self, value: int):
        if value in EducationLevel._value2member_map_:
            self._education_level = value
        else:
            raise ValueError("Education level must be one of the following: 0 (None), 1 (High School), 2 (Bachelors), 3 (Higher)")
            

    @property
    def bmi(self):
        return self._bmi

    @bmi.setter
    def bmi(self, value: float):
        if 15 <= value <= 40:
            self._bmi = value
        else:
            raise ValueError("BMI must be a float and between 15 and 40")

    @property
    def smoking(self):
        return self._smoking

    @smoking.setter
    def smoking(self, value: int):
        if value in Decision._value2member_map_:
            self._smoking = value
        else:
            raise ValueError("Smoking must be 0 (No) or 1 (Yes)")

    @property
    def alcohol_consumption(self):
        return self._alcohol_consumption

    @alcohol_consumption.setter
    def alcohol_consumption(self, value: float):
        if 0 <= value <= 20:
            self._alcohol_consumption = value
        else:
            raise ValueError("Alcohol consumption must be a float and between 0 and 20")

    @property
    def physical_activity(self):
        return self._physical_activity

    @physical_activity.setter
    def physical_activity(self, value: float):
        if 0 <= value <= 9.99:
            self._physical_activity = value
        else:
            raise ValueError("Physical activity must be a float and between 0 and 9.99")
            
    @property
    def diet_quality(self):
        return self._diet_quality

    @diet_quality.setter
    def diet_quality(self, value: float):
        if 0.01 <= value <= 10.0:
            self._diet_quality = value
        else:
            raise ValueError("Diet quality must be float and between 0.01 and 10.0")

    @property
    def sleep_quality(self):
        return self._sleep_quality

    @sleep_quality.setter
    def sleep_quality(self, value: float):
        if 4.0 <= value <= 10.0:
            self._sleep_quality = value
        else:
            raise ValueError("Sleep quality must be float and between 4.0 and 10.0")


    # Genetic
    @property
    def family_history_alzheimers(self):
        return self._family_history_alzheimers

    @family_history_alzheimers.setter
    def family_history_alzheimers(self, value: int):
        if value in Decision._value2member_map_:
            self._family_history_alzheimers = value
        else:
            raise ValueError("Family history alzheimers must be 0 (No) or 1 (Yes)")

    @property
    def cardiovascular_disease(self):
        return self._cardiovascular_disease

    @cardiovascular_disease.setter
    def cardiovascular_disease(self, value: int):
        if value in Decision._value2member_map_:
            self._cardiovascular_disease = value
        else:
            raise ValueError("Cardiovascular disease must be 0 (No) or 1 (Yes)")

    @property
    def diabetes(self):
        return self._diabetes

    @diabetes.setter
    def diabetes(self, value: int):
        if value in Decision._value2member_map_:
            self._diabetes = value
        else:
            raise ValueError("Diabetes must be 0 (No) or 1 (Yes)")

    @property
    def depression(self):
        return self._depression

    @depression.setter
    def depression(self, value: int):
        if value in Decision._value2member_map_:
            self._depression = value
        else:
            raise ValueError("Depression must be 0 (No) or 1 (Yes)")

    @property
    def head_injury(self):
        return self._head_injury

    @head_injury.setter
    def head_injury(self, value: int):
        if value in Decision._value2member_map_:
            self._head_injury = value
        else:
            raise ValueError("Head injury must be 0 (No) or 1 (Yes)")

    @property
    def hypertension(self):
        return self._hypertension

    @hypertension.setter
    def hypertension(self, value: int):
        if value in Decision._value2member_map_:
            self._hypertension = value
        else:
            raise ValueError("Hypertension must be 0 (No) or 1 (Yes)")

    # Clinical
    @property
    def systolic_bp(self):
        return self._systolic_bp

    @systolic_bp.setter
    def systolic_bp(self, value: float):
        value = round(value, 0)
        if 90 <= value <= 179:
            self._systolic_bp = value
        else:
            raise ValueError("Systolic BP must be float and between 90 and 179")

    @property
    def diastolic_bp(self):
        return self._diastolic_bp

    @diastolic_bp.setter
    def diastolic_bp(self, value: float):
        value = round(value, 0)
        if 60 <= value <= 119:
            self._diastolic_bp = value
        else:
            raise ValueError("Diastolic BP must be float and between 60 and 119")

    @property
    def cholesterol_total(self):
        return self._cholesterol_total

    @cholesterol_total.setter
    def cholesterol_total(self, value: float):
        if 150.0 <= value <= 300.0:
            self._cholesterol_total = value
        else:
            raise ValueError("Cholesterol total must be float and between 150.0 and 300.0")

    @property
    def cholesterol_ldl(self):
        return self._cholesterol_ldl

    @cholesterol_ldl.setter
    def cholesterol_ldl(self, value: float):
        if 50.0 <= value <= 200.0:
            self._cholesterol_ldl = value
        else:
            raise ValueError("Cholesterol LDL must be float and between 50.0 and 200.0")

    @property
    def cholesterol_hdl(self):
        return self._cholesterol_hdl

    @cholesterol_hdl.setter
    def cholesterol_hdl(self, value: float):
        if 20.0 <= value <= 100.0:
            self._cholesterol_hdl = value
        else:
            raise ValueError("Cholesterol HDL must be float and between 20.0 and 100.0")

    @property
    def cholesterol_triglycerides(self):
        return self._cholesterol_triglycerides

    @cholesterol_triglycerides.setter
    def cholesterol_triglycerides(self, value: float):
        if 50.0 <= value <= 400.0:
            self._cholesterol_triglycerides = value
        else:
            raise ValueError("Cholesterol Triglycerides must be float and between 50.0 and 400.0")

    # Cognitive
    @property
    def mmse(self):
        return self._mmse

    @mmse.setter
    def mmse(self, value: float):
        if 0.01 <= value <= 30.0:
            self._mmse = value
        else:
            raise ValueError("MMSE must be float and between 0.01 and 10.0")

    @property
    def functional_assessment(self):
        return self._functional_assessment

    @functional_assessment.setter
    def functional_assessment(self, value: float):
        if 0.0 <= value <= 10.0:
            self._functional_assessment = value
        else:
            raise ValueError("Functional assessment must be float and between 0.0 and 10.0")

    @property
    def memory_complaints(self):
        return self._memory_complaints

    @memory_complaints.setter
    def memory_complaints(self, value: int):
        if value in Decision._value2member_map_:
            self._memory_complaints = value
        else:
            raise ValueError("Memory complaints must be 0 (No) or 1 (Yes)")

    @property
    def behavioral_problems(self):
        return self._behavioral_problems

    @behavioral_problems.setter
    def behavioral_problems(self, value: int):
        if value in Decision._value2member_map_:
            self._behavioral_problems = value
        else:
            raise ValueError("Behavioral problems must be 0 (No) or 1 (Yes)")

    @property
    def adl(self):
        return self._adl

    @adl.setter
    def adl(self, value: float):
        if 0.0 <= value <= 10.0:
            self._adl = value
        else:
            raise ValueError("ADL must be float and between 0.0 and 10.0")

    @property
    def confusion(self):
        return self._confusion

    @confusion.setter
    def confusion(self, value: int):
        if value in Decision._value2member_map_:
            self._confusion = value
        else:
            raise ValueError("Confusion must be 0 (No) or 1 (Yes)")

    @property
    def disorientation(self):
        return self._disorientation

    @disorientation.setter
    def disorientation(self, value: int):
        if value in Decision._value2member_map_:
            self._disorientation = value
        else:
            raise ValueError("Disorientation must be 0 (No) or 1 (Yes)")

    @property
    def personality_changes(self):
        return self._personality_changes

    @personality_changes.setter
    def personality_changes(self, value: int):
        if value in Decision._value2member_map_:
            self._personality_changes = value
        else:
            raise ValueError("Personality changes must be 0 (No) or 1 (Yes)")

    @property
    def difficulty_completing_tasks(self):
        return self._difficulty_completing_tasks

    @difficulty_completing_tasks.setter
    def difficulty_completing_tasks(self, value: int):
        if value in Decision._value2member_map_:
            self._difficulty_completing_tasks = value
        else:
            raise ValueError("Difficulty completing tasks must be 0 (No) or 1 (Yes)")

    @property
    def forgetfulness(self):
        return self._forgetfulness

    @forgetfulness.setter
    def forgetfulness(self, value: int):
        if value in Decision._value2member_map_:
            self._forgetfulness = value
        else:
            raise ValueError("Forgetfulness must be 0 (No) or 1 (Yes)")
    
    def to_dataframe(self):
        """
        Converts the dataset attributes to a pandas DataFrame.
        Returns:
            pd.DataFrame: A DataFrame containing the dataset attributes with the following columns:
                - Age
                - Gender
                - Ethnicity
                - EducationLevel
                - BMI
                - Smoking
                - AlcoholConsumption
                - PhysicalActivity
                - DietQuality
                - SleepQuality
                - FamilyHistoryAlzheimers
                - CardiovascularDisease
                - Diabetes
                - Depression
                - HeadInjury
                - Hypertension
                - SystolicBP
                - DiastolicBP
                - CholesterolTotal
                - CholesterolLDL
                - CholesterolHDL
                - CholesterolTriglycerides
                - MMSE
                - FunctionalAssessment
                - MemoryComplaints
                - BehavioralProblems
                - ADL
                - Confusion
                - Disorientation
                - PersonalityChanges
                - DifficultyCompletingTasks
                - Forgetfulness
        """
        data = {
            'Age': [self._age],
            'Gender': [self._gender],
            'Ethnicity': [self._ethnicity],
            'EducationLevel': [self._education_level],
            'BMI': [self._bmi],
            'Smoking': [self._smoking],
            'AlcoholConsumption': [self._alcohol_consumption],
            'PhysicalActivity': [self._physical_activity],
            'DietQuality': [self._diet_quality],
            'SleepQuality': [self._sleep_quality],
            'FamilyHistoryAlzheimers': [self._family_history_alzheimers],
            'CardiovascularDisease': [self._cardiovascular_disease],
            'Diabetes': [self._diabetes],
            'Depression': [self._depression],
            'HeadInjury': [self._head_injury],
            'Hypertension': [self._hypertension],
            'SystolicBP': [self._systolic_bp],
            'DiastolicBP': [self._diastolic_bp],
            'CholesterolTotal': [self._cholesterol_total],
            'CholesterolLDL': [self._cholesterol_ldl],
            'CholesterolHDL': [self._cholesterol_hdl],
            'CholesterolTriglycerides': [self._cholesterol_triglycerides],
            'MMSE': [self._mmse],
            'FunctionalAssessment': [self._functional_assessment],
            'MemoryComplaints': [self._memory_complaints],
            'BehavioralProblems': [self._behavioral_problems],
            'ADL': [self._adl],
            'Confusion': [self._confusion],
            'Disorientation': [self._disorientation],
            'PersonalityChanges': [self._personality_changes],
            'DifficultyCompletingTasks': [self._difficulty_completing_tasks],
            'Forgetfulness': [self._forgetfulness]
        }

        return pd.DataFrame(data)
