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
