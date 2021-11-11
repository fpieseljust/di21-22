import sys
import argparse
from PySide6.QtCore import QSize

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, title="Title", button_text="Text", fixed=False):
        super().__init__()
        self.setWindowTitle(title)

        self.button = QPushButton(button_text)

        self.setCentralWidget(self.button)

app = QApplication(sys.argv)

window = MainWindow()

parser = argparse.ArgumentParser()
parser.add_argument("-t","--title", help="Title of application")
parser.add_argument("-b","--button-text",help="Button text")
parser.add_argument("-f","--fixed-size",help="Window fixed size", action='store_true')
parser.add_argument("-s","--size",help="Size of windows", nargs=2, type=int)
args = parser.parse_args()


if args.size:
    window.setBaseSize(QSize(int(args.size[0]),int(args.size[1])))
if args.fixed_size:
    window.setFixedSize(400,600)
else:
    window.button.setMaximumSize(100,25)
    window.setMaximumSize(400,400)
    window.setMinimumSize(200,200)

if(args.title):
    window.setWindowTitle(args.title)

if(args.button_text):
    window.button.setText(args.button_text)

window.button.show()
window.show()

app.exec()
