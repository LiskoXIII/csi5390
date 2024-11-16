import sys
from dataclasses import dataclass

from ui.ADPS import Ui_ADPS

from PySide6.QtWidgets import QApplication, QMainWindow

@dataclass
class Dataset:

    # Patient Information
    # Patient ID
    PatientID: int = None
    # Demographic Details
    Age: int = None
    Gender: int = None
    Ethnicity: int = None
    EducationLevel: int = None
    # Lifestyle Factors
    BMI = None
    Smoking = None
    AlcoholConsumption = None
    PhysicalActivity = None
    DietQuality = None
    SleepQuality = None
    # Medical History
    FamilyHistoryAlzheimers = None
    CardiovascularDisease = None
    Diabetes = None
    Depression = None
    HeadInjury = None
    Hypertension = None
    # Clinical Measurements
    SystolicBP = None
    DiastolicBP = None
    CholesterolTotal = None
    CholesterolLDL = None
    CholesterolHDL = None
    CholesterolTriglycerides = None
    # Cognitive and Functional Assessments
    MMSE = None
    FunctionalAssessment = None
    MemoryComplaints = None
    BehavioralProblems = None
    ADL = None
    # Symptoms
    Confusion = None
    Disorientation = None
    PersonalityChanges = None
    DifficultyCompletingTasks = None
    Forgetfulness = None
    # Diagnosis Information
    Diagnosis = None
    # Confidential Information
    DoctorInCharge = None


class Patient:

    def __init__(self):
        self.result: Result = Result()

    

    


class Result:

    def __init__(self):
        pass


class ADPS(QMainWindow, Ui_ADPS):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_ui(self)


    def connect_ui(self):
        pass


def main():
    app = QApplication(sys.argv)

    window = ADPS()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()
