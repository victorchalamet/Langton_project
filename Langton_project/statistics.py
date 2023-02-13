""" Data processing module """
import numpy as np

class AntStat:
    """ Data collection and processing """

    def __init__(self, n):
        """ Initialize each data array """
        self.data = np.zeros(shape = (n,2)) # array of the position at each moment
        self.r2_mean = np.zeros(shape = n) # array of the squared distance at each instant
        self.r4_mean = np.zeros(shape = n) # array of the distance to the power of four at each instant
        self.nb_traj = 0

    def add_data(self, data):
        """ Add all data"""
        data_origin = data - data[0] # puts the positions at (0,0) for the calculation of the distances
        r2 = np.linalg.norm(data_origin, axis=1)**2
        self.r2_mean = self.r2_mean + r2
        self.r4_mean = self.r4_mean + np.power(r2, 2)
        self.nb_traj += 1

    def get_stat(self):
        """ Returns processed data """
        r2moy = self.r2_mean / self.nb_traj
        r2var = self.r4_mean / self.nb_traj - r2moy ** 2
        return (r2moy+1e-14), np.sqrt(r2var+1e-12)

def coeffdir(x,y):
    """ Function that returns the leading coefficient and the correlation coefficient of a linear regression """
    varx = (x*x).mean() - (x.mean())**2
    vary = (y*y).mean() - (y.mean())**2
    covxy = (x*y).mean() - x.mean()*y.mean()
    a = covxy / varx
    R = covxy / np.sqrt(varx*vary)
    return a, R