# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercise_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Home_Frame import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget




class Exercise_Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Exercise_Frame")
        self.resize(800, 450)
        
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(700, 340, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Back")
        self.pushButton.clicked.connect(self.go_to_home)

    def go_to_home(self):
        main_window = self.window()  # Access the parent window
        while main_window is not None and not isinstance(main_window, QMainWindow):
            main_window = main_window.parent()
        if main_window is not None:
            main_window.open_page1()  # Go back to page 1
