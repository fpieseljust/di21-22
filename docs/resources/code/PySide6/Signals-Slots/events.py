import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")        
        self.setCentralWidget(self.label)
        #self.centralWidget().setAttribute(Qt.WA_TransparentForMouseEvents)
        #self.setMouseTracking(False)

    def mouseMoveEvent(self, e):
        tracking = self.hasMouseTracking()
        self.label.setText(f'mouseMoveEvent {tracking}')

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()