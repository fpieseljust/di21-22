---
title: Introducció a la programació amb Python
author: Ferran Cunyat
lang: ca-ES
layout: page
permalink: /PyQt5/
---

# Qt i PyQt5

La biblioteca PyQt5 és simplement un *wrapper* a la biblioteca C++ Qt, per permetre que es puga utilitzar des de Python.

Com que es tracta d'una interfície Python per a una biblioteca C++, les convencions de noms que s’utilitzen a PyQt5 no compleixen els estàndards PEP8. Les funcions i les variables es nomenen utilitzant *mixedCase* en lloc de *snake_case*. **En els nostres desenvolupaments deuriem utilitzar els estàndars definits per Python**.

Per últim, tot i que hi ha documentació específica de PyQt5 disponible, serà més util **utilitzar la documentació de Qt**, ja que és més completa. S’haurà de traduir la sintaxi d'objectes i mètodes per adaptar-ho a Python.

## Instal·lació de PyQt5

### Windows i macOS

Per a instal·lar PyQt5 ho podem fer a través de l’instal·lador de paquets de Python, ja que està disponible a PyPi.

```py
pip3 install pyqt5
```

En cas de tindre disponible el Homebrew en macOS, podem instal·lar fent:

```py
brew install pyqt5 
```

### Debian i derivats
```py
apt install python3-pyqt5
```
Una vegada instal·lat ja podem fer:

```py
import PyQt5 
```
\newpage

# Primera aplicació amb PyQt5

```py
from PyQt5.QtWidgets import QApplication, QWidget
# Sols si necessitem arguments importem sys
import sys

# Necessitem una instància (i sols una) de QApplication per cada aplicació.
# Li passem sys.argv per a permetre arguments des de la línia de comandaments
# Si no anem a passar arguments podem utilitzar QApplication([])
app = QApplication(sys.argv)

# Creem un QtWidget, que serà la nostra finestra .
window = QWidget()
window.show() # IMPORTANT!!!!! Les finestres estan ocultes per defecte.

# Iniciem el bucle d’esdeveniments.
app.exec_()
#exec és una paraula reservada en Python 2.7, per això afegim _
```

## Què és una finestra?

- Conté la interfície de l’usuari
- Cada aplicació en necessita almenys una, però en pot tindre més
- L’aplicació, per defecte, acabarà en tancar l’última d’elles


## Què és el bucle d’esdeveniments (event loop)?

Ja hem vist que cada aplicació necessita un i sols un objecte QApplication. 

Aquest objecte gestiona els esdeveniments. Cada una de les interaccions de l’usuari amb la interfície, per exemple, un clic de ratolí sobre un element, genera un esdeveniment. 

L’esdeveniment es col·loca a la cola d’esdeveniments per ser gestionat (**event queue**).

Al bucle d'esdeveniments (**event loop**), la cua es comprova a cada iteració i si es troba un esdeveniment en espera, l'esdeveniment i el control es passen al gestor de l’esdeveniment (**event handler**).

El gestor d'esdeveniments s'ocupa de l'esdeveniment i després passa de nou el control al bucle d'esdeveniments per esperar més esdeveniments. 

Només hi ha un bucle d'esdeveniments per aplicació.

## QMainWindow
Es tracta d’un component pre-definit que proporciona moltes funcions estàndard de les finestres que fareu servir les vostres aplicacions, com poden ser les barres d'eines, els menús, la barra d'estat, els components que es poden acoblar, etc. Veurem aquestes funcions avançades més endavant, però de moment anem a fer ús d’ella a la nostra aplicació.

#### Activitat 2.1
Anem a crear la nostra primera aplicació.

1. Has de definir una classe MainWindow, que herede de QmainWindow.
2. Amb el mètode setWindowTitle() posa-li títol a l’aplicació «La meua aplicació». 
3. Amb QpushButton(), crea un botó amb el text, «Aceptar».
4. Afig el botó a la part central de la finestra amb setCentralWidget(«component»).
5. Recorda mostrar la finestra i iniciar el bucle d’esdeveniments.

![activitat2.1](img/activitat2.1.png "Activitat 2.1")

#### Activitat 2.2
Modifica el codi de l’anterior activitat per a que es puga passar per línia de comandaments el títol i el text del botó.

```py
python3 activitat2.2.py "APP" "Text"
```
![activitat2.2](img/activitat2.2.png "Activitat 2.2")

\newpage

## Assignant tamany a les finestres i els components

Amb la funcions **.setFixedSize(amplada, altura)** assignem una mida fixa al component sobre el que l’apliquem. 

Amb **.setMinimumSize(amplada, altura)** i **setMaximumSize(amplada, altura)**, assignem les mides màximes i mínimes, de forma que ni redimensionant amb el ratolí ni amb els botons de maximitzar i minimitzar tindrem la possibilitat d’establir unes dimensions menors o majors de les establides.

# Senyals i ranures (signal & slots)

En l’anterior aplicació hem inclòs un botó, però que no executa ninguna acció al fer clic sobre ell. Necessitem connectar les accions a alguna funcionalitat. En Qt, açò s’aconseguix gràcies a les senyals i les ranures.

Una **senyal** és una notificació emesa pels components quan es produeix un esdeveniment. 

Una **ranura** és el nom que Qt dona als rebedors de senyals. En Python, qualsevol funció pot ser una ranura, simplement connectant-li una senyal. Alguns components Qt tenen unes ranures predefinides, de forma que els pots connectar a les senyals directament.

```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(200, 132))
        self.setWindowTitle(
            "Exemple senyal 1")

        pybutton = QPushButton('Clic', self)
        
        #Connectem la senyal clicked a la ranura button_pressed
        pybutton.clicked.connect(self.button_pressed) 

        pybutton.resize(100, 32)
        pybutton.move(50, 50)

    def button_pressed(self):
        print('Clic rebut!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
```

\newpage

## Canviem la interfície

El següent exemple canvia el títol de l'aplicació al fer clic sobre le botó.

```py
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

import sys
from random import choice

window_titles = [
    'La meua aplicació',
    'La meua aplicació',
    'Què passa?',
    'Què passa?',
    'Alguna cosa no va bé',
    'Alguna cosa no va bé',
    'Puuuuuum!!'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_title = 0
        self.n_times_clicked = 0

        self.setWindowTitle("La meua aplicació")

        self.button = QPushButton("Apreta'm!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.n_title = self.n_title + 1
        new_window_title = window_titles[self.n_title]
        print("Clic. Establint el títol:  {}".format(new_window_title))
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Títol canviat: %s" % window_title)

        if window_title == 'Puuuuuum!!':
            self.button.setDisabled(True)
            self.button.setText('Puuuuum!!')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
```

1. Tingues en compte que l'event *.windowTitleChanged* no es llança sempre, sols quan el títol canvia realment, però no al assignar-li el mateix.
2. Observeu com som capaços d’encadenar les coses mitjançant senyals. Una cosa que passa (clic al botó) pot desencadenar que passen altres coses. Aquests efectes posteriors no necessiten saber què els ha causat, sinó que s'executen com a  conseqüència de regles senzilles. Aquest desacoblament dels efectes dels seus desencadenants és un dels conceptes clau que cal entendre en la creació d'aplicacions GUI.


\newpage

# Components (Qt Widgets)

Qt conté multitud de components disponibles i, a més, et permet crear els teus propis components. El components anirem estudiant-los al llarg de tot el curs, segons les nostres necessitats.

## QLabel

El compoenent QLabel és simplement una etiqueta, normalment ocupa una línia. Al seu constructor es rep una cadena de text. També podem utilitzar *.setText()* per canviar-lo.

Exemple:

```py
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, text="Hola"):
        super().__init__()

        self.setWindowTitle("La meua app")

        widget = QLabel(text)
        font = widget.font() # Objecte per a configurar les fonts
        font.setPointSize(80) # Tamany de font
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Centrat horitzontalment i verticalment

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

if(len(sys.argv) == 2):
    window = MainWindow(sys.argv[1])
else:
    window = MainWindow()
window.show()

app.exec_()
```

\newpage

| Flag            | Comportament                    |
| --------------- | ------------------------------- |
| Qt.AlignLeft    | Aliniar a l'esquerra.           |
| Qt.AlignRight   | Aliniar a la dreta.             |
| Qt.AlignHCenter | Centra horitzontalment.         |
| Qt.AlignJustify | Justificat a l'espai disponible |

| Flag            | Comportament          |
| --------------- | --------------------- |
| Qt.AlignTop     | Aliniar dalt.         |
| Qt.AlignBottom  | Aliniar baix.         |
| Qt.AlignVCenter | Centrar verticalment. |

Podem combinar les aliniacions amb |.

```py
top_left = Qt.AlignLeft | Qt.AlignTop
```

Per a combinar tant horitzontalment com verticalment podem utilitzar *Qt.AlignCenter*.

### Activitat 2.3 (entregable)

Fes la calculadora, esta vegada de forma gràfica.

\newpage

# Layouts (esquemes de disseny)

Normalment una aplicació conté més d'un component, per això utilitzem els *layouts* per a organitzar-los sobre la interfície. 
Els components s'organitzen sobre el *layout* seguint un model semblant al model de caixes en components *inline* de les pàgines web, és a dir, aniran situant-se un al costat de l'altre o un dalt de l'altre fins ocupar tot l'espai disponible.

Utilitzarem les classes següents per definir els *layouts*.

| Layout         | Behaviour                        |
| -------------- | -------------------------------- |
| QHBoxLayout    | Esquema horitzontal              |
| QVBoxLayout    | Esquema vertical                 |
| QGridLayout    | Esquema en graella               |
| QStackedLayout | Esquema apilat, uns sobre altres |

## Utilització de layouts

Els passos que seguirem per a agregar un o diversos components a l'aplicació mitjançant *layouts* serà:
1. Creem el component principal.
2. Creem l'objecte layout que ens interesse.
3. Afegim els components als *layouts* utilitzant el mètode \<\<layout\>\>.**addWidget(\<\<component\>\>)**. En cas de ser un *QGridLayout*, haurem de passar-li fila i columna **\<\<layout\>\>.addWidget(\<\<component\>\>, fila, columna)**.
4. Assignem el *layout* al component principal.

En cas d'utilitzar un QStackedLayout, podem fer visible (sols un) o invisibles els components amb **\<\<stacked_layout\>\>.setCurrentIndex(\<\<enter>>)**. L'índex assignat a cada component ve determinat per l'ordre en què s'han assignat al *layout*.

~~~py
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Creem layout
        layout = QVBoxLayout()

        # Afegim components al layout
        layout.addWidget(QPushButton("Primer"))
        layout.addWidget(QPushButton("Segon"))
        layout.addWidget(QPushButton("Segon"))

        widget = QWidget()

        # Assignem el laytout a la finestra principal
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
~~~

El resultat és el següent:

![exemple_layout_vertical](img/exemple_layout_vertical.png "Exemple layout vertical")

## Nesting layouts (niament)

Els *layouts* es poden niuar per a donar l'aspecte desitjat. Per fer-ho utilitarem el mètode **\<\<layout1\>\>.addLayout(\<\<layout2\>\>)**.

~~~py
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))

        layout1.addLayout(layout2)

        layout1.addWidget(Color("green"))

        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))

        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
~~~

![exemple_niuament_layouts](img/exemple_niuament_layouts.png "Exemple niuament de layouts")

### Activitat 2.4

Millora el codi de la calculadora amb les idees explicades a classe (creació de tots els botons amb while, utilització d'una sola ranura per a tots els botons, herència de components, ...).
Situa tots els components sobre els layouts, de forma que no caldrà indicar-li a l'aplicació on s'han de situar.

### Activitat 2.5

Crea una interfície com la següent:

![exemple_stacked_layout](img/exemple_stacked_layout.png "Exemple de layouts apilats")

Al pulsar sobre els botons, els fons canviarà al color corresponent. Utilitzeu la classe Color que està al moodle.

### Activitat 2.6

Busca a la documentació de Qt com es crea un component amb pestanyes. Crea una aplicació on a cada pestanya li corresponga la informació dels següents usuaris:

Usuari1: Pedro
DNI: 00000000A

Usuari2: Pablo
DNI: 11111111B

Usuari1: Juan
DNI: 22222222C

Usuari1: Maria
DNI: 33333333D

Per a la informació dels usuaris, crea un component UserInformation.

# Menús, barres de ferramentes i barres d'estat.

En esta secció veurem com afegir menús, barres de ferramentes i barres d'estat a les nostres aplicacions. A partir d'este moment si que utilitzarem QMAinWindows per a crear les nostres aplicacions, no ho farem heredant de QWidget.

## QAction

Abans de començar a afegir elements a les aplicacions, ens fixarem en la calsse QAction. Els objectes QAction s'utilitzen per a executar el mateix codi, ja siga amb l'entrada d'un menú, el botó d'una barra de ferramentes o un mètode abreviat. Per exemple, per a Copiar un fragment de text en *LibreOffice Writer* tenim la possibilitat de fer-ho amb el menú Editar -> Copiar, fent clic a l'icona corresponent a la barra de ferramentes estàndar o utilitzant Ctrl + C. 

## Barres de ferramentes

Per a afegir una barra de ferramentes a la nostra aplicació seguim els següents passos:
1. Creem un component **QToolBar()**.
2. Afegim el component a la finestra principal amb **.addToolBar()**.

### Botons a les barres de ferramentes

Si volem afegir un botó a la barra de ferramentes, farem ús d'un QAction:
1. Declarem un **QAction** i li passem el parent
2. Li podem definir un estat per a la barra d'estat amb **setStatusTip**.
3. Li connectem la ranura a l'event **triggered** del QAction.
4. Afegim el QAction a la barra de ferramentes.
5. Insertem una barra d'estat amb **self.setStatusBar(QStatusBar(self))**
6. Podem fer ús de **.setCheckable(True)**, per a saber si el botó està apretat o no.

Quedaria així el codi:

~~~py
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStatusBar, QAction, QApplication, QLabel, QMainWindow, QToolBar


# tag::MainWindow[]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App amb QMainWindow")

        self.label = QLabel("Hola!")
        self.label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.label)

        toolbar = QToolBar("La meua barra de ferramentes")
        self.addToolBar(toolbar)

        button_action = QAction("El meu botó", self)
        button_action.setStatusTip("Este és el teu botó")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, checked):
        if checked:
            self.label.setText("Botó apretat")
        else:
            self.label.setText("Botó no apretat")

# end::MainWindow[]


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
~~~

### Canviant l'aspecte dels botons

Fins ara l'estil dels botons que hem utilitzat eren textos. Però podem utilitzar icones, textos o combinacions d'estos elements.

| Flag                        | Comportament          |
| --------------------------- | --------------------- |
| Qt.ToolButtonIconOnly       | Icona sols, no text   |
| Qt.ToolButtonTextOnly       | Text sols, no icona   |
| Qt.ToolButtonTextBesideIcon | Icona i textal costat |
| Qt.ToolButtonTextUnderIcon  | Icona i text,baix     |
| Qt.ToolButtonFollowStyle    | Estil del sistema     |







