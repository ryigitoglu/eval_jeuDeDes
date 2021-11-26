from Partie import Partie

class Joueur:
    
    def __init__(self, nom) -> None:
        self.nom = str(input("Veuillez saisir votre nom : "))
        self.score = 0
        
        
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        self._nom=nom
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
        
    def get_nom(self):
        return self.nom
    
    def get_score(self):
        return self.score
    
    def jouer(self, gobelet):
        return
        
        
    def afficher_score(self):
        
        print(f"Votre socre est: {self.score}")
    