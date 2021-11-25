from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(300, 300))
        self.setWindowTitle("Exemple signals-slots 1")

        pybutton = QPushButton('Clic', self)
        
        #Connectem la senyal clicked a la ranura button_pressed
        pybutton.clicked.connect(self.button_pressed) 

        pybutton.resize(100, 100)
        pybutton.move(100, 100)

    def button_pressed(self):
        '''
            S'executaà al rebre la notificació de que s'ha apretat el botó:
            - Observeu que la consola imprimirà "Clic rebut!" al fer clic al botó
        '''
        print('Clic rebut!')

if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()