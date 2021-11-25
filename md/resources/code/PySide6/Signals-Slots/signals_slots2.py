import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        if self.windowTitle() == "La meua aplicació":
            self.setWindowTitle("My App")
        else:
            self.setWindowTitle("La meua aplicació")

    def the_button_was_toggled(self):
        print("Clic rebut!")

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
 

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
