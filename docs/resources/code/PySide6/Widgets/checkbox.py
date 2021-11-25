from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.widget = QCheckBox()
        self.widget.setCheckState(Qt.Checked)
        self.widget.setTristate(True)

        # For tristate: self.widget.setCheckState(Qt.PartiallyChecked)
        # Or: self.widget.setTriState(True)
        self.widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(self.widget)


    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)
        self.widget.move(0, 50)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()