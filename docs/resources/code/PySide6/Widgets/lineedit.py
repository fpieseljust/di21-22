from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        
        widget = QWidget()

        line_edit = QLineEdit(widget)
        line_edit.setMaxLength(10)
        line_edit.setPlaceholderText("Enter your text")

        #widget.setReadOnly(True) # uncomment this to make readonly

        line_edit.returnPressed.connect(self.return_pressed)
        line_edit.selectionChanged.connect(self.selection_changed)
        line_edit.textChanged.connect(self.text_changed)
        line_edit.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)


    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication([])
window = MainWindow()
window.show()

app.exec()