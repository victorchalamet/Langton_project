""" Module de traitement des données """
import numpy as np

class AntStat:
    """ Récuperation et traitement des données """

    def __init__(self, n):
        """ Initialise chaque tableaux de données """
        self.data = np.zeros(shape = (n,2)) # tableau de la position a chaque instant
        self.r2_moy = np.zeros(shape = n) # tableau de la distance au carr� �  chaque instant
        self.r4_moy = np.zeros(shape = n) # tableau de la distance puissance 4 �  chaque instant
        self.nb_traj = 0

    def add_data(self, data):
        """ Ajoute toutes les données """
        data_origine = data - data[0] # met les positions en (0,0) pour le calcul des distances
        r2 = np.linalg.norm(data_origine, axis=1)**2
        self.r2_moy = self.r2_moy + r2
        self.r4_moy = self.r4_moy + np.power(r2, 2)
        self.nb_traj += 1

    def get_stat(self):
        """ Renvoie les données traitées """
        r2moy = self.r2_moy / self.nb_traj
        r2var = self.r4_moy / self.nb_traj - r2moy ** 2
        return (r2moy+1e-14), np.sqrt(r2var+1e-12)

def coeffdir(x,y):
    """ Fonction qui renvoie le coef dir et le coef de corr d'une regression lineaire """
    varx = (x*x).mean() - (x.mean())**2
    vary = (y*y).mean() - (y.mean())**2
    covxy = (x*y).mean() - x.mean()*y.mean()
    a = covxy / varx
    R = covxy / np.sqrt(varx*vary)
    return a, R