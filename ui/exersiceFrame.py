# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exersiceFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExerciseFrame(object):
    def setupUi(self, ExerciseFrame):
        ExerciseFrame.setObjectName("ExerciseFrame")
        ExerciseFrame.resize(800, 470)
        ExerciseFrame.setStyleSheet("background-color: #141332;")
        self.pushButton = QtWidgets.QPushButton(ExerciseFrame)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #6359E9; /* Change this to your desired background color */\n"
"    color: white; /* Change this to your desired text color */\n"
"    border: 2px; /* Change this to your desired border color and thickness */\n"
"    border-radius: 15px; /* Adjust the radius to your desired value for rounded corners */\n"
"    padding: 5px 10px; /* Adjust the padding to your desired value */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0ACDE4; /* Change this to your desired background color on hover */\n"
"    border: 2px solid #0ACDE4; /* Change this to your desired border color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0AADE2; /* Change this to your desired background color when pressed */\n"
"    border: 2px solid #0AADE2; /* Change this to your desired border color when pressed */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ExerciseFrame)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 230, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #6359E9; /* Change this to your desired background color */\n"
"    color: white; /* Change this to your desired text color */\n"
"    border: 2px; /* Change this to your desired border color and thickness */\n"
"    border-radius: 15px; /* Adjust the radius to your desired value for rounded corners */\n"
"    padding: 5px 10px; /* Adjust the padding to your desired value */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0ACDE4; /* Change this to your desired background color on hover */\n"
"    border: 2px solid #0ACDE4; /* Change this to your desired border color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0AADE2; /* Change this to your desired background color when pressed */\n"
"    border: 2px solid #0AADE2; /* Change this to your desired border color when pressed */\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(ExerciseFrame)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 360, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #6359E9; /* Change this to your desired background color */\n"
"    color: white; /* Change this to your desired text color */\n"
"    border: 2px; /* Change this to your desired border color and thickness */\n"
"    border-radius: 15px; /* Adjust the radius to your desired value for rounded corners */\n"
"    padding: 5px 10px; /* Adjust the padding to your desired value */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0ACDE4; /* Change this to your desired background color on hover */\n"
"    border: 2px solid #0ACDE4; /* Change this to your desired border color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0AADE2; /* Change this to your desired background color when pressed */\n"
"    border: 2px solid #0AADE2; /* Change this to your desired border color when pressed */\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(ExerciseFrame)
        QtCore.QMetaObject.connectSlotsByName(ExerciseFrame)

    def retranslateUi(self, ExerciseFrame):
        _translate = QtCore.QCoreApplication.translate
        ExerciseFrame.setWindowTitle(_translate("ExerciseFrame", "Frame"))
        self.pushButton.setText(_translate("ExerciseFrame", "Exercise 1"))
        self.pushButton_2.setText(_translate("ExerciseFrame", "Exercise 2"))
        self.pushButton_3.setText(_translate("ExerciseFrame", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExerciseFrame = QtWidgets.QFrame()
    ui = Ui_ExerciseFrame()
    ui.setupUi(ExerciseFrame)
    ExerciseFrame.show()
    sys.exit(app.exec_())