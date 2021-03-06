# -*- coding: utf-8 -*-

import webbrowser

from PySide import QtCore
from PySide import QtGui


from core.TestPython import TestPython
from gui.Preferences import Ui_Preferences
from gui.InfoPanel import InfoPanel
from gui.Raw_Data import Raw_Data
from core.SqlMap import SqlMap
from gui.tabData import tabData


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 654)
        self.Frame = QtGui.QFrame()
        self.Layout = QtGui.QHBoxLayout()
        self.gbxInfo = QtGui.QGroupBox()
        self.gbxInfo.setTitle('Information')
        self.Info = InfoPanel()
        self.InfoLayout = QtGui.QHBoxLayout()
        self.InfoLayout.addWidget(self.Info)
        self.gbxInfo.setLayout(self.InfoLayout)
        self.Wdg = QtGui.QVBoxLayout()
        self.Frame.setLayout(self.Layout)
        self.tabWidget = QtGui.QTabWidget()
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 621, 611))
        self.tabAnalyze = QtGui.QWidget()
        self.lblTarget = QtGui.QLabel(self.tabAnalyze)
        self.lblTarget.setGeometry(QtCore.QRect(10, 20, 64, 21))
        self.edtTarget = QtGui.QLineEdit(self.tabAnalyze)
        self.edtTarget.setGeometry(QtCore.QRect(90, 10, 441, 33))
        self.btnAnalyze = QtGui.QPushButton(self.tabAnalyze)
        self.btnAnalyze.setGeometry(QtCore.QRect(540, 10, 71, 31))
        self.lblMethod = QtGui.QLabel(self.tabAnalyze)
        self.lblMethod.setGeometry(QtCore.QRect(10, 60, 64, 21))
        self.cbxMethod = QtGui.QComboBox(self.tabAnalyze)
        self.cbxMethod.setGeometry(QtCore.QRect(90, 60, 76, 29))
        self.cbxMethod.addItem("")
        self.cbxMethod.addItem("")
        self.lblPostData = QtGui.QLabel(self.tabAnalyze)
        self.lblPostData.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.lblPostData.setVisible(False)
        self.edtPostData = QtGui.QLineEdit(self.tabAnalyze)
        self.edtPostData.setGeometry(QtCore.QRect(90, 100, 441, 33))
        self.edtPostData.setVisible(False)
        self.tabWidget.addTab(self.tabAnalyze, "")
        self.tabRawData = QtGui.QWidget()
        self.tabWidget.addTab(self.tabRawData, "")
        self.tabData = tabData(self)
        self.tabWidget.addTab(self.tabData, 'Data')
        self.RawData = Raw_Data(self)
        self.RawView = QtGui.QPlainTextEdit()
        self.RawView.setReadOnly(True)
        self.RDLayout = QtGui.QHBoxLayout(self.tabRawData)
        self.RDLayout.addWidget(self.RawData)
        self.RDLayout.addWidget(self.RawView)
        MainWindow.setCentralWidget(self.Frame)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 27))
        self.menubar.setObjectName("menubar")
        self.menuTyrant = QtGui.QMenu(self.menubar)
        self.menuTyrant.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSql_Map_Hlelp = QtGui.QAction(MainWindow)
        self.actionOnline_Help = QtGui.QAction(MainWindow)
        self.actionLicense = QtGui.QAction(MainWindow)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setText('Preferences')
        self.menuTyrant.addSeparator()
        self.menuTyrant.addAction(self.actionPreferences)
        self.menuTyrant.addSeparator()
        self.menuTyrant.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionSql_Map_Hlelp)
        self.menuHelp.addAction(self.actionOnline_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionLicense)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuTyrant.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.Wdg.addWidget(self.tabWidget)
        self.Wdg.addWidget(self.gbxInfo)
        self.Wdg.setStretchFactor(self.tabWidget, 10)
        self.Wdg.setStretchFactor(self.gbxInfo, 5)
        self.Layout.addLayout(self.Wdg)
        self.RawData.hide()
        Test = TestPython()
        Working = Test.TestVersion()
        Test2 = TestPython(1)
        Working = Test2.TestVersion()
        if not Working:
            Msg = QtGui.QMessageBox()
            Msg.information(self, 'Python',
                    'Tyrant failed to find Python >=2.5.* and <=2.7.* \n Goto'
                    + ' preferences!!')

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        #to hide or show post data
        QtCore.QObject.connect(self.cbxMethod, QtCore.SIGNAL
                            ("currentIndexChanged(int)"), self.ShowHidePostData)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionPreferences.triggered.connect(self.OpenPreferences)
        self.SQLMap = SqlMap(self)
        self.btnAnalyze.clicked.connect(self.Analyze)
        self.actionSql_Map_Hlelp.triggered.connect(self.SqlMapHelp)
        self.actionAbout.triggered.connect(self.About)
        self.actionLicense.triggered.connect(self.License)
        self.actionOnline_Help.triggered.connect(self.TyrantHelp)
        self.actionExit.triggered.connect(self.close)

    def SqlMapHelp(self):
        Web = webbrowser.get()
        Web.open('http://www.sqlmap.org/')

    def TyrantHelp(self):
        Web = webbrowser.get()
        Web.open('https://github.com/aron-bordin/Tyrant-SQL/wiki')

    def License(self):
        Web = webbrowser.get()
        Web.open('http://www.gnu.org/licenses/gpl-3.0.txt')

    def About(self):
        Web = webbrowser.get()
        Web.open('https://github.com/aron-bordin/Tyrant-SQL/')

    def Analyze(self):
        self.SQLMap.IdentifyDB()

    def ShowHidePostData(self, ID):
        if ID is 0:
            self.edtPostData.setVisible(False)
            self.lblPostData.setVisible(False)
            self.edtPostData.setText('')
        else:
            self.edtPostData.setVisible(True)
            self.lblPostData.setVisible(True)

    def OpenPreferences(self):
        self.Pre = Ui_Preferences()
        self.Dialog = QtGui.QDialog()
        self.Pre.setupUi(self.Dialog, self)
        self.Dialog.exec_()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate
            ("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTarget.setText(QtGui.QApplication.translate
            ("MainWindow", "Target:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAnalyze.setText(QtGui.QApplication.translate
            ("MainWindow", "Analyze", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMethod.setText(QtGui.QApplication.translate
            ("MainWindow", "Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxMethod.setItemText(0, QtGui.QApplication.translate
            ("MainWindow", "GET", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxMethod.setItemText(1, QtGui.QApplication.translate
            ("MainWindow", "POST", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPostData.setText(QtGui.QApplication.translate
            ("MainWindow", "Post Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAnalyze),
             QtGui.QApplication.translate
             ("MainWindow", "Target", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRawData),
            QtGui.QApplication.translate("MainWindow", "Raw Data", None,
            QtGui.QApplication.UnicodeUTF8))
        self.menuTyrant.setTitle(QtGui.QApplication.translate
            ("MainWindow", "Tyrant", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate
            ("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSql_Map_Hlelp.setText(QtGui.QApplication.translate
            ("MainWindow", "Sql Map  Help",
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionOnline_Help.setText(QtGui.QApplication.translate
            ("MainWindow", "Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLicense.setText(QtGui.QApplication.translate
            ("MainWindow", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate
            ("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow",
            "Exit", None, QtGui.QApplication.UnicodeUTF8))