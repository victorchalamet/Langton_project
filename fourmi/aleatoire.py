""" Module gérant les initialisations aléatoire """
import random

def orientation_aleatoire(donnees_fourmis):
    """ Donne une orientation aléatoire à chaque fourmi """
    Liste_ori = [0,90,180,270]
    for i in range(len(donnees_fourmis)):
        donnees_fourmis[i]['direction_init'] = random.choice(Liste_ori)

def position_aleatoire(donnees_fourmis, screen_x, screen_y):
    """ Donne une position aléatoire à chaque fourmi """
    for i in range(len(donnees_fourmis)):
            donnees_fourmis[i]['x_init'] = random.randint(-screen_x//10, screen_x//10)
            donnees_fourmis[i]['y_init'] = random.randint(-screen_y//10, screen_y//10)

def creation_dico(nb_ant, comportement):
    """ Crée un dictionnaire avec les premières info des fourmis """
    donnees_fourmi_dico = []
    for ant in range(nb_ant):
        donnees_fourmi_dico.append({}) # crée le dictionnaire de chaque fourmi
        donnees_fourmi_dico[ant]['id'] = ant
        donnees_fourmi_dico[ant]['comportement'] = comportement
        donnees_fourmi_dico[ant]['direction_init'] = 0
    return donnees_fourmi_dico

def initialisation_aleatoire(nb_ant, comportement, screen_x=1000, screen_y=1000):
    """ Renvoie un dictionnaire avec toutes les informations utiles à la
    définition des fourmis"""
    donnees_fourmis = creation_dico(nb_ant, comportement)
    position_aleatoire(donnees_fourmis, screen_x, screen_y)
    orientation_aleatoire(donnees_fourmis)
    return donnees_fourmis
