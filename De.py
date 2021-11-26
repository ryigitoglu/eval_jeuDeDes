from random import randint 


class De:
    
    def __init__(self):
        
        self.valeur = 0
        
    @property
    def valeur(self):
        return self._valeur
    
    @valeur.setter
    def valeur(self, valeur):
        self._valeur = valeur      
    


    def get_valeur(self, lancerDe):
        return self.valeur
    
    def lancer(self)
