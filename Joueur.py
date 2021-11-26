from Partie import Partie
# Import de la classe Partie pour récuperer l'attribut Gobelet
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
        
        # Renvoie le nom du joueur
    def get_nom(self): 
        return self.nom
        # Revoie le score du joueur
    def get_score(self):
        return self.score
        # Prend en paramètre le gobelet de la classe Partie
    def jouer(self, gobelet):
        return
        
        # Affiche le score du joueur sur la console
    def afficher_score(self):
        
        print(f"Votre socre est: {self.score}")
    