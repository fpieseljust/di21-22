## Components (Widgets)

A Qt (i la majoria de les interfícies d'usuari) *widget* és el nom donat a un component de la interfície d'usuari amb el qual l'usuari pot interactuar. Les interfícies d'usuari estan formades per diversos *widgets* o components, disposats dins de la finestra.

Qt inclou una gran selecció de *widgets* disponibles, i fins i tot us permet crear els vostres propis components personalitzats.

### Una demostració ràpida

Primer fem una ullada a alguns dels *widgets* PySide més comuns. El codi següent crea una sèrie de ginys PySide i els afegeix a un disseny de finestra perquè pugueu veure'ls junts.

    Veurem com funcionen els *layouts* a més endavant.

```python
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
```

Podeu baixar el codi [ací](../../resources/code/PySide6/Widgets/widgets1.py)

### Principals Widgets

PySide6 té disponible multitud de widgets i cadascun d'ells s'utilitza de forma semblant, amb algunes peculiaritats segons el seu tipus. Veurem ara alguns exemples de cadascun dels principals Widgets:

#### Label

```python
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
```

Pots baixar el codi [ací](../../resources/code/PySide6/Widgets/label.py)

#### CheckBox

```python
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.widget = QCheckBox()
        self.widget.setCheckState(Qt.Checked)
        self.widget.setTristate(True)

        # For tristate: self.widget.setCheckState(Qt.PartiallyChecked)
        # Or: self.widget.setTriState(True)
        self.widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(self.widget)


    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)
        self.widget.move(0, 50)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()
```

Pots baixar el codi [ací](../../resources/code/PySide6/Widgets/checkbox.py)

#### ComboBox

```python
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
```

Pots baixar el codi [ací](../../resources/code/PySide6/Widgets/comboBox.py)

#### ListWidget

```python
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
```

Pots baixar el codi [ací](../../resources/code/PySide6/Widgets/listwidget.py)

#### LineEdit

```python
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
```

Pots baixar el codi [ací](../../resources/code/PySide6/Widgets/lineedit.py)

#### SpinBox

```python
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()
```

Pots baixar el codi [ací](../../resources/code/PySide6/Widgets/spinbox.py)

#### Slider

```python
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
```

Pots baixar el codi [ací](../../resources/code/PySide6/Widgets/slider.py)

#### Dial

```python
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
```

Pots baixar el codi [ací](../../resources/code/PySide6/Widgets/dial.py)

#### Activitat 6

Fes una aplicació amb un dial, un slider i un label. Tant l'slider com el dial tindran valors entre 0 i 10. Quan es moga l'slider, el dial es mourà agafant el mateix valor i el label mostrarà el seu valor. Quan es mou el dial, el comportament serà el mateix.