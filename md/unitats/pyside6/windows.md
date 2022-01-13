# Finestres adicionals

Hem vist fins ara com crear diàlegs modals que executen el seu propi bucle d'esdeveniments, bloquejant l'execució de la resta de l'aplicació.

Tanmateix, de vegades voldreu obrir una segona finestra en una aplicació, sense interrompre la finestra principal, per exemple, per mostrar l'eixida d'algun procés de llarga durada, o mostrar gràfics o altres visualitzacions. Alternativament, és possible que vulgueu crear una aplicació que us permeta treballar amb diversos documents alhora, a les seves pròpies finestres.

És relativament senzill obrir finestres noves, però cal tenir en compte algunes coses per assegurar-vos que funcionin bé. En aquest apartat explicarem com crear una finestra nova i com mostrar i amagar finestres externes sota demanda.

## Creant una nova finestra

A Qt qualsevol *widget* sense un pare és una finestra. Això vol dir que per mostrar una nova finestra només cal que creeu una nova instància d'un widget. Pot ser qualsevol tipus de widget (tècnicament qualsevol subclasse de QWidget) inclòs un altre QMainWindow si voleu.

> No hi ha cap restricció sobre el nombre d'instàncies de QMainWindow que podeu tindre. Si necessiteu barres d'eines o menús a la vostra segona finestra, haureu d'utilitzar un QMainWindow per aconseguir-ho. Tanmateix, això pot resultar confús per als usuaris, així que assegureu-vos que siga necessari.

Igual que amb la vostra finestra principal, crear una finestra no és suficient, també l'heu de mostrar:

```py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
    )

import sys

from random import randint


class AnotherWindow(QWidget):
    """
    Esta finestra és un QWidget, si no té parent,
    es mostrarà com una finestra flotant.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        '''
        Necessitem que la finestra siga una propietat de la classe,
        ja que si no, al eixir del mètode es perdrà la referència a esta i es
        destruirà
        '''
        self.w = None  # Referència nula
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

Aquesta solució està bé per a les finestres que creeu temporalment, per exemple, si voleu que aparega una finestra per mostrar una finestra de log. Tanmateix, per a moltes aplicacions disposeu d'una sèrie de finestres estàndard que podeu mostrar/amagar sota demanda.

Al següent exemple, la finestra es crea al construir l'aplicació, i amb un botó, controlem si es fa visible o s'amaga, sense necessitat de crear-la de nou i destruir-la cada vegada.

```py
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from random import randint


class AnotherWindow(QWidget):
    """
    Esta finestra és un QWidget, si no té parent,
    es mostrarà com una finestra flotant.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        '''
        Necessitem que la finestra siga una propietat de la classe,
        ja que si no, al eixir del mètode es perdrà la referència a esta i es
        destruirà
        '''
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()

        else:
            self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
```

A este tercer exemple, utilitzem les funcions lambda per controlar que diverses finestres apareguen o s'oculten amb una sola funció.

```py
import sys
from random import randint

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
```