# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adps.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)
import ui.adps_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1283, 1417)
        icon = QIcon()
        icon.addFile(u":/icon/ADPS_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"#MainWindow {\n"
"background-color: rgb(176, 125, 180);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralWidget {\n"
"background-color: rgb(176, 125, 180);\n"
"}")
        self.verticalLayoutMain = QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setSpacing(0)
        self.verticalLayoutMain.setObjectName(u"verticalLayoutMain")
        self.verticalLayoutMain.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 60))
        self.widget.setStyleSheet(u"#widget { background-color: rgb(176, 125, 180);\n"
" }")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(120, 60))
        self.label.setStyleSheet(u"#label { background-color: rgb(176, 125, 180);\n"
" }")
        self.label.setPixmap(QPixmap(u":/icon/ADPS_logo_w.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_17)

        self.labelPatientID = QLabel(self.widget)
        self.labelPatientID.setObjectName(u"labelPatientID")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelPatientID.setFont(font)

        self.horizontalLayout_5.addWidget(self.labelPatientID)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)

        self.pushButtonBack = QPushButton(self.widget)
        self.pushButtonBack.setObjectName(u"pushButtonBack")
        self.pushButtonBack.setMinimumSize(QSize(100, 30))
        self.pushButtonBack.setStyleSheet(u"#pushButtonBack {\n"
"	background-color: rgb(156, 105, 160);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButtonBack)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_16)


        self.verticalLayoutMain.addWidget(self.widget)

        self.widgetLogin = QWidget(self.centralwidget)
        self.widgetLogin.setObjectName(u"widgetLogin")
        self.widgetLogin.setEnabled(True)
        self.widgetLogin.setStyleSheet(u"#widgetLogin { background-color: rgb(176, 125, 180);\n"
" }")
        self.gridLayout = QGridLayout(self.widgetLogin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 7, 2, 1, 1)

        self.loginPatientID = QLineEdit(self.widgetLogin)
        self.loginPatientID.setObjectName(u"loginPatientID")
        self.loginPatientID.setMinimumSize(QSize(200, 0))
        self.loginPatientID.setMaximumSize(QSize(300, 16777215))
        self.loginPatientID.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.loginPatientID, 10, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.loginSubmit = QPushButton(self.widgetLogin)
        self.loginSubmit.setObjectName(u"loginSubmit")
        self.loginSubmit.setEnabled(True)
        self.loginSubmit.setMinimumSize(QSize(200, 0))
        self.loginSubmit.setMaximumSize(QSize(300, 16777215))
        self.loginSubmit.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.loginSubmit, 11, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 13, 1, 1, 1)

        self.loginTitle = QLabel(self.widgetLogin)
        self.loginTitle.setObjectName(u"loginTitle")
        self.loginTitle.setMinimumSize(QSize(151, 71))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.loginTitle.setFont(font1)
        self.loginTitle.setTextFormat(Qt.TextFormat.AutoText)
        self.loginTitle.setScaledContents(True)
        self.loginTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loginTitle.setWordWrap(False)

        self.gridLayout.addWidget(self.loginTitle, 8, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_3, 9, 1, 1, 1)


        self.verticalLayoutMain.addWidget(self.widgetLogin)

        self.widgetHomepage = QWidget(self.centralwidget)
        self.widgetHomepage.setObjectName(u"widgetHomepage")
        self.widgetHomepage.setEnabled(False)
        self.widgetHomepage.setStyleSheet(u"#widgetHomepage { background-color: rgb(176, 125, 180);\n"
" }")
        self.gridLayout_5 = QGridLayout(self.widgetHomepage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 0, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.frame = QFrame(self.widgetHomepage)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 250))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.GeneticLabel_2 = QLabel(self.frame)
        self.GeneticLabel_2.setObjectName(u"GeneticLabel_2")
        self.GeneticLabel_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.GeneticLabel_2, 0, 0, 1, 1)

        self.cognitive_button = QPushButton(self.frame)
        self.cognitive_button.setObjectName(u"cognitive_button")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(False)
        self.cognitive_button.setFont(font2)

        self.gridLayout_2.addWidget(self.cognitive_button, 2, 0, 1, 1)

        self.cognitive_status = QLabel(self.frame)
        self.cognitive_status.setObjectName(u"cognitive_status")
        self.cognitive_status.setFont(font)
        self.cognitive_status.setStyleSheet(u"color: red;")
        self.cognitive_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.cognitive_status, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.frame_2 = QFrame(self.widgetHomepage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 250))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.genetic_label = QLabel(self.frame_2)
        self.genetic_label.setObjectName(u"genetic_label")

        self.gridLayout_3.addWidget(self.genetic_label, 0, 0, 1, 1)

        self.genetic_status = QLabel(self.frame_2)
        self.genetic_status.setObjectName(u"genetic_status")
        self.genetic_status.setFont(font)
        self.genetic_status.setStyleSheet(u"color: red;")
        self.genetic_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.genetic_status, 1, 0, 1, 1)

        self.genetic_button = QPushButton(self.frame_2)
        self.genetic_button.setObjectName(u"genetic_button")
        self.genetic_button.setFont(font2)

        self.gridLayout_3.addWidget(self.genetic_button, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.frame_3 = QFrame(self.widgetHomepage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 250))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.GeneticLabel_3 = QLabel(self.frame_3)
        self.GeneticLabel_3.setObjectName(u"GeneticLabel_3")
        self.GeneticLabel_3.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.GeneticLabel_3, 0, 0, 1, 1)

        self.patient_status = QLabel(self.frame_3)
        self.patient_status.setObjectName(u"patient_status")
        self.patient_status.setFont(font)
        self.patient_status.setStyleSheet(u"color: red;")
        self.patient_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.patient_status, 1, 0, 1, 1)

        self.patient_button = QPushButton(self.frame_3)
        self.patient_button.setObjectName(u"patient_button")
        self.patient_button.setFont(font2)

        self.gridLayout_4.addWidget(self.patient_button, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 1, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 6, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 2, 3, 1, 1)

        self.frame_4 = QFrame(self.widgetHomepage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 100))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.results_button = QPushButton(self.frame_4)
        self.results_button.setObjectName(u"results_button")
        self.results_button.setFont(font2)
        self.results_button.setStyleSheet(u"color: red;")

        self.verticalLayout.addWidget(self.results_button)


        self.gridLayout_5.addWidget(self.frame_4, 3, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 4, 3, 1, 1)


        self.verticalLayoutMain.addWidget(self.widgetHomepage)

        self.widgetCognitive = QWidget(self.centralwidget)
        self.widgetCognitive.setObjectName(u"widgetCognitive")
        self.widgetCognitive.setEnabled(False)
        self.widgetCognitive.setStyleSheet(u"#widgetCognitive {\n"
"	background-color: rgb(176, 125, 180);\\n\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widgetCognitive)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.widgetCognitive)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.scrollAreaCognitive = QScrollArea(self.widgetCognitive)
        self.scrollAreaCognitive.setObjectName(u"scrollAreaCognitive")
        self.scrollAreaCognitive.setStyleSheet(u"#scrollAreaWidgetContents { background-color: rgb(255, 255, 255); }")
        self.scrollAreaCognitive.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1251, 572))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.behavioralProblems = QCheckBox(self.scrollAreaWidgetContents)
        self.behavioralProblems.setObjectName(u"behavioralProblems")
        self.behavioralProblems.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.behavioralProblems, 3, 3, 1, 1)

        self.functionalAssesment = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.functionalAssesment.setObjectName(u"functionalAssesment")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.functionalAssesment.sizePolicy().hasHeightForWidth())
        self.functionalAssesment.setSizePolicy(sizePolicy1)
        self.functionalAssesment.setAutoFillBackground(True)
        self.functionalAssesment.setMinimum(0.000000000000000)
        self.functionalAssesment.setMaximum(10.000000000000000)

        self.gridLayout_6.addWidget(self.functionalAssesment, 1, 3, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_10, 6, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_5, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 4, 0, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_11, 7, 1, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_8, 4, 1, 1, 1)

        self.adl = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.adl.setObjectName(u"adl")
        sizePolicy1.setHeightForWidth(self.adl.sizePolicy().hasHeightForWidth())
        self.adl.setSizePolicy(sizePolicy1)
        self.adl.setAutoFillBackground(True)
        self.adl.setMinimum(0.000000000000000)
        self.adl.setMaximum(10.000000000000000)

        self.gridLayout_6.addWidget(self.adl, 4, 3, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_13, 9, 1, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_12, 8, 1, 1, 1)

        self.disorientation = QCheckBox(self.scrollAreaWidgetContents)
        self.disorientation.setObjectName(u"disorientation")
        self.disorientation.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.disorientation, 6, 3, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_9, 5, 1, 1, 1)

        self.memoryComplaints = QCheckBox(self.scrollAreaWidgetContents)
        self.memoryComplaints.setObjectName(u"memoryComplaints")
        self.memoryComplaints.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.memoryComplaints, 2, 3, 1, 1)

        self.diffCompTask = QCheckBox(self.scrollAreaWidgetContents)
        self.diffCompTask.setObjectName(u"diffCompTask")
        self.diffCompTask.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.diffCompTask, 8, 3, 1, 1)

        self.personalityChanges = QCheckBox(self.scrollAreaWidgetContents)
        self.personalityChanges.setObjectName(u"personalityChanges")
        self.personalityChanges.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.personalityChanges, 7, 3, 1, 1)

        self.forgetfulness = QCheckBox(self.scrollAreaWidgetContents)
        self.forgetfulness.setObjectName(u"forgetfulness")
        self.forgetfulness.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.forgetfulness, 9, 3, 1, 1)

        self.confusion = QCheckBox(self.scrollAreaWidgetContents)
        self.confusion.setObjectName(u"confusion")
        self.confusion.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.confusion, 5, 3, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 4, 4, 1, 1)

        self.mmseCognitive = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.mmseCognitive.setObjectName(u"mmseCognitive")
        sizePolicy1.setHeightForWidth(self.mmseCognitive.sizePolicy().hasHeightForWidth())
        self.mmseCognitive.setSizePolicy(sizePolicy1)
        self.mmseCognitive.setAutoFillBackground(True)
        self.mmseCognitive.setMinimum(0.010000000000000)
        self.mmseCognitive.setMaximum(30.000000000000000)

        self.gridLayout_6.addWidget(self.mmseCognitive, 0, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 4, 2, 1, 1)

        self.scrollAreaCognitive.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollAreaCognitive)

        self.widget_2 = QWidget(self.widgetCognitive)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.submitButtonCognitive = QPushButton(self.widget_2)
        self.submitButtonCognitive.setObjectName(u"submitButtonCognitive")
        self.submitButtonCognitive.setMaximumSize(QSize(300, 16777215))
        self.submitButtonCognitive.setStyleSheet(u"QPushButton#submitButtonCognitive {\n"
"background-color: rgb(85, 255, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.submitButtonCognitive)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayoutMain.addWidget(self.widgetCognitive)

        self.widgetResult = QWidget(self.centralwidget)
        self.widgetResult.setObjectName(u"widgetResult")
        self.widgetResult.setEnabled(False)
        self.widgetResult.setStyleSheet(u"#widgetResult {\n"
"	background-color: rgb(176, 125, 180);\\n\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widgetResult)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_results = QLabel(self.widgetResult)
        self.label_results.setObjectName(u"label_results")
        sizePolicy.setHeightForWidth(self.label_results.sizePolicy().hasHeightForWidth())
        self.label_results.setSizePolicy(sizePolicy)
        self.label_results.setFont(font1)
        self.label_results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_results)

        self.label_diagnosis = QLabel(self.widgetResult)
        self.label_diagnosis.setObjectName(u"label_diagnosis")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_diagnosis.setFont(font3)
        self.label_diagnosis.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_diagnosis)

        self.scrollAreaResult = QScrollArea(self.widgetResult)
        self.scrollAreaResult.setObjectName(u"scrollAreaResult")
        self.scrollAreaResult.setWidgetResizable(True)
        self.scrollAreaWidgetContentsResult = QWidget()
        self.scrollAreaWidgetContentsResult.setObjectName(u"scrollAreaWidgetContentsResult")
        self.scrollAreaWidgetContentsResult.setGeometry(QRect(0, 0, 1251, 78))
        self.scrollAreaWidgetContentsResult.setStyleSheet(u"background-color: rgb(176, 125, 180)")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContentsResult)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelMMSE = QLabel(self.scrollAreaWidgetContentsResult)
        self.labelMMSE.setObjectName(u"labelMMSE")
        self.labelMMSE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.labelMMSE)

        self.labelADL = QLabel(self.scrollAreaWidgetContentsResult)
        self.labelADL.setObjectName(u"labelADL")
        self.labelADL.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.labelADL)

        self.labelFA = QLabel(self.scrollAreaWidgetContentsResult)
        self.labelFA.setObjectName(u"labelFA")
        self.labelFA.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.labelFA)

        self.scrollAreaResult.setWidget(self.scrollAreaWidgetContentsResult)

        self.verticalLayout_5.addWidget(self.scrollAreaResult)


        self.verticalLayoutMain.addWidget(self.widgetResult)

        self.widgetPatient = QWidget(self.centralwidget)
        self.widgetPatient.setObjectName(u"widgetPatient")
        self.widgetPatient.setEnabled(False)
        self.widgetPatient.setStyleSheet(u"#widgetPatient {\n"
"	background-color: rgb(176, 125, 180);\\n\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widgetPatient)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4Patient = QLabel(self.widgetPatient)
        self.label_4Patient.setObjectName(u"label_4Patient")
        sizePolicy.setHeightForWidth(self.label_4Patient.sizePolicy().hasHeightForWidth())
        self.label_4Patient.setSizePolicy(sizePolicy)
        self.label_4Patient.setFont(font1)
        self.label_4Patient.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4Patient)

        self.scrollAreaPatient = QScrollArea(self.widgetPatient)
        self.scrollAreaPatient.setObjectName(u"scrollAreaPatient")
        self.scrollAreaPatient.setStyleSheet(u"")
        self.scrollAreaPatient.setWidgetResizable(True)
        self.scrollAreaWidgetPatient = QWidget()
        self.scrollAreaWidgetPatient.setObjectName(u"scrollAreaWidgetPatient")
        self.scrollAreaWidgetPatient.setGeometry(QRect(0, 0, 1251, 578))
        self.scrollAreaWidgetPatient.setStyleSheet(u"#scrollAreaWidgetPatient {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetPatient)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 9, 3, 1, 1)

        self.physicalPatient = QDoubleSpinBox(self.scrollAreaWidgetPatient)
        self.physicalPatient.setObjectName(u"physicalPatient")
        sizePolicy1.setHeightForWidth(self.physicalPatient.sizePolicy().hasHeightForWidth())
        self.physicalPatient.setSizePolicy(sizePolicy1)
        self.physicalPatient.setAutoFillBackground(True)
        self.physicalPatient.setMinimum(0.000000000000000)
        self.physicalPatient.setMaximum(9.990000000000000)

        self.gridLayout_8.addWidget(self.physicalPatient, 12, 4, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 9, 0, 1, 1)

        self.educationPatient = QComboBox(self.scrollAreaWidgetPatient)
        self.educationPatient.addItem("")
        self.educationPatient.addItem("")
        self.educationPatient.addItem("")
        self.educationPatient.addItem("")
        self.educationPatient.setObjectName(u"educationPatient")
        sizePolicy1.setHeightForWidth(self.educationPatient.sizePolicy().hasHeightForWidth())
        self.educationPatient.setSizePolicy(sizePolicy1)
        self.educationPatient.setAutoFillBackground(True)

        self.gridLayout_8.addWidget(self.educationPatient, 8, 4, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetPatient)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_14, 7, 2, 1, 1)

        self.smokingPatient = QCheckBox(self.scrollAreaWidgetPatient)
        self.smokingPatient.setObjectName(u"smokingPatient")
        sizePolicy1.setHeightForWidth(self.smokingPatient.sizePolicy().hasHeightForWidth())
        self.smokingPatient.setSizePolicy(sizePolicy1)
        self.smokingPatient.setAutoFillBackground(False)

        self.gridLayout_8.addWidget(self.smokingPatient, 10, 4, 1, 1)

        self.alcoholPatient = QDoubleSpinBox(self.scrollAreaWidgetPatient)
        self.alcoholPatient.setObjectName(u"alcoholPatient")
        sizePolicy1.setHeightForWidth(self.alcoholPatient.sizePolicy().hasHeightForWidth())
        self.alcoholPatient.setSizePolicy(sizePolicy1)
        self.alcoholPatient.setAutoFillBackground(True)
        self.alcoholPatient.setMinimum(0.000000000000000)
        self.alcoholPatient.setMaximum(20.000000000000000)

        self.gridLayout_8.addWidget(self.alcoholPatient, 11, 4, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetPatient)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_15, 10, 2, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetPatient)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_16, 4, 2, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetPatient)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_17, 11, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_14, 9, 5, 1, 1)

        self.genderBoxPatient = QGroupBox(self.scrollAreaWidgetPatient)
        self.genderBoxPatient.setObjectName(u"genderBoxPatient")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.genderBoxPatient.sizePolicy().hasHeightForWidth())
        self.genderBoxPatient.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.genderBoxPatient)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.femalePatient = QRadioButton(self.genderBoxPatient)
        self.buttonGroupGender = QButtonGroup(MainWindow)
        self.buttonGroupGender.setObjectName(u"buttonGroupGender")
        self.buttonGroupGender.addButton(self.femalePatient)
        self.femalePatient.setObjectName(u"femalePatient")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.femalePatient.sizePolicy().hasHeightForWidth())
        self.femalePatient.setSizePolicy(sizePolicy4)
        self.femalePatient.setAutoFillBackground(False)
        self.femalePatient.setStyleSheet(u"color: black;")
        self.femalePatient.setChecked(True)

        self.horizontalLayout_4.addWidget(self.femalePatient)

        self.malePatient = QRadioButton(self.genderBoxPatient)
        self.buttonGroupGender.addButton(self.malePatient)
        self.malePatient.setObjectName(u"malePatient")
        self.malePatient.setAutoFillBackground(False)
        self.malePatient.setStyleSheet(u"color: black;")

        self.horizontalLayout_4.addWidget(self.malePatient)


        self.gridLayout_8.addWidget(self.genderBoxPatient, 6, 4, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetPatient)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_18, 6, 2, 1, 1)

        self.ethnicityPatient = QComboBox(self.scrollAreaWidgetPatient)
        self.ethnicityPatient.addItem("")
        self.ethnicityPatient.addItem("")
        self.ethnicityPatient.addItem("")
        self.ethnicityPatient.addItem("")
        self.ethnicityPatient.setObjectName(u"ethnicityPatient")
        sizePolicy1.setHeightForWidth(self.ethnicityPatient.sizePolicy().hasHeightForWidth())
        self.ethnicityPatient.setSizePolicy(sizePolicy1)
        self.ethnicityPatient.setAutoFillBackground(True)

        self.gridLayout_8.addWidget(self.ethnicityPatient, 7, 4, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetPatient)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_19, 8, 2, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetPatient)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_20, 9, 2, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetPatient)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_21, 14, 2, 1, 1)

        self.sleepPatient = QDoubleSpinBox(self.scrollAreaWidgetPatient)
        self.sleepPatient.setObjectName(u"sleepPatient")
        sizePolicy1.setHeightForWidth(self.sleepPatient.sizePolicy().hasHeightForWidth())
        self.sleepPatient.setSizePolicy(sizePolicy1)
        self.sleepPatient.setAutoFillBackground(True)
        self.sleepPatient.setMinimum(4.000000000000000)
        self.sleepPatient.setMaximum(10.000000000000000)

        self.gridLayout_8.addWidget(self.sleepPatient, 14, 4, 1, 1)

        self.bmiPatient = QDoubleSpinBox(self.scrollAreaWidgetPatient)
        self.bmiPatient.setObjectName(u"bmiPatient")
        sizePolicy1.setHeightForWidth(self.bmiPatient.sizePolicy().hasHeightForWidth())
        self.bmiPatient.setSizePolicy(sizePolicy1)
        self.bmiPatient.setAutoFillBackground(True)
        self.bmiPatient.setMinimum(15.000000000000000)
        self.bmiPatient.setMaximum(30.000000000000000)

        self.gridLayout_8.addWidget(self.bmiPatient, 9, 4, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetPatient)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_22, 12, 2, 1, 1)

        self.dietPatient = QDoubleSpinBox(self.scrollAreaWidgetPatient)
        self.dietPatient.setObjectName(u"dietPatient")
        sizePolicy1.setHeightForWidth(self.dietPatient.sizePolicy().hasHeightForWidth())
        self.dietPatient.setSizePolicy(sizePolicy1)
        self.dietPatient.setAutoFillBackground(True)
        self.dietPatient.setMinimum(0.010000000000000)
        self.dietPatient.setMaximum(10.000000000000000)

        self.gridLayout_8.addWidget(self.dietPatient, 13, 4, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetPatient)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.label_23, 13, 2, 1, 1)

        self.agePatient = QSpinBox(self.scrollAreaWidgetPatient)
        self.agePatient.setObjectName(u"agePatient")
        sizePolicy1.setHeightForWidth(self.agePatient.sizePolicy().hasHeightForWidth())
        self.agePatient.setSizePolicy(sizePolicy1)
        self.agePatient.setAutoFillBackground(True)
        self.agePatient.setMinimum(60)
        self.agePatient.setMaximum(90)

        self.gridLayout_8.addWidget(self.agePatient, 4, 4, 1, 1)

        self.scrollAreaPatient.setWidget(self.scrollAreaWidgetPatient)

        self.verticalLayout_4.addWidget(self.scrollAreaPatient)

        self.widgetSubPatient = QWidget(self.widgetPatient)
        self.widgetSubPatient.setObjectName(u"widgetSubPatient")
        self.horizontalLayout_3 = QHBoxLayout(self.widgetSubPatient)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2Patient = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2Patient)

        self.submitButtonPatient = QPushButton(self.widgetSubPatient)
        self.submitButtonPatient.setObjectName(u"submitButtonPatient")
        self.submitButtonPatient.setMaximumSize(QSize(300, 16777215))
        self.submitButtonPatient.setStyleSheet(u"background-color: rgb(85,255,0);")

        self.horizontalLayout_3.addWidget(self.submitButtonPatient)

        self.horizontalSpacerPatient = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacerPatient)


        self.verticalLayout_4.addWidget(self.widgetSubPatient)


        self.verticalLayoutMain.addWidget(self.widgetPatient)

        self.widgetClinical = QWidget(self.centralwidget)
        self.widgetClinical.setObjectName(u"widgetClinical")
        self.widgetClinical.setEnabled(False)
        self.widgetClinical.setStyleSheet(u"#widgetClinical {\n"
"	background-color: rgb(176, 125, 180);\\n\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widgetClinical)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4Clinical = QLabel(self.widgetClinical)
        self.label_4Clinical.setObjectName(u"label_4Clinical")
        sizePolicy.setHeightForWidth(self.label_4Clinical.sizePolicy().hasHeightForWidth())
        self.label_4Clinical.setSizePolicy(sizePolicy)
        self.label_4Clinical.setFont(font1)
        self.label_4Clinical.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4Clinical)

        self.scrollAreaClinical = QScrollArea(self.widgetClinical)
        self.scrollAreaClinical.setObjectName(u"scrollAreaClinical")
        self.scrollAreaClinical.setStyleSheet(u"")
        self.scrollAreaClinical.setWidgetResizable(True)
        self.scrollAreaWidgetClinical = QWidget()
        self.scrollAreaWidgetClinical.setObjectName(u"scrollAreaWidgetClinical")
        self.scrollAreaWidgetClinical.setGeometry(QRect(0, 0, 1251, 684))
        self.scrollAreaWidgetClinical.setStyleSheet(u"#scrollAreaWidgetClinical {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetClinical)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_8Clinical.setObjectName(u"label_8Clinical")
        sizePolicy2.setHeightForWidth(self.label_8Clinical.sizePolicy().hasHeightForWidth())
        self.label_8Clinical.setSizePolicy(sizePolicy2)
        self.label_8Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_8Clinical, 4, 1, 1, 1)

        self.headInjuryClinical = QCheckBox(self.scrollAreaWidgetClinical)
        self.headInjuryClinical.setObjectName(u"headInjuryClinical")
        self.headInjuryClinical.setAutoFillBackground(False)

        self.gridLayout_7.addWidget(self.headInjuryClinical, 4, 3, 1, 1)

        self.diabetesClinical = QCheckBox(self.scrollAreaWidgetClinical)
        self.diabetesClinical.setObjectName(u"diabetesClinical")
        self.diabetesClinical.setAutoFillBackground(False)

        self.gridLayout_7.addWidget(self.diabetesClinical, 2, 3, 1, 1)

        self.label_13Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_13Clinical.setObjectName(u"label_13Clinical")
        sizePolicy2.setHeightForWidth(self.label_13Clinical.sizePolicy().hasHeightForWidth())
        self.label_13Clinical.setSizePolicy(sizePolicy2)
        self.label_13Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_13Clinical, 9, 1, 1, 1)

        self.label_9Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_9Clinical.setObjectName(u"label_9Clinical")
        sizePolicy2.setHeightForWidth(self.label_9Clinical.sizePolicy().hasHeightForWidth())
        self.label_9Clinical.setSizePolicy(sizePolicy2)
        self.label_9Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_9Clinical, 5, 1, 1, 1)

        self.horizontalSpacer_4Clinical = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4Clinical, 4, 4, 1, 1)

        self.depressionClinical = QCheckBox(self.scrollAreaWidgetClinical)
        self.depressionClinical.setObjectName(u"depressionClinical")
        self.depressionClinical.setAutoFillBackground(False)

        self.gridLayout_7.addWidget(self.depressionClinical, 3, 3, 1, 1)

        self.cholTriClinical = QDoubleSpinBox(self.scrollAreaWidgetClinical)
        self.cholTriClinical.setObjectName(u"cholTriClinical")
        sizePolicy1.setHeightForWidth(self.cholTriClinical.sizePolicy().hasHeightForWidth())
        self.cholTriClinical.setSizePolicy(sizePolicy1)
        self.cholTriClinical.setAutoFillBackground(True)
        self.cholTriClinical.setMinimum(50.399999999999999)
        self.cholTriClinical.setMaximum(400.000000000000000)

        self.gridLayout_7.addWidget(self.cholTriClinical, 11, 3, 1, 1)

        self.label_16Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_16Clinical.setObjectName(u"label_16Clinical")
        sizePolicy2.setHeightForWidth(self.label_16Clinical.sizePolicy().hasHeightForWidth())
        self.label_16Clinical.setSizePolicy(sizePolicy2)
        self.label_16Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_16Clinical, 11, 1, 1, 1)

        self.label_12Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_12Clinical.setObjectName(u"label_12Clinical")
        sizePolicy2.setHeightForWidth(self.label_12Clinical.sizePolicy().hasHeightForWidth())
        self.label_12Clinical.setSizePolicy(sizePolicy2)
        self.label_12Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_12Clinical, 8, 1, 1, 1)

        self.label_5Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_5Clinical.setObjectName(u"label_5Clinical")
        sizePolicy2.setHeightForWidth(self.label_5Clinical.sizePolicy().hasHeightForWidth())
        self.label_5Clinical.setSizePolicy(sizePolicy2)
        self.label_5Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_5Clinical, 1, 1, 1, 1)

        self.label_15Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_15Clinical.setObjectName(u"label_15Clinical")
        sizePolicy2.setHeightForWidth(self.label_15Clinical.sizePolicy().hasHeightForWidth())
        self.label_15Clinical.setSizePolicy(sizePolicy2)
        self.label_15Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_15Clinical, 10, 1, 1, 1)

        self.label_10Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_10Clinical.setObjectName(u"label_10Clinical")
        sizePolicy2.setHeightForWidth(self.label_10Clinical.sizePolicy().hasHeightForWidth())
        self.label_10Clinical.setSizePolicy(sizePolicy2)
        self.label_10Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_10Clinical, 6, 1, 1, 1)

        self.famAlzClinical = QCheckBox(self.scrollAreaWidgetClinical)
        self.famAlzClinical.setObjectName(u"famAlzClinical")
        self.famAlzClinical.setAutoFillBackground(False)

        self.gridLayout_7.addWidget(self.famAlzClinical, 0, 3, 1, 1)

        self.label_3Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_3Clinical.setObjectName(u"label_3Clinical")
        sizePolicy2.setHeightForWidth(self.label_3Clinical.sizePolicy().hasHeightForWidth())
        self.label_3Clinical.setSizePolicy(sizePolicy2)
        self.label_3Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_3Clinical, 0, 1, 1, 1)

        self.cholHDLClinical = QDoubleSpinBox(self.scrollAreaWidgetClinical)
        self.cholHDLClinical.setObjectName(u"cholHDLClinical")
        sizePolicy1.setHeightForWidth(self.cholHDLClinical.sizePolicy().hasHeightForWidth())
        self.cholHDLClinical.setSizePolicy(sizePolicy1)
        self.cholHDLClinical.setAutoFillBackground(True)
        self.cholHDLClinical.setMinimum(20.000000000000000)
        self.cholHDLClinical.setMaximum(100.000000000000000)

        self.gridLayout_7.addWidget(self.cholHDLClinical, 10, 3, 1, 1)

        self.label_7Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_7Clinical.setObjectName(u"label_7Clinical")
        sizePolicy2.setHeightForWidth(self.label_7Clinical.sizePolicy().hasHeightForWidth())
        self.label_7Clinical.setSizePolicy(sizePolicy2)
        self.label_7Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_7Clinical, 3, 1, 1, 1)

        self.hypertensionClinical = QCheckBox(self.scrollAreaWidgetClinical)
        self.hypertensionClinical.setObjectName(u"hypertensionClinical")
        self.hypertensionClinical.setAutoFillBackground(False)

        self.gridLayout_7.addWidget(self.hypertensionClinical, 5, 3, 1, 1)

        self.cholTotalClinical = QDoubleSpinBox(self.scrollAreaWidgetClinical)
        self.cholTotalClinical.setObjectName(u"cholTotalClinical")
        sizePolicy1.setHeightForWidth(self.cholTotalClinical.sizePolicy().hasHeightForWidth())
        self.cholTotalClinical.setSizePolicy(sizePolicy1)
        self.cholTotalClinical.setAutoFillBackground(True)
        self.cholTotalClinical.setMinimum(150.000000000000000)
        self.cholTotalClinical.setMaximum(300.000000000000000)

        self.gridLayout_7.addWidget(self.cholTotalClinical, 8, 3, 1, 1)

        self.cholLDLClinical = QDoubleSpinBox(self.scrollAreaWidgetClinical)
        self.cholLDLClinical.setObjectName(u"cholLDLClinical")
        sizePolicy1.setHeightForWidth(self.cholLDLClinical.sizePolicy().hasHeightForWidth())
        self.cholLDLClinical.setSizePolicy(sizePolicy1)
        self.cholLDLClinical.setAutoFillBackground(True)
        self.cholLDLClinical.setMinimum(50.200000000000003)
        self.cholLDLClinical.setMaximum(200.000000000000000)

        self.gridLayout_7.addWidget(self.cholLDLClinical, 9, 3, 1, 1)

        self.label_11Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_11Clinical.setObjectName(u"label_11Clinical")
        sizePolicy2.setHeightForWidth(self.label_11Clinical.sizePolicy().hasHeightForWidth())
        self.label_11Clinical.setSizePolicy(sizePolicy2)
        self.label_11Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_11Clinical, 7, 1, 1, 1)

        self.sysBPClinical = QDoubleSpinBox(self.scrollAreaWidgetClinical)
        self.sysBPClinical.setObjectName(u"sysBPClinical")
        sizePolicy1.setHeightForWidth(self.sysBPClinical.sizePolicy().hasHeightForWidth())
        self.sysBPClinical.setSizePolicy(sizePolicy1)
        self.sysBPClinical.setAutoFillBackground(True)
        self.sysBPClinical.setMinimum(90.000000000000000)
        self.sysBPClinical.setMaximum(179.000000000000000)

        self.gridLayout_7.addWidget(self.sysBPClinical, 6, 3, 1, 1)

        self.label_6Clinical = QLabel(self.scrollAreaWidgetClinical)
        self.label_6Clinical.setObjectName(u"label_6Clinical")
        sizePolicy2.setHeightForWidth(self.label_6Clinical.sizePolicy().hasHeightForWidth())
        self.label_6Clinical.setSizePolicy(sizePolicy2)
        self.label_6Clinical.setMinimumSize(QSize(0, 50))

        self.gridLayout_7.addWidget(self.label_6Clinical, 2, 1, 1, 1)

        self.dasBPClinical = QDoubleSpinBox(self.scrollAreaWidgetClinical)
        self.dasBPClinical.setObjectName(u"dasBPClinical")
        sizePolicy1.setHeightForWidth(self.dasBPClinical.sizePolicy().hasHeightForWidth())
        self.dasBPClinical.setSizePolicy(sizePolicy1)
        self.dasBPClinical.setAutoFillBackground(True)
        self.dasBPClinical.setMinimum(60.000000000000000)
        self.dasBPClinical.setMaximum(119.000000000000000)

        self.gridLayout_7.addWidget(self.dasBPClinical, 7, 3, 1, 1)

        self.horizontalSpacer_3Clinical = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3Clinical, 4, 0, 1, 1)

        self.cardiovascularDiseaseClinical = QCheckBox(self.scrollAreaWidgetClinical)
        self.cardiovascularDiseaseClinical.setObjectName(u"cardiovascularDiseaseClinical")
        self.cardiovascularDiseaseClinical.setAutoFillBackground(False)

        self.gridLayout_7.addWidget(self.cardiovascularDiseaseClinical, 1, 3, 1, 1)

        self.horizontalSpacer_5Clinical = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5Clinical, 4, 2, 1, 1)

        self.scrollAreaClinical.setWidget(self.scrollAreaWidgetClinical)

        self.verticalLayout_3.addWidget(self.scrollAreaClinical)

        self.widgetsubClinical = QWidget(self.widgetClinical)
        self.widgetsubClinical.setObjectName(u"widgetsubClinical")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetsubClinical)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2Clinical = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2Clinical)

        self.submitButtonClinical = QPushButton(self.widgetsubClinical)
        self.submitButtonClinical.setObjectName(u"submitButtonClinical")
        self.submitButtonClinical.setMaximumSize(QSize(300, 16777215))
        self.submitButtonClinical.setStyleSheet(u"background-color: rgb(85,255,0);")

        self.horizontalLayout_2.addWidget(self.submitButtonClinical)

        self.horizontalSpacerClinical = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacerClinical)


        self.verticalLayout_3.addWidget(self.widgetsubClinical)


        self.verticalLayoutMain.addWidget(self.widgetClinical)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1283, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ADPS", None))
        self.label.setText("")
        self.labelPatientID.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButtonBack.setText(QCoreApplication.translate("MainWindow", u"Back to Login", None))
        self.loginPatientID.setInputMask("")
        self.loginPatientID.setText("")
        self.loginPatientID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Patient ID", None))
        self.loginSubmit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.loginTitle.setText(QCoreApplication.translate("MainWindow", u"Login With Patient ID", None))
        self.GeneticLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Cognitive Results</span></p></body></html>", None))
        self.cognitive_button.setText(QCoreApplication.translate("MainWindow", u"Go To", None))
        self.cognitive_status.setText(QCoreApplication.translate("MainWindow", u"Incomplete", None))
        self.genetic_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Clinical Results</span></p></body></html>", None))
        self.genetic_status.setText(QCoreApplication.translate("MainWindow", u"Incomplete", None))
        self.genetic_button.setText(QCoreApplication.translate("MainWindow", u"Go To", None))
        self.GeneticLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Patient Survey</span></p></body></html>", None))
        self.patient_status.setText(QCoreApplication.translate("MainWindow", u"Incomplete", None))
        self.patient_button.setText(QCoreApplication.translate("MainWindow", u"Go To", None))
        self.results_button.setText(QCoreApplication.translate("MainWindow", u"Compute Resuls", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cognitive Results", None))
        self.behavioralProblems.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Disorientation</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Functional Assessment</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Personality Changes</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">ADL</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Forgetfulness</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Difficulty Completing Tasks</span></p></body></html>", None))
        self.disorientation.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Behavioral Problems</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Memory Complaints</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Confusion</span></p></body></html>", None))
        self.memoryComplaints.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.diffCompTask.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.personalityChanges.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.forgetfulness.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.confusion.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">MMSE</span></p></body></html>", None))
        self.submitButtonCognitive.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_results.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_diagnosis.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelMMSE.setText("")
        self.labelADL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelFA.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4Patient.setText(QCoreApplication.translate("MainWindow", u"Patient Survey", None))
        self.educationPatient.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.educationPatient.setItemText(1, QCoreApplication.translate("MainWindow", u"High School", None))
        self.educationPatient.setItemText(2, QCoreApplication.translate("MainWindow", u"Bachelors", None))
        self.educationPatient.setItemText(3, QCoreApplication.translate("MainWindow", u"Higher", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Ethnicity</span></p></body></html>", None))
        self.smokingPatient.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Smoking</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Age</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Alcohol Consumption</span></p></body></html>", None))
        self.genderBoxPatient.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.femalePatient.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.malePatient.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Gender</span></p></body></html>", None))
        self.ethnicityPatient.setItemText(0, QCoreApplication.translate("MainWindow", u"Caucasian", None))
        self.ethnicityPatient.setItemText(1, QCoreApplication.translate("MainWindow", u"African American", None))
        self.ethnicityPatient.setItemText(2, QCoreApplication.translate("MainWindow", u"Asian", None))
        self.ethnicityPatient.setItemText(3, QCoreApplication.translate("MainWindow", u"Other", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Education Level</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">BMI</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Sleep Quality</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Physical Activity</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Diet Quality</span></p></body></html>", None))
        self.submitButtonPatient.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_4Clinical.setText(QCoreApplication.translate("MainWindow", u"Clinical Results", None))
        self.label_8Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Head Injury</span></p></body></html>", None))
        self.headInjuryClinical.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.diabetesClinical.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.label_13Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Cholesterol LDL</span></p></body></html>", None))
        self.label_9Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Hypertension</span></p></body></html>", None))
        self.depressionClinical.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.label_16Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Cholesterol Triglycerides</span></p></body></html>", None))
        self.label_12Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Cholesterol Total</span></p></body></html>", None))
        self.label_5Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Cardiovascular Disease</span></p></body></html>", None))
        self.label_15Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Cholesterol HDL</span></p></body></html>", None))
        self.label_10Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Systolic BP</span></p></body></html>", None))
        self.famAlzClinical.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.label_3Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Family History of Alzheimer's</span></p></body></html>", None))
        self.label_7Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Depression</span></p></body></html>", None))
        self.hypertensionClinical.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.label_11Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Diastolic BP</span></p></body></html>", None))
        self.label_6Clinical.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Diabetes</span></p></body></html>", None))
        self.cardiovascularDiseaseClinical.setText(QCoreApplication.translate("MainWindow", u"Yes / No", None))
        self.submitButtonClinical.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

