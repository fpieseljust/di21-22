from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap("github/di21-22/docs/resources/code/PySide6/logo_qt.png"))
        widget.setScaledContents(True)
        # font = widget.font()
        # font.setPointSize(30)
        # font.setFamily("Noto Serif Armenian")
        # font.setBold(True)
        # widget.setFont(font)
        # widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)

app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()
