from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.widget = QComboBox()
        self.widget.addItems(["One", "Two", "Three"])

        # The default signal from currentIndexChanged sends the index
        self.widget.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        self.widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(self.widget)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()