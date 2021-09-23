# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 589)
        MainWindow.setMinimumSize(QtCore.QSize(800, 580))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IT-куб3.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainTab = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MainTab.setFont(font)
        self.MainTab.setTabPosition(QtWidgets.QTabWidget.South)
        self.MainTab.setDocumentMode(True)
        self.MainTab.setObjectName("MainTab")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setMinimumSize(QtCore.QSize(200, 0))
        self.tab1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab1.setObjectName("tab1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setMaximumSize(QtCore.QSize(250, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(1)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line_3 = QtWidgets.QFrame(self.tab1)
        self.line_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.listBox = QtWidgets.QComboBox(self.tab1)
        self.listBox.setMinimumSize(QtCore.QSize(220, 0))
        self.listBox.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listBox.setFont(font)
        self.listBox.setObjectName("listBox")
        self.verticalLayout_2.addWidget(self.listBox)
        self.frame = QtWidgets.QFrame(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 178))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.add_Button = QtWidgets.QPushButton(self.frame)
        self.add_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.add_Button.setObjectName("add_Button")
        self.buttonMainGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonMainGroup.setObjectName("buttonMainGroup")
        self.buttonMainGroup.addButton(self.add_Button)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.add_Button)
        self.edit_Button = QtWidgets.QPushButton(self.frame)
        self.edit_Button.setObjectName("edit_Button")
        self.buttonMainGroup.addButton(self.edit_Button)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edit_Button)
        self.del_Button = QtWidgets.QPushButton(self.frame)
        self.del_Button.setObjectName("del_Button")
        self.buttonMainGroup.addButton(self.del_Button)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.del_Button)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.commit_Button = QtWidgets.QPushButton(self.frame)
        self.commit_Button.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.commit_Button.setFont(font)
        self.commit_Button.setAutoFillBackground(True)
        self.commit_Button.setFlat(False)
        self.commit_Button.setObjectName("commit_Button")
        self.buttonMainGroup.addButton(self.commit_Button)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.commit_Button)
        self.rollback_Button = QtWidgets.QPushButton(self.frame)
        self.rollback_Button.setMinimumSize(QtCore.QSize(150, 0))
        self.rollback_Button.setObjectName("rollback_Button")
        self.buttonMainGroup.addButton(self.rollback_Button)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.rollback_Button)
        self.labelCur2 = QtWidgets.QLabel(self.frame)
        self.labelCur2.setText("")
        self.labelCur2.setObjectName("labelCur2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelCur2)
        self.labelCur1 = QtWidgets.QLabel(self.frame)
        self.labelCur1.setText("")
        self.labelCur1.setObjectName("labelCur1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelCur1)
        self.transLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.transLabel.setFont(font)
        self.transLabel.setObjectName("transLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.transLabel)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 160))
        self.frame_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fltCheck = QtWidgets.QCheckBox(self.frame_2)
        self.fltCheck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fltCheck.setObjectName("fltCheck")
        self.verticalLayout_4.addWidget(self.fltCheck)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.fltLabel1 = QtWidgets.QLabel(self.frame_2)
        self.fltLabel1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fltLabel1.setObjectName("fltLabel1")
        self.verticalLayout_4.addWidget(self.fltLabel1)
        self.fltCombo1 = QtWidgets.QComboBox(self.frame_2)
        self.fltCombo1.setObjectName("fltCombo1")
        self.verticalLayout_4.addWidget(self.fltCombo1)
        self.fltLabel2 = QtWidgets.QLabel(self.frame_2)
        self.fltLabel2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fltLabel2.setObjectName("fltLabel2")
        self.verticalLayout_4.addWidget(self.fltLabel2)
        self.fltCombo2 = QtWidgets.QComboBox(self.frame_2)
        self.fltCombo2.setObjectName("fltCombo2")
        self.verticalLayout_4.addWidget(self.fltCombo2)
        self.fltLabel3 = QtWidgets.QLabel(self.frame_2)
        self.fltLabel3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fltLabel3.setObjectName("fltLabel3")
        self.verticalLayout_4.addWidget(self.fltLabel3)
        self.fltCombo3 = QtWidgets.QComboBox(self.frame_2)
        self.fltCombo3.setObjectName("fltCombo3")
        self.verticalLayout_4.addWidget(self.fltCombo3)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_6 = QtWidgets.QFrame(self.tab1)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout.addWidget(self.line_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.tab1)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.line_4 = QtWidgets.QFrame(self.tab1)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.tableLabel = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableLabel.setFont(font)
        self.tableLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tableLabel.setObjectName("tableLabel")
        self.verticalLayout_3.addWidget(self.tableLabel)
        self.line_5 = QtWidgets.QFrame(self.tab1)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.editFrame = QtWidgets.QFrame(self.tab1)
        self.editFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.editFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editFrame.setObjectName("editFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.editFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.editFrame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.buttonEditFrame = QtWidgets.QDialogButtonBox(self.editFrame)
        self.buttonEditFrame.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonEditFrame.setObjectName("buttonEditFrame")
        self.gridLayout.addWidget(self.buttonEditFrame, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.editFrame)
        self.tableView = QtWidgets.QTableView(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.MainTab.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.MainTab.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.MainTab.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.MainTab.addTab(self.tab4, "")
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.MainTab.addTab(self.tab5, "")
        self.verticalLayout.addWidget(self.MainTab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Перечень таблиц:"))
        self.add_Button.setText(_translate("MainWindow", "Добавить"))
        self.edit_Button.setText(_translate("MainWindow", "Изменить"))
        self.del_Button.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Текущая запись:"))
        self.commit_Button.setText(_translate("MainWindow", "Сохранить изменения"))
        self.rollback_Button.setText(_translate("MainWindow", "Отменить изменения"))
        self.transLabel.setText(_translate("MainWindow", "!"))
        self.fltCheck.setText(_translate("MainWindow", "Фильтр"))
        self.fltLabel1.setText(_translate("MainWindow", "TextLabel"))
        self.fltLabel2.setText(_translate("MainWindow", "TextLabel"))
        self.fltLabel3.setText(_translate("MainWindow", "TextLabel"))
        self.tableLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Ввод данных:"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.tab1), _translate("MainWindow", "Справочники"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.tab2), _translate("MainWindow", "Списочный состав"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.tab3), _translate("MainWindow", "Расписания"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.tab4), _translate("MainWindow", "Журналы"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.tab5), _translate("MainWindow", "Настройки"))
