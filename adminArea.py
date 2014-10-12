# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminArea.ui'
#
# Created: Sun Oct 12 00:02:24 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_adminWindow(object):
    def setupUi(self, adminWindow):
        adminWindow.setObjectName(_fromUtf8("adminWindow"))
        adminWindow.setEnabled(True)
        adminWindow.resize(745, 514)
        adminWindow.setMinimumSize(QtCore.QSize(329, 218))
        adminWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/images/48x48/registron.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        adminWindow.setWindowIcon(icon)
        adminWindow.setWindowOpacity(1.0)
        adminWindow.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        self.centralwidget = QtGui.QWidget(adminWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 721, 451))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8("color:white;background: rgb(10, 80, 111);"))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.indexTab = QtGui.QWidget()
        self.indexTab.setObjectName(_fromUtf8("indexTab"))
        self.schoolNameLabel = QtGui.QLabel(self.indexTab)
        self.schoolNameLabel.setGeometry(QtCore.QRect(20, 15, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.schoolNameLabel.setFont(font)
        self.schoolNameLabel.setObjectName(_fromUtf8("schoolNameLabel"))
        self.addStudentLabel = QtGui.QLabel(self.indexTab)
        self.addStudentLabel.setGeometry(QtCore.QRect(20, 130, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addStudentLabel.setFont(font)
        self.addStudentLabel.setObjectName(_fromUtf8("addStudentLabel"))
        self.surnameLabel = QtGui.QLabel(self.indexTab)
        self.surnameLabel.setGeometry(QtCore.QRect(20, 160, 81, 16))
        self.surnameLabel.setObjectName(_fromUtf8("surnameLabel"))
        self.othernamesLabel = QtGui.QLabel(self.indexTab)
        self.othernamesLabel.setGeometry(QtCore.QRect(370, 160, 101, 16))
        self.othernamesLabel.setObjectName(_fromUtf8("othernamesLabel"))
        self.studentsDeptLabel = QtGui.QLabel(self.indexTab)
        self.studentsDeptLabel.setGeometry(QtCore.QRect(20, 230, 171, 16))
        self.studentsDeptLabel.setObjectName(_fromUtf8("studentsDeptLabel"))
        self.imageDropLabel = QtGui.QLabel(self.indexTab)
        self.imageDropLabel.setGeometry(QtCore.QRect(20, 300, 641, 16))
        self.imageDropLabel.setObjectName(_fromUtf8("imageDropLabel"))
        self.schoolNameBtn = QtGui.QPushButton(self.indexTab)
        self.schoolNameBtn.setGeometry(QtCore.QRect(560, 80, 141, 31))
        self.schoolNameBtn.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        self.schoolNameBtn.setObjectName(_fromUtf8("schoolNameBtn"))
        self.addStudentBtn = QtGui.QPushButton(self.indexTab)
        self.addStudentBtn.setGeometry(QtCore.QRect(560, 380, 141, 31))
        self.addStudentBtn.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        self.addStudentBtn.setObjectName(_fromUtf8("addStudentBtn"))
        self.schoolSaved = QtGui.QLabel(self.indexTab)
        self.schoolSaved.setGeometry(QtCore.QRect(20, 80, 131, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.schoolSaved.setFont(font)
        self.schoolSaved.setObjectName(_fromUtf8("schoolSaved"))
        self.studentImage = QtGui.QLineEdit(self.indexTab)
        self.studentImage.setGeometry(QtCore.QRect(20, 330, 681, 31))
        self.studentImage.setStyleSheet(_fromUtf8("background:white;color:black;"))
        self.studentImage.setObjectName(_fromUtf8("studentImage"))
        self.surname = QtGui.QLineEdit(self.indexTab)
        self.surname.setGeometry(QtCore.QRect(20, 180, 331, 31))
        self.surname.setStyleSheet(_fromUtf8("background:white;color:black;"))
        self.surname.setObjectName(_fromUtf8("surname"))
        self.othernames = QtGui.QLineEdit(self.indexTab)
        self.othernames.setGeometry(QtCore.QRect(370, 180, 331, 31))
        self.othernames.setStyleSheet(_fromUtf8("background:white;color:black;"))
        self.othernames.setObjectName(_fromUtf8("othernames"))
        self.schoolName = QtGui.QLineEdit(self.indexTab)
        self.schoolName.setGeometry(QtCore.QRect(20, 40, 681, 31))
        self.schoolName.setStyleSheet(_fromUtf8("background:white;color:black;"))
        self.schoolName.setObjectName(_fromUtf8("schoolName"))
        self.studentSaved = QtGui.QLabel(self.indexTab)
        self.studentSaved.setGeometry(QtCore.QRect(20, 380, 231, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.studentSaved.setFont(font)
        self.studentSaved.setObjectName(_fromUtf8("studentSaved"))
        self.campusID = QtGui.QLineEdit(self.indexTab)
        self.campusID.setGeometry(QtCore.QRect(370, 250, 331, 31))
        self.campusID.setStyleSheet(_fromUtf8("background:white;color:black;"))
        self.campusID.setObjectName(_fromUtf8("campusID"))
        self.campusIDLabel = QtGui.QLabel(self.indexTab)
        self.campusIDLabel.setGeometry(QtCore.QRect(370, 230, 101, 16))
        self.campusIDLabel.setObjectName(_fromUtf8("campusIDLabel"))
        self.studentDept = QtGui.QComboBox(self.indexTab)
        self.studentDept.setGeometry(QtCore.QRect(20, 250, 331, 31))
        self.studentDept.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111); color:white;"))
        self.studentDept.setObjectName(_fromUtf8("studentDept"))
        self.tabWidget.addTab(self.indexTab, _fromUtf8(""))
        self.studentsTab = QtGui.QWidget()
        self.studentsTab.setObjectName(_fromUtf8("studentsTab"))
        self.studlistLabel = QtGui.QLabel(self.studentsTab)
        self.studlistLabel.setGeometry(QtCore.QRect(10, 20, 251, 16))
        self.studlistLabel.setObjectName(_fromUtf8("studlistLabel"))
        self.studentsLIst = QtGui.QScrollArea(self.studentsTab)
        self.studentsLIst.setGeometry(QtCore.QRect(10, 40, 201, 361))
        self.studentsLIst.setWidgetResizable(True)
        self.studentsLIst.setObjectName(_fromUtf8("studentsLIst"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 197, 357))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.studentsLIst.setWidget(self.scrollAreaWidgetContents)
        self.studnameLabel = QtGui.QLabel(self.studentsTab)
        self.studnameLabel.setGeometry(QtCore.QRect(240, 40, 121, 16))
        self.studnameLabel.setObjectName(_fromUtf8("studnameLabel"))
        self.studDeptLabel = QtGui.QLabel(self.studentsTab)
        self.studDeptLabel.setGeometry(QtCore.QRect(240, 180, 121, 16))
        self.studDeptLabel.setObjectName(_fromUtf8("studDeptLabel"))
        self.studImageLabel = QtGui.QLabel(self.studentsTab)
        self.studImageLabel.setGeometry(QtCore.QRect(240, 250, 121, 16))
        self.studImageLabel.setObjectName(_fromUtf8("studImageLabel"))
        self.updateStudentBtn = QtGui.QPushButton(self.studentsTab)
        self.updateStudentBtn.setGeometry(QtCore.QRect(560, 320, 131, 31))
        self.updateStudentBtn.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111); color: white;"))
        self.updateStudentBtn.setObjectName(_fromUtf8("updateStudentBtn"))
        self.studidLabel = QtGui.QLabel(self.studentsTab)
        self.studidLabel.setGeometry(QtCore.QRect(240, 110, 121, 16))
        self.studidLabel.setObjectName(_fromUtf8("studidLabel"))
        self.ed_studentName = QtGui.QLineEdit(self.studentsTab)
        self.ed_studentName.setGeometry(QtCore.QRect(240, 60, 451, 31))
        self.ed_studentName.setStyleSheet(_fromUtf8("color:black;background:white;"))
        self.ed_studentName.setObjectName(_fromUtf8("ed_studentName"))
        self.ed_studentID = QtGui.QLineEdit(self.studentsTab)
        self.ed_studentID.setGeometry(QtCore.QRect(240, 130, 451, 31))
        self.ed_studentID.setStyleSheet(_fromUtf8("color:black;background:white;"))
        self.ed_studentID.setObjectName(_fromUtf8("ed_studentID"))
        self.ed_department = QtGui.QLineEdit(self.studentsTab)
        self.ed_department.setGeometry(QtCore.QRect(240, 200, 451, 31))
        self.ed_department.setStyleSheet(_fromUtf8("color:black;background:white;"))
        self.ed_department.setObjectName(_fromUtf8("ed_department"))
        self.ed_image = QtGui.QLineEdit(self.studentsTab)
        self.ed_image.setGeometry(QtCore.QRect(240, 270, 451, 31))
        self.ed_image.setStyleSheet(_fromUtf8("color:black;background:white;"))
        self.ed_image.setObjectName(_fromUtf8("ed_image"))
        self.tabWidget.addTab(self.studentsTab, _fromUtf8(""))
        self.coursesTab = QtGui.QWidget()
        self.coursesTab.setObjectName(_fromUtf8("coursesTab"))
        self.label = QtGui.QLabel(self.coursesTab)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.addDept = QtGui.QLineEdit(self.coursesTab)
        self.addDept.setGeometry(QtCore.QRect(10, 40, 551, 31))
        self.addDept.setStyleSheet(_fromUtf8("background:white; color: black;"))
        self.addDept.setInputMask(_fromUtf8(""))
        self.addDept.setPlaceholderText(_fromUtf8(""))
        self.addDept.setObjectName(_fromUtf8("addDept"))
        self.addDeptBtn = QtGui.QPushButton(self.coursesTab)
        self.addDeptBtn.setGeometry(QtCore.QRect(570, 40, 131, 31))
        self.addDeptBtn.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        self.addDeptBtn.setObjectName(_fromUtf8("addDeptBtn"))
        self.label_2 = QtGui.QLabel(self.coursesTab)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 331, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea = QtGui.QScrollArea(self.coursesTab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 210, 221, 201))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 217, 197))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.label_3 = QtGui.QLabel(self.coursesTab)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.addCourse = QtGui.QLineEdit(self.coursesTab)
        self.addCourse.setGeometry(QtCore.QRect(10, 120, 271, 31))
        self.addCourse.setStyleSheet(_fromUtf8("background:white; color: black;"))
        self.addCourse.setInputMask(_fromUtf8(""))
        self.addCourse.setPlaceholderText(_fromUtf8(""))
        self.addCourse.setObjectName(_fromUtf8("addCourse"))
        self.addCourseBtn = QtGui.QPushButton(self.coursesTab)
        self.addCourseBtn.setGeometry(QtCore.QRect(570, 120, 131, 31))
        self.addCourseBtn.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        self.addCourseBtn.setObjectName(_fromUtf8("addCourseBtn"))
        self.label_4 = QtGui.QLabel(self.coursesTab)
        self.label_4.setGeometry(QtCore.QRect(300, 90, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.scrollArea_2 = QtGui.QScrollArea(self.coursesTab)
        self.scrollArea_2.setGeometry(QtCore.QRect(360, 210, 231, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 227, 197))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_5 = QtGui.QPushButton(self.coursesTab)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 240, 111, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.coursesTab)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 300, 111, 41))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.coursesTab)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 240, 111, 41))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.coursesTab)
        self.pushButton_8.setGeometry(QtCore.QRect(600, 300, 111, 41))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.addDeptNotice = QtGui.QLabel(self.coursesTab)
        self.addDeptNotice.setGeometry(QtCore.QRect(300, 20, 261, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.addDeptNotice.setFont(font)
        self.addDeptNotice.setText(_fromUtf8(""))
        self.addDeptNotice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.addDeptNotice.setObjectName(_fromUtf8("addDeptNotice"))
        self.courseAddDeptList = QtGui.QComboBox(self.coursesTab)
        self.courseAddDeptList.setGeometry(QtCore.QRect(300, 120, 261, 31))
        self.courseAddDeptList.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);color: white;"))
        self.courseAddDeptList.setObjectName(_fromUtf8("courseAddDeptList"))
        self.warningDpt = QtGui.QLabel(self.coursesTab)
        self.warningDpt.setGeometry(QtCore.QRect(10, 160, 551, 16))
        self.warningDpt.setObjectName(_fromUtf8("warningDpt"))
        self.courseAdded = QtGui.QLabel(self.coursesTab)
        self.courseAdded.setGeometry(QtCore.QRect(470, 90, 101, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.courseAdded.setFont(font)
        self.courseAdded.setObjectName(_fromUtf8("courseAdded"))
        self.tabWidget.addTab(self.coursesTab, _fromUtf8(""))
        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.label_11 = QtGui.QLabel(self.settingsTab)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.changePassBtn = QtGui.QPushButton(self.settingsTab)
        self.changePassBtn.setGeometry(QtCore.QRect(550, 80, 141, 31))
        self.changePassBtn.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);color:white;"))
        self.changePassBtn.setObjectName(_fromUtf8("changePassBtn"))
        self.passwordChanged = QtGui.QLabel(self.settingsTab)
        self.passwordChanged.setGeometry(QtCore.QRect(10, 80, 381, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.passwordChanged.setFont(font)
        self.passwordChanged.setText(_fromUtf8(""))
        self.passwordChanged.setObjectName(_fromUtf8("passwordChanged"))
        self.passwordChange = QtGui.QLineEdit(self.settingsTab)
        self.passwordChange.setGeometry(QtCore.QRect(10, 40, 681, 31))
        self.passwordChange.setStyleSheet(_fromUtf8("background:white; color: black;"))
        self.passwordChange.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordChange.setObjectName(_fromUtf8("passwordChange"))
        self.tabWidget.addTab(self.settingsTab, _fromUtf8(""))
        adminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(adminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
        self.menubar.setStyleSheet(_fromUtf8("color: white;"))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setStyleSheet(_fromUtf8(""))
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuAdministrators = QtGui.QMenu(self.menubar)
        self.menuAdministrators.setObjectName(_fromUtf8("menuAdministrators"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        adminWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(adminWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        adminWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(adminWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionDocumentation = QtGui.QAction(adminWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionAbout = QtGui.QAction(adminWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionCredits = QtGui.QAction(adminWindow)
        self.actionCredits.setObjectName(_fromUtf8("actionCredits"))
        self.actionSignIn = QtGui.QAction(adminWindow)
        self.actionSignIn.setObjectName(_fromUtf8("actionSignIn"))
        self.actionLicense = QtGui.QAction(adminWindow)
        self.actionLicense.setObjectName(_fromUtf8("actionLicense"))
        self.actionAdmin_Logout = QtGui.QAction(adminWindow)
        self.actionAdmin_Logout.setObjectName(_fromUtf8("actionAdmin_Logout"))
        self.menuMenu.addAction(self.actionQuit)
        self.menuMenu.addSeparator()
        self.menuAdministrators.addAction(self.actionAdmin_Logout)
        self.menuAdministrators.addSeparator()
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCredits)
        self.menuHelp.addAction(self.actionLicense)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAdministrators.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(adminWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(adminWindow)

    def retranslateUi(self, adminWindow):
        adminWindow.setWindowTitle(QtGui.QApplication.translate("adminWindow", "Registron Administrator", None, QtGui.QApplication.UnicodeUTF8))
        self.schoolNameLabel.setText(QtGui.QApplication.translate("adminWindow", "School Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.addStudentLabel.setText(QtGui.QApplication.translate("adminWindow", "Add Student:", None, QtGui.QApplication.UnicodeUTF8))
        self.surnameLabel.setText(QtGui.QApplication.translate("adminWindow", "Surname:", None, QtGui.QApplication.UnicodeUTF8))
        self.othernamesLabel.setText(QtGui.QApplication.translate("adminWindow", "Other names:", None, QtGui.QApplication.UnicodeUTF8))
        self.studentsDeptLabel.setText(QtGui.QApplication.translate("adminWindow", "Student\'s Department:", None, QtGui.QApplication.UnicodeUTF8))
        self.imageDropLabel.setText(QtGui.QApplication.translate("adminWindow", "Image (drop a 128x128 image in the folder resources/images/128x128 and put the file name here):", None, QtGui.QApplication.UnicodeUTF8))
        self.schoolNameBtn.setText(QtGui.QApplication.translate("adminWindow", "Save School Name", None, QtGui.QApplication.UnicodeUTF8))
        self.addStudentBtn.setText(QtGui.QApplication.translate("adminWindow", "Add Student", None, QtGui.QApplication.UnicodeUTF8))
        self.schoolSaved.setText(QtGui.QApplication.translate("adminWindow", "School Saved", None, QtGui.QApplication.UnicodeUTF8))
        self.studentSaved.setText(QtGui.QApplication.translate("adminWindow", "Student Added", None, QtGui.QApplication.UnicodeUTF8))
        self.campusIDLabel.setText(QtGui.QApplication.translate("adminWindow", "Campus ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.indexTab), QtGui.QApplication.translate("adminWindow", "School and Students", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.indexTab), QtGui.QApplication.translate("adminWindow", "Adjust settings of school and settings", None, QtGui.QApplication.UnicodeUTF8))
        self.studlistLabel.setText(QtGui.QApplication.translate("adminWindow", "Click on student ID to edit profile", None, QtGui.QApplication.UnicodeUTF8))
        self.studnameLabel.setText(QtGui.QApplication.translate("adminWindow", "Student Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.studDeptLabel.setText(QtGui.QApplication.translate("adminWindow", "Department:", None, QtGui.QApplication.UnicodeUTF8))
        self.studImageLabel.setText(QtGui.QApplication.translate("adminWindow", "Image file name:", None, QtGui.QApplication.UnicodeUTF8))
        self.updateStudentBtn.setText(QtGui.QApplication.translate("adminWindow", "Update Record", None, QtGui.QApplication.UnicodeUTF8))
        self.studidLabel.setText(QtGui.QApplication.translate("adminWindow", "Campus ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.studentsTab), QtGui.QApplication.translate("adminWindow", "Manage Students", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("adminWindow", "Add Department:", None, QtGui.QApplication.UnicodeUTF8))
        self.addDeptBtn.setText(QtGui.QApplication.translate("adminWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("adminWindow", "Select Department to Edit Courses in it:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("adminWindow", "New Course:", None, QtGui.QApplication.UnicodeUTF8))
        self.addCourseBtn.setText(QtGui.QApplication.translate("adminWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("adminWindow", "Department:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("adminWindow", "Delete \n"
"Department", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("adminWindow", "Edit \n"
"Department", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("adminWindow", "Delete \n"
"Course", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("adminWindow", "Edit \n"
"Course", None, QtGui.QApplication.UnicodeUTF8))
        self.warningDpt.setText(QtGui.QApplication.translate("adminWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Courses cannot be created for departments just added till program is restarted.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.courseAdded.setText(QtGui.QApplication.translate("adminWindow", "Course added", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.coursesTab), QtGui.QApplication.translate("adminWindow", "Manage Courses", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.coursesTab), QtGui.QApplication.translate("adminWindow", "Add and Edit School Courses", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("adminWindow", "Change Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.changePassBtn.setText(QtGui.QApplication.translate("adminWindow", "Update Password", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QtGui.QApplication.translate("adminWindow", "Setttings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("adminWindow", "Application", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministrators.setTitle(QtGui.QApplication.translate("adminWindow", "Administrator", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("adminWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("adminWindow", "Quit registron", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip(QtGui.QApplication.translate("adminWindow", "Exit this program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("adminWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setText(QtGui.QApplication.translate("adminWindow", "Online Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setShortcut(QtGui.QApplication.translate("adminWindow", "Ctrl+?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("adminWindow", "About Registron", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("adminWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setText(QtGui.QApplication.translate("adminWindow", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setShortcut(QtGui.QApplication.translate("adminWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignIn.setText(QtGui.QApplication.translate("adminWindow", "Manage Accounts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLicense.setText(QtGui.QApplication.translate("adminWindow", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdmin_Logout.setText(QtGui.QApplication.translate("adminWindow", "Admin Logout", None, QtGui.QApplication.UnicodeUTF8))

import app_rc
