import sys
import os

from prediction.predict import make_prediction
from prediction.analysis import analyze
from patient import Patient
from dataset import EducationLevel, Ethnicity
from ui.ui_adps import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow, QProgressDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class ADPS(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_ui()
        self.widgetClinical.setVisible(False)
        self.widgetCognitive.setVisible(False)
        self.widgetResult.setVisible(False)
        self.widgetHomepage.setVisible(False)
        self.widgetPatient.setVisible(False)
        self.pushButtonBack.setVisible(False)
        self.pushButtonBack.setEnabled(False)
        self.labelPatientID.setVisible(False)

        self.patient: Patient = None
        self.cognitive_complete: bool = False
        self.clinical_complete: bool = False
        self.patient_complete: bool = False


    def connect_ui(self):
        self.pushButtonBack.clicked.connect(self.goto_login)
        self.loginSubmit.clicked.connect(self.login_submit)
        self.cognitive_button.clicked.connect(self.goto_cognitive)
        self.submitButtonCognitive.clicked.connect(self.cognitiveSubmit)
        self.genetic_button.clicked.connect(self.goto_clinical)
        self.submitButtonClinical.clicked.connect(self.clinicalSubmit)
        self.patient_button.clicked.connect(self.goto_patient)
        self.submitButtonPatient.clicked.connect(self.patientSubmit)
        self.results_button.clicked.connect(self.goto_result)

    def goto_login(self):
        reply = QMessageBox.question(self, 'Warning', 'All progress will be lost. Do you want to continue?', 
                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.widgetLogin.setEnabled(True)
        self.widgetLogin.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)
        self.widgetCognitive.setVisible(False)
        self.widgetCognitive.setEnabled(False)
        self.widgetClinical.setVisible(False)
        self.widgetClinical.setEnabled(False)
        self.widgetPatient.setVisible(False)
        self.widgetPatient.setEnabled(False)
        self.widgetResult.setVisible(False)
        self.widgetResult.setEnabled(False)
        self.reset()

    def reset(self):
        self.pushButtonBack.setVisible(False)
        self.pushButtonBack.setEnabled(False)
        self.labelPatientID.setVisible(False)
        self.cognitive_complete = False
        self.clinical_complete = False
        self.patient_complete = False
        self.cognitive_status.setText("Incomplete")
        self.cognitive_status.setStyleSheet("color: red;")
        self.genetic_status.setText("Incomplete")
        self.genetic_status.setStyleSheet("color: red;")
        self.patient_status.setText("Incomplete")
        self.patient_status.setStyleSheet("color: red;")
        self.results_button.setEnabled(False)
        self.results_button.setStyleSheet("color: red;")
        self.loginPatientID.clear()
        self.statusbar.clearMessage()

    def login_submit(self):
        self.patient = Patient(self.loginPatientID.text())
        self.statusbar.showMessage(f"Logged in as {self.patient.id}")
        self.widgetHomepage.setEnabled(True)
        self.widgetHomepage.setVisible(True)
        self.widgetLogin.setVisible(False)
        self.widgetLogin.setEnabled(False)
        self.pushButtonBack.setEnabled(True)
        self.pushButtonBack.setVisible(True)
        self.labelPatientID.setVisible(True)
        self.labelPatientID.setText(f"Patient ID: {self.patient.id}")

    def goto_cognitive(self):
        self.widgetCognitive.setEnabled(True)
        self.widgetCognitive.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)

    def cognitiveSubmit(self):
        try:
            self.patient.data.mmse = self.mmseCognitive.value()
            self.patient.data.functional_assessment = self.functionalAssesment.value()
            self.patient.data.memory_complaints = int(self.memoryComplaints.isChecked())
            self.patient.data.behavioral_problems = int(self.behavioralProblems.isChecked())
            self.patient.data.adl = self.adl.value()
            self.patient.data.confusion = int(self.confusion.isChecked())
            self.patient.data.disorientation = int(self.disorientation.isChecked())
            self.patient.data.personality_changes = int(self.personalityChanges.isChecked())
            self.patient.data.difficulty_completing_tasks = int(self.diffCompTask.isChecked())
            self.patient.data.forgetfulness = int(self.forgetfulness.isChecked())
        except ValueError as e:
            self.statusbar.showMessage(f"ERROR: {e}")
        self.statusbar.showMessage("Cognitive data submitted!")
        self.widgetHomepage.setEnabled(True)
        self.widgetHomepage.setVisible(True)
        self.widgetCognitive.setVisible(False)
        self.widgetCognitive.setEnabled(False)
        self.cognitive_status.setText("Complete")
        self.cognitive_status.setStyleSheet("color: green;")
        self.cognitive_complete = True
        self.data_complete()

    def goto_clinical(self):
        self.widgetClinical.setEnabled(True)
        self.widgetClinical.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)

    def clinicalSubmit(self):
        try:
            self.patient.data.family_history_alzheimers = int(self.famAlzClinical.isChecked())
            self.patient.data.cardiovascular_disease = int(self.cardiovascularDiseaseClinical.isChecked())
            self.patient.data.diabetes = int(self.diabetesClinical.isChecked())
            self.patient.data.depression = int(self.depressionClinical.isChecked())
            self.patient.data.head_injury = int(self.headInjuryClinical.isChecked())
            self.patient.data.hypertension = int(self.hypertensionClinical.isChecked())
            self.patient.data.systolic_bp = self.sysBPClinical.value()
            self.patient.data.diastolic_bp = self.dasBPClinical.value()
            self.patient.data.cholesterol_total = self.cholTotalClinical.value()
            self.patient.data.cholesterol_ldl = self.cholLDLClinical.value()
            self.patient.data.cholesterol_hdl = self.cholHDLClinical.value()
            self.patient.data.cholesterol_triglycerides = self.cholTriClinical.value()
        except ValueError as e:
            self.statusbar.showMessage(f"ERROR: {e}")
        self.statusbar.showMessage("Clinical data submitted!")
        self.widgetHomepage.setEnabled(True)
        self.widgetHomepage.setVisible(True)
        self.widgetClinical.setVisible(False)
        self.widgetClinical.setEnabled(False)
        self.genetic_status.setText("Complete")
        self.genetic_status.setStyleSheet("color: green;")
        self.clinical_complete = True
        self.data_complete()


    def goto_patient(self): 
        self.widgetPatient.setEnabled(True)
        self.widgetPatient.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)

    def patientSubmit(self):
        try:
            self.patient.data.age = self.agePatient.value()
            self.patient.data.gender = int(self.malePatient.isChecked())
            self.patient.data.ethnicity =  Ethnicity[self.ethnicityPatient.currentText().upper().replace(" ", "_")]
            self.patient.data.education_level = EducationLevel[self.educationPatient.currentText().upper().replace(" ", "_")]
            self.patient.data.bmi = self.bmiPatient.value()
            self.patient.data.smoking = int(self.smokingPatient.isChecked())
            self.patient.data.alcohol_consumption = self.alcoholPatient.value()
            self.patient.data.physical_activity = self.physicalPatient.value()
            self.patient.data.diet_quality = self.dietPatient.value()
            self.patient.data.sleep_quality = self.sleepPatient.value()
        except ValueError as e:
            self.statusbar.showMessage(f"ERROR: {e}")
        self.statusbar.showMessage("Patient data submitted!")
        self.widgetHomepage.setEnabled(True)
        self.widgetHomepage.setVisible(True)
        self.widgetPatient.setVisible(False)
        self.widgetPatient.setEnabled(False)
        self.patient_status.setText("Complete")
        self.patient_status.setStyleSheet("color: green;")
        self.patient_complete = True
        self.data_complete()

    def data_complete(self):
        if self.cognitive_complete and self.clinical_complete and self.patient_complete:
            self.statusbar.showMessage("All data submitted!")
            self.results_button.setEnabled(True)
            self.results_button.setStyleSheet("color: green;")

    def goto_result(self):

        progress = QProgressDialog("Making prediction...", None, 0, 5, self)
        progress.setWindowTitle("Predicting")
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        progress.setAutoClose(True)
        progress.show()
        QApplication.processEvents()
        progress.setValue(1)
        QApplication.processEvents()

        self.patient.result = make_prediction(self.patient.data.to_dataframe())
        progress.setValue(2)
        QApplication.processEvents()

        analyze(self.patient.data.to_dataframe(), self.patient.result, progress)

        if self.patient.result == 1:
            self.label_diagnosis.setText("Positive for Alzheimer's Disease")
            self.label_diagnosis.setStyleSheet("color: red;")
        else:
            self.label_diagnosis.setText("Negative for Alzheimer's Disease")
            self.label_diagnosis.setStyleSheet("color: green;")

        self.labelADL.setPixmap(QPixmap(os.path.join("prediction","plot_ADL.png")))
        self.labelFA.setPixmap(QPixmap(os.path.join("prediction","plot_FunctionalAssessment.png")))
        self.labelMMSE.setPixmap(QPixmap(os.path.join("prediction","plot_MMSE.png")))

        self.widgetResult.setEnabled(True)
        self.widgetResult.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)


def main():
    app = QApplication(sys.argv)

    window = ADPS()
    window.resize(1200, 800)
    window.show()

    app.exec()

if __name__ == "__main__":
    main()
