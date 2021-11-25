from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.widget = QWidget()

        self.combo_box = QComboBox(self.widget)
        self.combo_box.setFixedWidth(200)
        self.combo_box.addItems(["One", "Two", "Three"])
        
        # The default signal from currentIndexChanged sends the index
        self.combo_box.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        self.combo_box.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(self.widget)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()