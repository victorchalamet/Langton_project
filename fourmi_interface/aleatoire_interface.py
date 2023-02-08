""" Module d'initialisation des paramètres de chaque fourmis """
import random

def couleur_aleatoire(donnees_fourmis, ale_color):
    """ Donne une couleur aléatoire à chaque fourmi """
    if ale_color:
        rbyte = lambda: random.randint(0, 255)
        for i in range(len(donnees_fourmis)):
            donnees_fourmis[i]['couleur'] = ('#%02X%02X%02X' % (rbyte(), rbyte(), rbyte()))
    else:
        for i in range(len(donnees_fourmis)):   
            donnees_fourmis[i]['couleur'] = ("black")
          
def orientation_aleatoire(donnees_fourmis):
    """ Donne une orientation aléatoire Ã  chaque fourmi """
    Liste_ori = [0,90,180,270]
    for i in range(len(donnees_fourmis)):
        donnees_fourmis[i]['direction_init'] = random.choice(Liste_ori)

def position_aleatoire(donnees_fourmis, screen_x, screen_y):
    """ Donne une position aléatoire à chaque fourmi """
    for i in range(len(donnees_fourmis)):
            donnees_fourmis[i]['x_init'] = random.randint(-screen_x//10, screen_x//10)
            donnees_fourmis[i]['y_init'] = random.randint(-screen_y//10, screen_y//10)

def conversion_dico(donnees_fourmis, nb_ant):
    """ Convertie une liste en un dico des infos de la fourmi """
    donnees_fourmi_dico = []
    for ant in range(nb_ant):
        donnees_fourmi_dico.append({}) # crÃ©e le dictionnaire de chaque fourmi
        donnees_fourmi_dico[ant]['id'] = ant
        donnees_fourmi_dico[ant]['direction_init'] = donnees_fourmis[ant][2]
        donnees_fourmi_dico[ant]['x_init'] = donnees_fourmis[ant][0]
        donnees_fourmi_dico[ant]['y_init'] = donnees_fourmis[ant][1]
    return donnees_fourmi_dico

def initialisation_aleatoire(donnees_fourmis, nb_ant, ale_color, varpos, varori,
                             screen_x, screen_y): 
    """ Renvoie un dictionnaire avec toutes les informations utiles à la
    définition des fourmis"""        
    donnees_fourmis = conversion_dico(donnees_fourmis, nb_ant)
    couleur_aleatoire(donnees_fourmis, ale_color)
    if not varpos and not varori:
        return donnees_fourmis
    elif varpos and not varori:
        position_aleatoire(donnees_fourmis, screen_x, screen_y)
        return donnees_fourmis
    elif varori and not varpos:
        orientation_aleatoire(donnees_fourmis)
        return donnees_fourmis
    else:
        position_aleatoire(donnees_fourmis, screen_x, screen_y)
        orientation_aleatoire(donnees_fourmis)
        return donnees_fourmis
