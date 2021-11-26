from Gobelet import Gobelet


class Partie:


    def __init__(self, gobelet):
        self.joueurs = (1,2)
        self.nb_tours = 3
        self.gobelet = gobelet
    
    
    @property
    def joueurs(self):
        return self._joueurs
    
    @nb_tours.setter
    def joueurs(self,):
        self._joueurs = (1,2)
        
    
    @property
    def nb_tours(self):
        return self._nb_tours
    
    @nb_tours.setter
    def nb_tours(self, tours):
        self._nb_tours= tours
        
    @property
    def gobelet(self):
        return self._gobelet
    
    @gobelet.setter
    def gobelet(self, gobelet):
        self._gobelet=gobelet
    
    
    def initialiser(self):
        return
        
    def lancer(self):
        return
        
        
    def afficher_gagnant(self):