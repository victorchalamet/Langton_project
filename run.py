from fourmi import statistique as stat
from fourmi import creation
from fourmi import aleatoire
from fourmi import save
import matplotlib.pyplot as plt
import time
import sys
import numpy as np
from scipy.optimize import curve_fit

""" Paramètres du système """
nb_fourmi = int(sys.argv[1])
nb_traj = int(sys.argv[2])
steps = int(sys.argv[3])
noise_ratio = float(sys.argv[4])
nb_iteration = int(sys.argv[5])
comportement = int(sys.argv[6])
t_init = time.time()
liste_dir = []

def script(comportement=3, nb_fourmi=1):
    # Paramètre par défaut: immobile, 1 fourmi
    """ Lancement de toutes les itérations """
    global noise_ratio
    global liste_dir
    bruit = []
    parametre_loi = []
    for iteration in range(1, nb_iteration+1):
        if noise_ratio != 0:
            if nb_iteration != 1:
                noise_ratio = iteration / (50*nb_iteration)
        t0 = time.time() # initialisation du temps de calcul
        statistics = stat.AntStat(steps) # initialise les tableaux
        for traj in range(nb_traj):
            donnees_fourmis = aleatoire.initialisation_aleatoire(nb_ant=nb_fourmi,
                                                                 comportement=comportement)
            liste_ant = creation.initialisation(donnees_fourmis)
            liste_ant_final = creation.move(liste_ant, steps=steps, noise_ratio=noise_ratio)
            for ant in liste_ant_final:
                data_ant = ant.get_data()
                statistics.add_data(data_ant)
        
        """ Récupération des données """
        r2_moy, r2_var = statistics.get_stat()
        
        """ Création des résultats pour un bruit constant sous forme de graphe """
        temps = list(range(1, steps+1))
        temps_reduit = list(range(int(steps*0.09), steps+1)) # enlève une partie des donnees car peu intéressantes
        
        def power_law(x, a, b):
            """ Fonction de la régression """
            return a * np.power(x, b)
        
        popt, pcov = curve_fit(power_law, temps_reduit, r2_moy[-len(temps_reduit):]) # paramètres optimaux
        
        plt.subplot(211)
        plt.title(f"Nb de fourmi: {nb_fourmi}, Nb de traj: {nb_traj}, Nb de pas: {steps}, Ratio du bruit: {round(noise_ratio, 4)}",
                  fontsize = 8)
        plt.ylabel("distance au carré moyenne",fontsize = 7)
        plt.loglog(temps[10:], r2_moy[10:])
        plt.grid()
        regress = plt.plot(temps_reduit, power_law(temps_reduit, *popt), label='power law', color="red")# régression
        plt.legend(regress, [f"{pcov}"], loc = 'lower right')
        
        plt.subplot(212)
        plt.xlabel("Time (in steps)",fontsize = 10)
        plt.ylabel("variance de la distance carré moyenne",fontsize = 7)
        plt.loglog(temps[10:], r2_var[10:])
        plt.grid()
        
        save.save_plot("Images", iteration, nb_fourmi) # Sauvegarde des résultats
        save.save_data("Position", r2_moy, iteration, nb_fourmi) # Sauvegarde des résultats
        
        """ Création du graphe de l'évolution de la pente de la distance au
        carré moyenne au cours du temps"""
        taille_sous_liste = 500
        init = len(temps_reduit)//taille_sous_liste
        liste_coef_dir = [0 for i in range(init)]
        liste_temps = [0 for i in range(init)]
        liste_coef_corr = [0 for i in range(init)]
        for i in range(init):
            temps_isole = np.array(temps_reduit[i*taille_sous_liste : (i+1)*taille_sous_liste]) # sous-liste du temps
            r2_isole = r2_moy[i*taille_sous_liste : (i+1)*taille_sous_liste] # sous-liste de r2_moy
            coef_dir, coef_corr = stat.coeffdir(np.log(temps_isole), np.log(r2_isole))
            
            liste_coef_dir[i] = coef_dir
            liste_temps[i] = temps_isole.mean()
            liste_coef_corr[i] = coef_corr
        
        plt.subplot(211)
        plt.title(f"Coef directeur de la régression: {round(popt[1], 3)}")
        plt.ylabel("Coef directeur", fontsize=10)
        plt.plot(liste_temps[1:], liste_coef_dir[1:])
        plt.grid()
        
        plt.subplot(212)
        plt.ylabel("Coef de corrélation")
        plt.xlabel("Time", fontsize=10)
        plt.scatter(liste_temps[1:], liste_coef_corr[1:], marker='+')
        plt.grid()
        
        save.save_plot("Coef", iteration, nb_fourmi) # Sauvegarde des résultats
        
        bruit.append(noise_ratio)
        parametre_loi.append(popt[1])

        liste_dir.append(popt[1])
        print(f"Temps de calcul: {time.time()-t0}")
    
    if nb_iteration != 1:
        # ne trace pas de graphe inutile
        """ Création du graphe paramètre_loi en fonction de bruit """
        plt.plot(bruit, parametre_loi)
        plt.title(f"Nb de fourmi: {nb_fourmi}, Nb de traj: {nb_traj}, Nb de pas: {steps}, Nb d'itération: {nb_iteration}",fontsize = 8)
        plt.xlabel("Bruit", fontsize = 7)
        plt.grid()
        plt.ylabel("Paramètre de la loi de puissance", fontsize = 7)
        
        save.save_plot("Résultats/bruit", iteration, nb_fourmi) # Sauvegarde des résultats

""" Définition des boucles """
if __name__ == '__main__':
    if nb_fourmi != 1:
        for nb_fourmis in range(2,10,3):
            script(comportement, nb_fourmi=nb_fourmis)
    else:
        script(comportement, nb_fourmi)

""" Graphe d'anayse de résultats """
if nb_fourmi != 1:
    liste_nb_fourmi = [i for i in range(2,10,3)]
    plt.title(f"Nb de traj: {nb_traj}, Nb de pas: {steps}, Ratio du bruit: {round(noise_ratio, 4)}",
                fontsize=8)
    plt.xlabel("Nombre de fourmi", fontsize=10)
    plt.ylabel("Paramètre de la loi de puissance", fontsize=7)
    plt.grid()
    plt.plot(liste_nb_fourmi, liste_dir)
    
    save.save_plot("Résultats/fourmi", iteration=1, nb_fourmi=nb_fourmi)
    
print(f"Temps de calcul total: {time.time()-t_init}")