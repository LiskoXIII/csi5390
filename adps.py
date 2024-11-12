import sys

from ui.ADPS import Ui_ADPS

from PySide6.QtWidgets import QApplication, QMainWindow

class Patient:

    def __init__(self):
        pass

class Result:

    def __init__(self):
        pass


class ADPS(QMainWindow, Ui_ADPS):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)

    window = ADPS()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()