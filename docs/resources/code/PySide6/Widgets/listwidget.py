from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        # In QListWidget there are two separate signals for the item, and the str
        widget.currentItemChanged.connect( self.index_changed )
        widget.currentTextChanged.connect( self.text_changed )

        self.setCentralWidget(widget)


    def index_changed(self, i): # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s): # s is a str
        print(s)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()