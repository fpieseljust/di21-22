# Finestra de login

Heu de crear una aplicació que al ser llançada mostre una finestra de login, demanant a l'usuari el nom d'usuari i la contrasenya:

- En cas d'introduir 'admin', '1234', mostrarà la finstra principal de l'aplicació, on s'indicarà (a l'status bar i amb un QLabel com a CentralWidget) que s'està loguejat amb l'usuari admin. 
- Si s'introdueix 'user', '1234', es mostrarà que s'està loguejat com a usuari estàndar. 
- Si l'usuari o la contrasenya són incorrectes, llanceu un avís informant a l'usuari.

Poseu una opció al menú de la finestra principal per a fer logout, de forma que ens torne a mostrar la finestra de login i una altra opció per tancar l'aplicació. Si es tanca qualsevol de les finestres, l'aplicació acabarà la seua execució.