import sys
from PyQt5 import QtWidgets
import os
# import the classes
from Exercise_Frame import Exercise_Frame
from control_motor_gui import MotorControlUi
from HomeFramePro import Ui_mainFramePro
from sensoryFramePro import Ui_sensoryFramePro

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_mainFramePro()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.QuitButton.clicked.connect(self.close)
        self.ui.SensorTestButton.clicked.connect(self.open_sensory_page)
        self.ui.ExerciseButton.clicked.connect(self.open_exercise_page)
        self.ui.OptionsButton.clicked.connect(self.open_option_page)

    def open_sensory_page(self):
        self.sensory_page = QtWidgets.QMainWindow()
        self.ui = Ui_sensoryFramePro()
        self.ui.setupUi(self.sensory_page)
        self.sensory_page.showFullScreen()

    def open_exercise_page(self):
        self.exercise_page = QtWidgets.QMainWindow()
        self.ui = Exercise_Frame()  # Assuming Exercise_Frame is defined in exercise_page.py
        self.ui.setupUi(self.exercise_page)
        self.exercise_page.show()
    def open_option_page(self):
        self.exercise_page = QtWidgets.QMainWindow()
        self.ui = MotorControlUi()  # Assuming Exercise_Frame is defined in exercise_page.py
        self.ui.setupUi(self.exercise_page)
        self.exercise_page.showFullScreen()


if __name__ == "__main__":
    import sys

    #  create an application
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
