class Gobelet:
    
    def __init__(self, nb_des) -> None:
        
        self.valeur = 0
        self.des = nb_des
        
    @property
    def valeur(self):
        return self._valeur
    
    @valeur.setter
    def valeur(self, valeur):
        self._valeur = valeur
        
    @property
    def des(self):
        return self._des
    
    @nom.setter
    def des(self, des):
        self._des= des   
        
    
        
    def get_valeur(self):
        
    def lancer(self):
        
    return
        
    def afficher_score(self):
        
        print(f"Votre dernier socre est: {self.valeur}")
