import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    message = Signal(str)
    value = Signal(int, str, int)
    another = Signal(list)
    onemore = Signal(dict)
    anything = Signal(object)

    def __init__(self):
        super().__init__()
        self.message.connect(self.custom_slot)
        self.value.connect(self.custom_slot)
        self.another.connect(self.custom_slot)
        self.onemore.connect(self.custom_slot)
        self.anything.connect(self.custom_slot)

        self.message.emit("my message")
        self.value.emit(23, "abc", 1)
        self.another.emit([1, 2, 3, 4, 5])
        self.onemore.emit({"a": 2, "b": 7})
        self.anything.emit(1223)

        

    def custom_slot(self, a):
        print(a)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
