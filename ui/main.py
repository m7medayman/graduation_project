import sys
from PyQt5 import QtWidgets
import os
# import the classes
from Home_Frame import Ui_MainWindow
from Exercise_Frame import Exercise_Frame
from Sensory_Frame import SensoryView
from Steper_Adjust import StepperAdjustFrame

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.QuitButton.clicked.connect(self.close)
        self.ui.SensorTestButton.clicked.connect(self.open_sensory_page)
        self.ui.ExerciseButton.clicked.connect(self.open_exercise_page)
        self.ui.OptionsButton.clicked.connect(self.open_option_page)

    def open_sensory_page(self):
        self.sensory_page = QtWidgets.QMainWindow()
        self.ui = SensoryView()  # Assuming Sensory_Frame is defined in sensory_page.py
        self.ui.setupUi(self.sensory_page)
        self.sensory_page.showFullScreen()

    def open_exercise_page(self):
        self.exercise_page = QtWidgets.QMainWindow()
        self.ui = Exercise_Frame()  # Assuming Exercise_Frame is defined in exercise_page.py
        self.ui.setupUi(self.exercise_page)
        self.exercise_page.show()
    def open_option_page(self):
        self.exercise_page = QtWidgets.QMainWindow()
        self.ui = StepperAdjustFrame()  # Assuming Exercise_Frame is defined in exercise_page.py
        self.ui.setup(self.exercise_page)
        self.exercise_page.showFullScreen()


if __name__ == "__main__":
    import sys

    #  create an application
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
