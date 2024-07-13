import sys
from PyQt5 import  QtWidgets, QtGui, QtCore
import os
# import the classes
from Exercise_Frame import Exercise_Frame
from control_motor_gui import MotorControlUi
from HomeFramePro import Ui_mainFramePro
from sensoryFramePro import Ui_sensoryFramePro
import subprocess

from input import Ui_InputFrame


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
        self.loading_screen = LoadingScreen()
        self.loading_screen.show()
        QtCore.QTimer.singleShot(100, self.show_sensory_page)

    def show_sensory_page(self):
        self.sensory_page = QtWidgets.QMainWindow()
        self.ui = Ui_InputFrame()
        self.ui.setupUi(self.sensory_page)
        self.sensory_page.showFullScreen()
        self.loading_screen.close()

    def open_exercise_page(self):
        self.loading_screen = LoadingScreen()
        self.loading_screen.show()
        # Path to your Pygame script
        pygame_script_path = '/home/pi/body balance seeker/game_module/x_game/main_loop.py'
        # Start the Pygame script using subprocess
        subprocess.Popen(['python', pygame_script_path])
                # Close the loading screen after a short delay
        QtCore.QTimer.singleShot(25000, self.loading_screen.close)
        # self.close()
    def open_option_page(self):
        self.exercise_page = QtWidgets.QMainWindow()
        self.ui = MotorControlUi()  # Assuming Exercise_Frame is defined in exercise_page.py
        self.ui.setupUi(self.exercise_page)
        self.exercise_page.showFullScreen()

class LoadingScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Loading')
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # No window frame
        self.setWindowState(QtCore.Qt.WindowFullScreen)  # Fullscreen

        # Create a black background
        self.setStyleSheet("background-color: black;")

        # Create a label for the loading text
        self.label = QtWidgets.QLabel('Loading...', self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 30px;")

        # Create a layout and add the label
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
if __name__ == "__main__":
    import sys

    #  create an application
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
