# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_defragScript.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_defragScript(object):
    def setupUi(self, defragScript):
        defragScript.setObjectName("defragScript")
        defragScript.resize(301, 204)
        self.centralwidget = QtWidgets.QWidget(defragScript)
        self.centralwidget.setObjectName("centralwidget")
        self.uploadBTN = QtWidgets.QPushButton(self.centralwidget)
        self.uploadBTN.setGeometry(QtCore.QRect(30, 35, 75, 31))
        self.uploadBTN.setObjectName("uploadBTN")
        self.executeBTN = QtWidgets.QPushButton(self.centralwidget)
        self.executeBTN.setEnabled(False)
        self.executeBTN.setGeometry(QtCore.QRect(30, 85, 75, 31))
        self.executeBTN.setObjectName("executeBTN")
        self.uploadText = QtWidgets.QLabel(self.centralwidget)
        self.uploadText.setEnabled(True)
        self.uploadText.setGeometry(QtCore.QRect(130, 35, 151, 31))
        self.uploadText.setFrameShape(QtWidgets.QFrame.Box)
        self.uploadText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.uploadText.setAlignment(QtCore.Qt.AlignCenter)
        self.uploadText.setWordWrap(True)
        self.uploadText.setObjectName("uploadText")
        self.executeText = QtWidgets.QLabel(self.centralwidget)
        self.executeText.setEnabled(True)
        self.executeText.setGeometry(QtCore.QRect(130, 85, 151, 31))
        self.executeText.setFrameShape(QtWidgets.QFrame.Box)
        self.executeText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.executeText.setAlignment(QtCore.Qt.AlignCenter)
        self.executeText.setWordWrap(True)
        self.executeText.setObjectName("executeText")
        self.saveBTN = QtWidgets.QPushButton(self.centralwidget)
        self.saveBTN.setEnabled(False)
        self.saveBTN.setGeometry(QtCore.QRect(30, 135, 75, 31))
        self.saveBTN.setObjectName("saveBTN")
        self.saveText = QtWidgets.QLabel(self.centralwidget)
        self.saveText.setEnabled(True)
        self.saveText.setGeometry(QtCore.QRect(130, 135, 151, 31))
        self.saveText.setFrameShape(QtWidgets.QFrame.Box)
        self.saveText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.saveText.setAlignment(QtCore.Qt.AlignCenter)
        self.saveText.setWordWrap(True)
        self.saveText.setObjectName("saveText")
        defragScript.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(defragScript)
        self.statusbar.setObjectName("statusbar")
        defragScript.setStatusBar(self.statusbar)

        self.retranslateUi(defragScript)
        QtCore.QMetaObject.connectSlotsByName(defragScript)

    def retranslateUi(self, defragScript):
        _translate = QtCore.QCoreApplication.translate
        defragScript.setWindowTitle(_translate("defragScript", "Defragmantation Algorithm"))
        self.uploadBTN.setText(_translate("defragScript", "Upload"))
        self.executeBTN.setText(_translate("defragScript", "Execute"))
        self.uploadText.setText(_translate("defragScript", "TextLabel"))
        self.executeText.setText(_translate("defragScript", "TextLabel"))
        self.saveBTN.setText(_translate("defragScript", "Save"))
        self.saveText.setText(_translate("defragScript", "TextLabel"))
