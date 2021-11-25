from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QSlider, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QWidget()

        slider = QSlider(widget)

        self.label = QLabel("  0 ",widget)
        self.label.move(25,0)

        slider.setMinimum(-10)
        slider.setMaximum(3)
        # Or: widget.setRange(-10,3)

        slider.setSingleStep(1)
        slider.setSliderPosition(0)

        slider.valueChanged.connect(self.value_changed)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        self.label.setText(str(i))

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