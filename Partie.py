


class Partie:


   def _init_(self, nb_tour, nbr_des):
        self.nb_tour = nb_tour
        self.nbr_des = nbr_des
    
    
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
    
    
    # Initilise le nombre de joueurs dans la partie
    def initialiser(self):
        return
    # Démarre la partie
    def lancer(self):
        return
        
    # compare les scores des joueurs et affiche le gagnant
    def afficher_gagnant(self):