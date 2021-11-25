import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        container = QWidget()
        container.setFixedSize(240,100)

        self.label = QLabel(container)
        self.label.setFixedSize(200,20)
        self.label.move(20, 20)

        self.input = QLineEdit(container)
        self.input.setFixedSize(200,20)
        self.input.move(20, 60)
        self.input.textChanged.connect(self.label.setText)

        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()