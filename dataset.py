
from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = 0
    FEMALE = 1

class Ethnicity(Enum):
    CAUCASIAN = 0
    AFRICAN_AMERICAN = 1
    ASIAN = 2
    OTHER = 3

class EducationLevel(Enum):
    NONE = 0
    HIGH_SCHOOL = 1
    BACHELORS = 2
    HIGHER = 3

class Decision(Enum):
    NO = 0
    YES = 1


class Dataset:

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
        if 60.0 >= value <= 90.0:
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
        if 15 >= value <= 40:
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
        if 0 >= value <= 20:
            self._alcohol_consumption = value
        else:
            raise ValueError("Alcohol consumption must be a float and between 0 and 20")

    @property
    def physical_activity(self):
        return self._physical_activity

    @physical_activity.setter
    def physical_activity(self, value: float):
        if 0 >= value <= 9.99:
            self._physical_activity = value
        else:
            raise ValueError("Physical activity must be a float and between 0 and 9.99")
            
    @property
    def diet_quality(self):
        return self._diet_quality

    @diet_quality.setter
    def diet_quality(self, value):
        self._diet_quality = value

    @property
    def sleep_quality(self):
        return self._sleep_quality

    @sleep_quality.setter
    def sleep_quality(self, value):
        self._sleep_quality = value

    @property
    def family_history_alzheimers(self):
        return self._family_history_alzheimers

    @family_history_alzheimers.setter
    def family_history_alzheimers(self, value):
        self._family_history_alzheimers = value

    @property
    def cardiovascular_disease(self):
        return self._cardiovascular_disease

    @cardiovascular_disease.setter
    def cardiovascular_disease(self, value):
        self._cardiovascular_disease = value

    @property
    def diabetes(self):
        return self._diabetes

    @diabetes.setter
    def diabetes(self, value):
        self._diabetes = value

    @property
    def depression(self):
        return self._depression

    @depression.setter
    def depression(self, value):
        self._depression = value

    @property
    def head_injury(self):
        return self._head_injury

    @head_injury.setter
    def head_injury(self, value):
        self._head_injury = value

    @property
    def hypertension(self):
        return self._hypertension

    @hypertension.setter
    def hypertension(self, value):
        self._hypertension = value

    @property
    def systolic_bp(self):
        return self._systolic_bp

    @systolic_bp.setter
    def systolic_bp(self, value):
        self._systolic_bp = value

    @property
    def diastolic_bp(self):
        return self._diastolic_bp

    @diastolic_bp.setter
    def diastolic_bp(self, value):
        self._diastolic_bp = value

    @property
    def cholesterol_total(self):
        return self._cholesterol_total

    @cholesterol_total.setter
    def cholesterol_total(self, value):
        self._cholesterol_total = value

    @property
    def cholesterol_ldl(self):
        return self._cholesterol_ldl

    @cholesterol_ldl.setter
    def cholesterol_ldl(self, value):
        self._cholesterol_ldl = value

    @property
    def cholesterol_hdl(self):
        return self._cholesterol_hdl

    @cholesterol_hdl.setter
    def cholesterol_hdl(self, value):
        self._cholesterol_hdl = value

    @property
    def cholesterol_triglycerides(self):
        return self._cholesterol_triglycerides

    @cholesterol_triglycerides.setter
    def cholesterol_triglycerides(self, value):
        self._cholesterol_triglycerides = value

    @property
    def mmse(self):
        return self._mmse

    @mmse.setter
    def mmse(self, value):
        self._mmse = value

    @property
    def functional_assessment(self):
        return self._functional_assessment

    @functional_assessment.setter
    def functional_assessment(self, value):
        self._functional_assessment = value

    @property
    def memory_complaints(self):
        return self._memory_complaints

    @memory_complaints.setter
    def memory_complaints(self, value):
        self._memory_complaints = value

    @property
    def behavioral_problems(self):
        return self._behavioral_problems

    @behavioral_problems.setter
    def behavioral_problems(self, value):
        self._behavioral_problems = value

    @property
    def adl(self):
        return self._adl

    @adl.setter
    def adl(self, value):
        self._adl = value

    @property
    def confusion(self):
        return self._confusion

    @confusion.setter
    def confusion(self, value):
        self._confusion = value

    @property
    def disorientation(self):
        return self._disorientation

    @disorientation.setter
    def disorientation(self, value):
        self._disorientation = value

    @property
    def personality_changes(self):
        return self._personality_changes

    @personality_changes.setter
    def personality_changes(self, value):
        self._personality_changes = value

    @property
    def difficulty_completing_tasks(self):
        return self._difficulty_completing_tasks

    @difficulty_completing_tasks.setter
    def difficulty_completing_tasks(self, value):
        self._difficulty_completing_tasks = value

    @property
    def forgetfulness(self):
        return self._forgetfulness

    @forgetfulness.setter
    def forgetfulness(self, value):
        self._forgetfulness = value

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value

    @property
    def doctor_in_charge(self):
        return self._doctor_in_charge

    @doctor_in_charge.setter
    def doctor_in_charge(self, value):
        self._doctor_in_charge = value