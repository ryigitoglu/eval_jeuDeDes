
from random import *


class de :
    def _init_(self):
        self.nombre = 0
        
    def lancer(self):
        self.nombre = randint(1,6)
        print (self.nombre)
        return self.nombre

    
nouveauJeu = de()


class gobelet :
    tableau = [nouveauJeu.lancer(),nouveauJeu.lancer(),nouveauJeu.lancer()]  
    valeur : 0
    des : tableau
    
    def _init_(self, des, valeur, nbr_des = 0):
        self.nbr_des = nbr_des
    def get_valeur(self):
        return self.valeur
    def lancer(self):
        valeur=+1
    def afficher_score():
        return