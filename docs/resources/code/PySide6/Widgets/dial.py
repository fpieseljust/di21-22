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
        dial.sliderMoved.connect(self.slider_position)
        dial.sliderPressed.connect(self.slider_pressed)
        dial.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        text = f'Value: {i}'
        self.label.setText(text)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")

app = QApplication([])
window = MainWindow()
window.show()

app.exec()