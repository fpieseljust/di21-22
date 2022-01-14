# Accions: barres de ferramentes i menús 

A continuació, veurem alguns dels elements comuns de la interfície d'usuari, que probablement heu vist en moltes altres aplicacions: barres d'eines i menús. Farem ús de *QAction* per a evitar duplicitat entre diferents parts de la interfície.

## Barres d'eines (*tool bar*)

Un dels elements de la interfície d'usuari més comuna és la barra de ferramentes. Són barres d'icones i/o text que s'utilitzen per realitzar tasques habituals dins d'una aplicació, per a les quals l'accés mitjançant un menú seria complicat. Són una de les funcions d'interfície d'usuari més comunes que es veuen en moltes aplicacions. Tot i que algunes aplicacions complexes, especialment a la suite de Microsoft Office, han migrat a interfícies de "menú" contextuals, la barra d'eines estàndard sol ser suficient per a la majoria d'aplicacions que creareu.

![Barra de ferramentes](../../../resources/img/PySide6/action/toolbar.png)

> Normalment es proporciona una interfície alternativa als menús per activar i desactivar les barres d'eines.

## QAction
QAction és una classe que proporciona una manera de descriure interfícies d'usuari abstractes. Això significa que podeu definir diversos elements d'interfície dins d'un únic objecte, unificats per l'efecte que té la interacció amb aquest element. Per exemple, és comú tindre funcions que es representen a la barra d'eines, però també al menú; penseu en alguna cosa com Edita->Retallar que està present tant al menú Edita com també a la barra d'eines com unes tisores, i també a través de la drecera de teclat Ctrl-X (Cmd-X a Mac).

Sense QAction hauríeu de definir-ho en diversos llocs. Però amb QAction podeu definir una única QAction, definint l'acció activada i després afegir aquesta acció tant al menú com a la barra d'eines. Cada QAction té noms, missatges d'estat, icones i senyals als quals us podeu subscriure.

Al codi següent podeu veure aquesta primera QAction a una barra de ferramentes.


### Exemple

```py
import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)



    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```

## Barra d'estat (*status bar*)

En el següent exemple creem una barra d'estat i l'afegim a la finestra principal. En passar el ratolí per damunt el botó de la barra d'estat, es mostra el text definit a la barra d'estats.

#### Exemple

```py
import sys
import os

from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        icon_path = os.path.join(os.path.dirname(__file__), "img/animal-penguin.png")

        button_action = QAction(QIcon(icon_path), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))



    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```

Podem configurar l'action per a transformar el botó en un polsador. A més, també podem afegir una icona i configurar la posició del text que acompanya a aquesta icona segons els valors de la taula següents:

| Flag                        | Comportament                                      |
| :-------------------------- | :------------------------------------------------ |
| Qt.ToolButtonIconOnly       | Icona sola, sense text                            |
| Qt.ToolButtonTextOnly       | Text sol, sense icona                             |
| Qt.ToolButtonTextBesideIcon | Icona i text, amb el text al costat de la icona   |
| Qt.ToolButtonTextUnderIcon  | Icona i text, amb el text baix de la icona        |
| Qt.ToolButtonFollowStyle    | Seguir l'estil de la configuració de l'escriptori |

El valor predeterminat és Qt.ToolButtonFollowStyle, el que significa que la vostra aplicació seguirà per defecte la configuració estàndard/global per a l'escriptori on s'executa l'aplicació. Això es recomana generalment perquè la vostra aplicació s'integre millor i es senta el més nativa possible.

Finalment, afegirem un segon botó i un *checkbox* a la barra de ferramentes. Podeu posar qualsevol component.

> Podeu accedir a icones publicades baix CC al següent [enllaç](http://p.yusukekamiyamane.com/)

## Menús

Els menús són un altre component estàndard de les interfícies d'usuari. Normalment es troben a la part superior de la finestra o a la part superior d'una pantalla a macOS. Permeten l'accés a totes les funcions estàndard de l'aplicació. Hi ha uns quants menús estàndard, per exemple Fitxer, Edita, Ajuda. Els menús es poden *anidar* per crear arbres jeràrquics de funcions i sovint admeten i mostren dreceres de teclat per accedir ràpidament a les seves funcions.

Per crear un menú, creem una barra de menús que anomenem **.menuBar()** a QMainWindow. Afegim un menú a la nostra barra de menús cridant a **.addMenu()**, passant el nom del menú. En este cas l'hem anomenat "&Fitxer". El *ampersand* defineix una tecla ràpida per mostrar aquest menú en prémer Alt.

> Això no serà visible a macOS. Tingueu en compte que no estem definint una drecera de teclat.

Ací és on entra en joc el poder de les accions. Podem reutilitzar el QAction ja existent per afegir la mateixa funció al menú. Per afegir una acció, cridem a **.addAction()** passant en una de les nostres accions definides.

```py
import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        icon_path = os.path.join(os.path.dirname(__file__), "img/animal-penguin.png")

        button_action = QAction(QIcon(icon_path), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon(icon_path), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```

> Feu clic a l'element del menú i notareu que es pot alternar com un polsador: hereta les característiques de QAction.

En este segon exemple, afegim algunes coses més al menú. Afegirem un separador al menú, que apareixerà com una línia horitzontal al menú, i després afegirem la segona QAction que hem creat.

```py
import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        icon_path = os.path.join(os.path.dirname(__file__), "img/animal-penguin.png")

        button_action = QAction(QIcon(icon_path), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon(icon_path), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```

També podeu fer servir un *ampersand* per afegir **tecles d'acceleració** al menú per permetre que una sola tecla s'utilitzi per anar a un element del menú **quan estiga obert**. De nou, això no funciona a macOS.

Per afegir un submenú, només cal que creeu un nou menú cridant a **addMenu()** al menú principal. A continuació, podeu afegir accions amb normalitat. 

![Submenu](../../../resources/img/PySide6/action/submenu.png)

```py
import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        icon_path = os.path.join(os.path.dirname(__file__), "img/animal-penguin.png")

        button_action = QAction(QIcon(icon_path), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon(icon_path), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```

### Dreceres de teclat

Finalment afegirem una drecera de teclat a QAction. Definim una drecera de teclat passant **setKeySequence()** i passant la seqüència de tecles. Qualsevol seqüència de tecles definida apareixerà al menú.

> Tingueu en compte que la drecera de teclat està associada amb el QAction i seguirà funcionant tant si el QAction s'afegeix o no a un menú o a una barra d'eines.

Les dreceres de teclat es poden definir de diverses maneres, ja sigui passant com a text, utilitzant noms de tecles o utilitzant les seqüències de tecles definides. Utilitzeu aquest últim sempre que pugueu per garantir el compliment dels estàndards del sistema operatiu.

#### Exemple

```py
import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")

        # The `Qt` namespace has a lot of attributes to customize
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        icon_path = os.path.join(os.path.dirname(__file__), "img/animal-penguin.png")

        button_action = QAction(QIcon(icon_path), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        # You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
        # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
        # or system agnostic identifiers (e.g. QKeySequence.Print)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon(icon_path), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")

        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
                
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```