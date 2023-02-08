""" Module de définition des fourmi et de leur comportement """
import random
import numpy as np

""" Variable global """
visited_global = {}
current_position = {}
visited_noir = {}
orientation_blanc = [(1,0), (0,-1), (-1,0), (0,1)]
orientation_noir = [(-1,0), (0,1), (1,0), (0,-1)]

class Ant:
    """ Création d'une fourmi sur l'ecran """
    global visited_global
    global current_position
    global visited_noir

    def __init__(self, donnees_fourmis):
        self.visited_local = []
        self.id_fourmi = donnees_fourmis['id']
        self.x_initial= donnees_fourmis['x_init']
        self.y_initial = donnees_fourmis['y_init']
        self.comportement = donnees_fourmis['comportement']
        self.position = np.array([self.x_initial, self.y_initial])
        self.direction_initiale = donnees_fourmis['direction_init'] // 90
        self.direction = self.direction_initiale

    def avancer(self, orientation):
        """ Fait avancer la fourmi """
        self.position = self.position + orientation[self.direction]

    def tourner_droite(self):
        """ Fait tourner la fourmi de 90° vers la droite """
        self.direction = (self.direction+1) % 4

    def tourner_gauche(self):
        """ Fait tourner la fourmi de 90° vers la gauche """
        self.direction = (self.direction+3) % 4
        
    def mvt_comportement(self, x, y, tourner, orientation):
        """ Définie plusieurs comportement d'une fourmi par rapport a des
        fourmis adjacentes """
        global current_position
        tout_droit = [(0,1), (1,0), (0,-1), (-1,0)]
        prochaine_position = tout_droit[self.direction]+self.position
        if self.comportement == 1:
            # avance tout droit
            if tuple(prochaine_position) not in current_position.values():
                self.avancer(tout_droit)
        elif self.comportement == 2:
            # ignore
            tourner
            self.avancer(orientation)
        elif self.comportement == 3:
            # reste immobile
            pass
        else:
            print("Ce comportement n'est pas définie")
    
    def prochaine_position(self,orientation):
        return orientation[self.direction]+self.position
    
    def new_position(self, noise_ratio):
        """ Définie comment se comporte une fourmi et stock les données """
        global visited_global
        global current_position
        global orientation_noir
        global orientation_blanc
        (x,y) = self.position
        if (x,y) not in visited_global:
            # case non visitée
            if random.random() < noise_ratio:
                prochaine_position = (self.prochaine_position(orientation_blanc),
                                      orientation_blanc,self.tourner_droite)
            else:
                prochaine_position = (self.prochaine_position(orientation_noir),
                                      orientation_noir,self.tourner_gauche)
            if tuple(prochaine_position[0]) in current_position.values():
                # autre fourmi sur la prochaine case
                self.mvt_comportement(x,y,prochaine_position[2],prochaine_position[1])
            else:
                prochaine_position[2]()
                self.position = prochaine_position[0]
            visited_global[(x,y)] = self.id_fourmi+1
            current_position[self.id_fourmi] = tuple(prochaine_position[0])
            self.visited_local.append((x,y))
        elif (x,y) not in visited_noir:
            # case noir visitée
            prochaine_position = self.prochaine_position(orientation_blanc)
            if tuple(prochaine_position) in current_position.values():
                # autre fourmi sur la prochaine case
                self.mvt_comportement(x,y,self.tourner_gauche(),orientation_blanc)
            else:
                self.tourner_droite()
                self.position = prochaine_position
            visited_noir[(x,y)] = self.id_fourmi
            current_position[self.id_fourmi] = tuple(prochaine_position)
            self.visited_local.append((x,y))
        else:
            # case blanche visitée
            prochaine_position = self.prochaine_position(orientation_noir)
            if tuple(prochaine_position) in current_position.values():
                # autre fourmi sur la prochaine case
                self.mvt_comportement(x,y,self.tourner_droite(),orientation_noir)
            else:
                self.tourner_gauche()
                self.position = prochaine_position
            del visited_noir[(x,y)]             
            current_position[self.id_fourmi] = tuple(prochaine_position)
            self.visited_local.append((x,y))

    def get_data(self):
        """ Transforme nos données en array """
        return np.asarray(self.visited_local, dtype=int)

def initialisation(donnees_fourmis):
    global visited_global
    global current_position
    """ Avec données_fourmis un dictionnaire contenant les infos de chaque
    fourmis: (x_init, y_init, direction_init, couleur, id, comportement) """
    n_fourmis = len(donnees_fourmis)
    visited_global = {}
    current_position = {}
    liste_ant = [0]*n_fourmis
    for numero_fourmi in range(n_fourmis):
        ant = Ant(donnees_fourmis[numero_fourmi])
        x = round(donnees_fourmis[numero_fourmi]['x_init'])
        y = round(donnees_fourmis[numero_fourmi]['y_init'])
        current_position[donnees_fourmis[numero_fourmi]['id']] = (x,y)
        liste_ant[numero_fourmi] = ant
    return liste_ant

def move(liste_ant, steps, noise_ratio):
    """ Fait bouger toutes les fourmis définies """
    for step in range(steps):
        for ant in liste_ant:
            ant.new_position(noise_ratio)
    return liste_ant