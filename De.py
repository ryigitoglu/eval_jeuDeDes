from random import randint
import random 
# Importe de la classe random pour la méthode lancer()

class De:
    
    def __init__(self):
        
        self.valeur = random.randint(1,6)
        
    @property
    def valeur(self):
        return self._valeur
    
    @valeur.setter
    def valeur(self, valeur):
        self._valeur = valeur      
    

    # Renvoie la valeur du dè
    def get_valeur(self):
        return self.valeur
    
    # Change la valeur du dè grace à la méthode randint
    def lancer(self):
        self.valeur = random.randint(1,6)
