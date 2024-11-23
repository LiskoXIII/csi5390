import sys

from patient import Patient
from ui.ui_adps import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow


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

        self.patient = None


    def connect_ui(self):
        self.loginSubmit.clicked.connect(self.login_submit)
        self.cognitive_button.clicked.connect(self.cognitive)
        self.genetic_button.clicked.connect(self.clinical)
        self.patient_button.clicked.connect(self.patient)
        self.results_button.clicked.connect(self.result)

    def login_submit(self):
        self.patient = Patient(self.loginPatientID.text())
        self.statusbar.showMessage(f"Logged in as {self.patient.id}")
        self.widgetHomepage.setEnabled(True)
        self.widgetHomepage.setVisible(True)
        self.widgetLogin.setVisible(False)
        self.widgetLogin.setEnabled(False)

    def cognitive(self):
        self.widgetCognitive.setEnabled(True)
        self.widgetCognitive.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)

    def clinical(self):
        self.widgetClinical.setEnabled(True)
        self.widgetClinical.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)

    def patient(self): 
        self.widgetPatient.setEnabled(True)
        self.widgetPatient.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)

    def result(self):
        self.widgetResult.setEnabled(True)
        self.widgetResult.setVisible(True)
        self.widgetHomepage.setVisible(False)
        self.widgetHomepage.setEnabled(False)


def main():
    app = QApplication(sys.argv)

    window = ADPS()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()
