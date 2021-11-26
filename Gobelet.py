from De import De


class Gobelet:
    nouveauJeu = De()
    tableau = [nouveauJeu.lancer(),nouveauJeu.lancer(),nouveauJeu.lancer()]  
    valeur : 0
    des : tableau
    
    def __init__(self, nb_des):
        
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
    
    @des.setter
    def des(self, des):
        self._des= des   
        
    
        
    def get_valeur(self):
        return self.valeur
    def lancer(self):
        valeur=+1
        
    def afficher_score(self):
        
        print(f"Votre dernier socre est: {self.valeur}")
