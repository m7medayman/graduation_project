# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensoryFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from HomeFramePro import Ui_MainWindow
from live_plot_module.bar_chart import BarChartWidget
from live_plot_module.live_plot import LivePlot
from live_plot_module.live_dot_plot import PointPlotWidget
from sensory_model import SensoryModel
from test_model import TestModel
from person import Person

class Ui_sensoryFramePro(object):
    def setupUi(self, sensoryFrame):
        self.model=SensoryModel()
        sensoryFrame.setObjectName("sensoryFrame")
        sensoryFrame.resize(800, 470)
        sensoryFrame.setStyleSheet("background-color: #141332;")
        self.backButton = QtWidgets.QPushButton(sensoryFrame)
        self.backButton.setGeometry(QtCore.QRect(30, 390, 151, 31))
        self.backButton.setStyleSheet("QPushButton {\n"
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
        self.backButton.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(sensoryFrame)
        self.frame.setGeometry(QtCore.QRect(20, 50, 361, 291))
        self.frame.setStyleSheet("background-color:#1D1D41;\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_chart = QtWidgets.QFrame(self.frame)
        self.frame_chart.setGeometry(QtCore.QRect(10, 9, 341, 241))
        self.frame_chart.setStyleSheet("background-color:#8C89B4;\n"
"border-radius: 15px;")
        self.frame_chart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_chart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_chart.setObjectName("frame_chart")
        self.frame_t1 = QtWidgets.QFrame(self.frame)
        self.frame_t1.setGeometry(QtCore.QRect(10, 260, 51, 20))
        self.frame_t1.setStyleSheet("background-color:#64CFF6;\n"
"border-radius: 30px;")
        self.frame_t1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_t1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t1.setObjectName("frame_22")
        self.label_10 = QtWidgets.QLabel(self.frame_t1)
        self.label_10.setGeometry(QtCore.QRect(20, 0, 31, 16))
        self.label_10.setStyleSheet("QLabel {\n"
"    color: #ffffff; /* Change this to your desired text color */\n"
"    font-family: Arial; /* Change this to your desired font family */\n"
"    font-size: 12px; /* Change this to your desired font size */\n"
"    font-weight: bold; /* Make the text bold */\n"
"    /* Add other text properties as needed */\n"
"}")
        self.label_10.setObjectName("label_10")
        self.frame_t2 = QtWidgets.QFrame(self.frame)
        self.frame_t2.setGeometry(QtCore.QRect(70, 260, 51, 20))
        self.frame_t2.setStyleSheet("background-color:#64CFF6;\n"
"border-radius: 30px;")
        self.frame_t2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_t2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t2.setObjectName("frame_23")
        self.label_12 = QtWidgets.QLabel(self.frame_t2)
        self.label_12.setGeometry(QtCore.QRect(20, 0, 31, 16))
        self.label_12.setStyleSheet("QLabel {\n"
"    color: #ffffff; /* Change this to your desired text color */\n"
"    font-family: Arial; /* Change this to your desired font family */\n"
"    font-size: 12px; /* Change this to your desired font size */\n"
"    font-weight: bold; /* Make the text bold */\n"
"    /* Add other text properties as needed */\n"
"}")
        self.label_12.setObjectName("label_12")
        self.frame_t3 = QtWidgets.QFrame(self.frame)
        self.frame_t3.setGeometry(QtCore.QRect(130, 260, 51, 20))
        self.frame_t3.setStyleSheet("background-color:#64CFF6;\n"
"border-radius: 30px;")
        self.frame_t3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_t3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t3.setObjectName("frame_24")
        self.label_14 = QtWidgets.QLabel(self.frame_t3)
        self.label_14.setGeometry(QtCore.QRect(20, 0, 31, 16))
        self.label_14.setStyleSheet("QLabel {\n"
"    color: #ffffff; /* Change this to your desired text color */\n"
"    font-family: Arial; /* Change this to your desired font family */\n"
"    font-size: 12px; /* Change this to your desired font size */\n"
"    font-weight: bold; /* Make the text bold */\n"
"    /* Add other text properties as needed */\n"
"}")
        self.label_14.setObjectName("label_14")
        self.frame_t4 = QtWidgets.QFrame(self.frame)
        self.frame_t4.setGeometry(QtCore.QRect(190, 260, 51, 20))
        self.frame_t4.setStyleSheet("background-color:#64CFF6;\n"
"border-radius: 30px;")
        self.frame_t4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_t4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t4.setObjectName("frame_25")
        self.label_17 = QtWidgets.QLabel(self.frame_t4)
        self.label_17.setGeometry(QtCore.QRect(20, 0, 31, 16))
        self.label_17.setStyleSheet("QLabel {\n"
"    color: #ffffff; /* Change this to your desired text color */\n"
"    font-family: Arial; /* Change this to your desired font family */\n"
"    font-size: 12px; /* Change this to your desired font size */\n"
"    font-weight: bold; /* Make the text bold */\n"
"    /* Add other text properties as needed */\n"
"}")
        self.label_17.setObjectName("label_17")
        self.frame_t5 = QtWidgets.QFrame(self.frame)
        self.frame_t5.setGeometry(QtCore.QRect(310, 260, 51, 20))
        self.frame_t5.setStyleSheet("background-color:#64CFF6;\n"
"border-radius: 30px;")
        self.frame_t5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_t5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t5.setObjectName("frame_31")
        self.label_18 = QtWidgets.QLabel(self.frame_t5)
        self.label_18.setGeometry(QtCore.QRect(20, 0, 31, 16))
        self.label_18.setStyleSheet("QLabel {\n"
"    color: #ffffff; /* Change this to your desired text color */\n"
"    font-family: Arial; /* Change this to your desired font family */\n"
"    font-size: 12px; /* Change this to your desired font size */\n"
"    font-weight: bold; /* Make the text bold */\n"
"    /* Add other text properties as needed */\n"
"}")
        self.label_18.setObjectName("label_18")
        self.frame_t6 = QtWidgets.QFrame(self.frame)
        self.frame_t6.setGeometry(QtCore.QRect(250, 260, 51, 20))
        self.frame_t6.setStyleSheet("background-color:#64CFF6;\n"
"border-radius: 30px;")
        self.frame_t6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_t6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t6.setObjectName("frame_32")
        self.label_19 = QtWidgets.QLabel(self.frame_t6)
        self.label_19.setGeometry(QtCore.QRect(20, 0, 31, 16))
        self.label_19.setStyleSheet("QLabel {\n"
"    color: #ffffff; /* Change this to your desired text color */\n"
"    font-family: Arial; /* Change this to your desired font family */\n"
"    font-size: 12px; /* Change this to your desired font size */\n"
"    font-weight: bold; /* Make the text bold */\n"
"    /* Add other text properties as needed */\n"
"}")
        self.label_19.setObjectName("label_19")
        self.frame_2 = QtWidgets.QFrame(sensoryFrame)
        self.frame_2.setGeometry(QtCore.QRect(410, 50, 371, 291))
        self.frame_2.setStyleSheet("background-color:#1D1D41;\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_x = QtWidgets.QFrame(self.frame_2)
        self.frame_x.setGeometry(QtCore.QRect(190, 170, 171, 101))
        self.frame_x.setStyleSheet("background-color:#8C89B4;\n"
"border-radius: 15px;")
        self.frame_x.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_x.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_x.setObjectName("frame_x")
        self.frame_y = QtWidgets.QFrame(self.frame_2)
        self.frame_y.setGeometry(QtCore.QRect(10, 170, 171, 101))
        self.frame_y.setStyleSheet("background-color:#8C89B4;\n"
"border-radius: 15px;")
        self.frame_y.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_y.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_y.setObjectName("frame_y")
        self.frame_dotPlot = QtWidgets.QFrame(self.frame_2)
        self.frame_dotPlot.setGeometry(QtCore.QRect(70, 10, 221, 151))
        self.frame_dotPlot.setStyleSheet("background-color:#8C89B4;\n"
"border-radius: 15px;")
        self.frame_dotPlot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dotPlot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dotPlot.setObjectName("frame_28")
        self.pushButton = QtWidgets.QPushButton(sensoryFrame)
        self.pushButton.setGeometry(QtCore.QRect(620, 392, 151, 31))
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
        self.progressBar = QtWidgets.QProgressBar(sensoryFrame)
        self.progressBar.setGeometry(QtCore.QRect(20, 352, 761, 21))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 1px solid grey ;\n"
"    border-radius: 300px;\n"
"    text-align: center;\n"
"    background-color:#1D1D41;\n"
"    color: #ffffff;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"    \n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #64CFF6; /* Change this color to your desired color */\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.label = QtWidgets.QLabel(sensoryFrame)
        self.label.setGeometry(QtCore.QRect(210, 10, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: white;  /* Change \'red\' to any color you prefer */\n"
"}")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")

        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.label_cond = QtWidgets.QLabel(sensoryFrame)
        self.label_cond.setGeometry(QtCore.QRect(240, 380, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_cond.setFont(font)
        self.label_cond.setStyleSheet("QLabel {\n"
"    color: white;  /* Change \'red\' to any color you prefer */\n"
"}")
        self.label_cond.setObjectName("label_cond")
######## setup Liveplot
        winX=pg.GraphicsLayoutWidget()
        layoutx = QVBoxLayout()
        self.frame_x.setLayout(layoutx)
        layoutx.addWidget(winX)
        winY=pg.GraphicsLayoutWidget()
        layoutY = QVBoxLayout()
        self.frame_y.setLayout(layoutY)
        layoutY.addWidget(winY)
        self.livePlotX=LivePlot(win=winX,row=0,col=0)
        
        self.livePlotY=LivePlot(win=winY,row=0,col=0)

        # Create a layout for the central widget
        layoutDotPlot = QVBoxLayout()
        layoutDotPlot.addWidget(self.frame_dotPlot)
        # Set up the frame layout
        frameLayoutDotPlot = QVBoxLayout(self.frame_dotPlot)
        self.frame_dotPlot.setLayout(frameLayoutDotPlot)
        # Create and add the plot widget to the frame
        self.dotPlot = PointPlotWidget(parent=self.frame_dotPlot)
        frameLayoutDotPlot.addWidget(self.dotPlot)
        #creat chart plot 
        frameLayoutChart= QVBoxLayout()
        self.frame_chart.setLayout(frameLayoutChart)
        self.bar_chart_widget = BarChartWidget([10 ,20 ,50 ,10 ,20,90])
        frameLayoutChart.addWidget(self.bar_chart_widget)


###### frame control 
        self.frameControl=[self.frame_t1,self.frame_t2,self.frame_t3,self.frame_t4,self.frame_t5 ,self.frame_t6]
#######end of setup liveplot
        self.teckperiod=5 #5 ms 
        self.retranslateUi(sensoryFrame)
        QtCore.QMetaObject.connectSlotsByName(sensoryFrame)
        self.person=Person(name="mohamed")
        self.testModel=TestModel(period=300,person=self.person) #4000 * 5 ms=20s
#################### end of gui setup
#################### buttons function connect section  
        self.backButton.clicked.connect(self.go_to_home)
        self.pushButton.clicked.connect(self.startTest)
#################### end of buttton function connect section 
#################### time loop setup
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(0.01) 
################### end of time loop setup
################## time update loop

    def startTest(self):
        self.model.setCenter()
        self.testModel.startButtonFunction()


    def updateFrameColor(self,frame,hexColor):
        hex_color = hexColor
        frame.setStyleSheet(f"background-color: {hex_color};")
    def selectTestFrame(self,index):
        for frame in self.frameControl :
            if self.frameControl.index(frame)==index :
                self.updateFrameColor(frame=frame,hexColor="#64CFF6")
            else:
                self.updateFrameColor(frame=frame,hexColor="#8C89B6")
            
        
    def update(self):
        
        self.model.updateLoop()
        sensorX=self.model.getSensorX()
        sensorY=self.model.getSensorY()
        self.selectTestFrame(self.testModel.getCurrentTestNumber())
        self.testModel.updateLoop(xRead=sensorX,yRead=sensorY)
        self.progressBar.setProperty("value", self.testModel.getTestTimepercent())
        self.pushButton.setText(self.testModel.getSatausText())
        self.livePlotX.update(sensorX)
        self.livePlotY.update(sensorY)
        self.dotPlot.setPosition(x=sensorX,y=sensorY)
        self.dotPlot.update()
################# end of update loop 


    def retranslateUi(self, sensoryFrame):
        _translate = QtCore.QCoreApplication.translate
        sensoryFrame.setWindowTitle(_translate("sensoryFrame", "Frame"))
        self.backButton.setText(_translate("sensoryFrame", "back "))
        self.label_10.setText(_translate("sensoryFrame", "C1"))
        self.label_12.setText(_translate("sensoryFrame", "C2"))
        self.label_14.setText(_translate("sensoryFrame", "C3"))
        self.label_17.setText(_translate("sensoryFrame", "C4"))
        self.label_19.setText(_translate("sensoryFrame", "C5"))
        self.label_18.setText(_translate("sensoryFrame", "C6"))
        self.pushButton.setText(_translate("sensoryFrame", "start and stop button"))
        self.label.setText(_translate("sensoryFrame", "Sensory organization test "))
        self.label_cond.setText(_translate("sensoryFrame", "cond1: eye opend , fixed platform "))




    def go_to_home(self):
        self.timer.stop()
        # Close the current window (Exercise_Frame) and show the main window (Home_Frame)
        main_window = self.backButton.window()  # Access the parent window
        while main_window is not None and not isinstance(main_window, QtWidgets.QMainWindow):
            main_window = main_window.parent()
        if main_window is not None:
            home_frame = Ui_MainWindow()  # Instantiate the home frame
            # Set up the home frame in the main window
            home_frame.setupUi(main_window)
            main_window.show()  # Show the main window
            main_window.close()
          # Close the current window
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sensoryFrame = QtWidgets.QFrame()
    ui = Ui_sensoryFramePro()
    ui.setupUi(sensoryFrame)
    sensoryFrame.show()
    sys.exit(app.exec_())
