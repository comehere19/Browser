#Importation des packages

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

#FenPrincipale est la fonction principale permettant d'exécuter le code
class FenPrincipale(QMainWindow):
    def __init__(self):
        super(FenPrincipale, self).__init__()
        self.setWindowIcon(QtGui.QIcon('logo.ico')) #code permettant de donner un ico à notre application
        self.navigateur = QWebEngineView()
        self.navigateur.setUrl(QUrl('https://google.com')) #spécifier le site web à afficher par défault lorsqu'on lance le navigateur
        self.setCentralWidget(self.navigateur)
        self.showMaximized()

        #navbar:
        navbar = QToolBar()
        self.addToolBar(navbar)

        #Création des boutons 
        retour_btn = QAction('Before', self)
        retour_btn.triggered.connect(self.navigateur.back)
        navbar.addAction(retour_btn)

        rafraichir_btn = QAction('Refresh', self)
        rafraichir_btn.triggered.connect(self.navigateur.reload)
        navbar.addAction(rafraichir_btn)

        avancer_btn = QAction(' Next', self)
        avancer_btn.triggered.connect(self.navigateur.forward)
        navbar.addAction(avancer_btn)

        accueil_btn = QAction('Home', self)
        accueil_btn.triggered.connect(self.url_accueil)
        navbar.addAction(accueil_btn)

        meteo_btn = QAction('Weather', self)
        meteo_btn.triggered.connect(self.url_meteo)
        navbar.addAction(meteo_btn)

        #Récupération de l'adresse web puis exécution
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigation)
        navbar.addWidget(self.url_bar)

        self.navigateur.urlChanged.connect(self.update_url)

    #fonction permettant 
    def url_accueil(self):
            self.navigateur.setUrl(QUrl('https://google.com'))

    #fonction permettant d'accéder à la visualisation météo 
    def url_meteo(self):
            self.navigateur.setUrl(QUrl('https://weathertec.000webhostapp.com/'))

    #fonction permettant d'avoir l'url 
    def navigation(self):
        url =  self.url_bar.text()
        self.navigateur.setUrl(QUrl(url))

    #fonction permettant de mettre à jour l'url dans la barre de recherche
    def update_url(self, url):
        self.url_bar.setText(url.toString())

    #Création des fonctions


app = QApplication(sys.argv)
QApplication.setApplicationName('Zindor') #code permettant de donner un titre à notre navigateur de recherche
fenetre = FenPrincipale()
app.exec()
