from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QDial, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QWidget()

        layout = QVBoxLayout(widget)

        dial = QDial()
        dial.setRange(0,60)
        dial.setSingleStep(1)
        layout.addWidget(dial)

        self.label = QLabel(f'Value: {dial.sliderPosition()}')
        layout.addWidget(self.label)

        dial.valueChanged.connect(self.value_changed)


        self.setCentralWidget(widget)

    def value_changed(self, i):
        text = f'Value: {i}'
        self.label.setText(text)
        print("position", i)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()