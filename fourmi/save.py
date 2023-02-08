""" Module de sauvegarde des données et résultats """
import os
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import sys

""" Variables global """
nb_fourmi = int(sys.argv[1])
nb_traj = int(sys.argv[2])
steps = int(sys.argv[3])
noise_ratio = float(sys.argv[4])
nb_iteration = int(sys.argv[5])
comportement = int(sys.argv[6])
current_date = str(datetime.now()).split()[0].split('-')

def save_plot(dossier, iteration, nb_fourmi):
    """ Sauvegarde les graphiques en créant le dossier s'il n'existe pas """
    global noise_ratio
    if noise_ratio != 0:
        if nb_iteration != 1:
            noise_ratio = iteration / (50*nb_iteration)
    file_name = f"fourmi_{f'{current_date[0][2:]}{current_date[1]}{current_date[2]}'}_{nb_fourmi}_{nb_traj}_{steps}_{behave(comportement)}_{round(noise_ratio, 4)}-0.png"
    path = f"{dossier}/{current_date[1]}-{current_date[2]}"
    if not os.path.isdir(path):
        os.makedirs(path)
        plt.savefig(f"{path}/{file_name}", format='png')
    else:
        if not os.path.exists(f"{path}/{file_name}"):
            plt.savefig(f"{path}/{file_name}", format='png')
        else:
            while os.path.exists(f"{path}/{file_name}"):
                file_name = f"{file_name.split('-')[0]}-{str(int(file_name.split('-')[1].split('.')[0])+1)}.png"
            plt.savefig(f"{path}/{file_name}", format='png')
    plt.close()

def save_data(dossier, data, iteration, nb_fourmi):
    """ Sauvegarde les array de position en créant le dossier s'il n'existe pas """
    global noise_ratio
    if noise_ratio != 0:
        if nb_iteration != 1:
            noise_ratio = iteration / (50*nb_iteration)
    file_name = f"fourmi_{f'{current_date[0][2:]}{current_date[1]}{current_date[2]}'}_{nb_fourmi}_{nb_traj}_{steps}_{behave(comportement)}_{round(noise_ratio, 4)}-0.csv"
    path = f"{dossier}/{current_date[1]}-{current_date[2]}"
    if not os.path.isdir(path):
        os.makedirs(path)
        np.savetxt(f"{path}/{file_name}", data, delimiter = '  ')
    else:
        if not os.path.exists(f"{path}/{file_name}"):
            np.savetxt(f"{path}/{file_name}", data, delimiter = '  ')
        else:
            while os.path.exists(f"{path}/{file_name}"):
                file_name = f"{file_name.split('-')[0]}-{str(int(file_name.split('-')[1].split('.')[0])+1)}.csv"
            np.savetxt(f"{path}/{file_name}", data, delimiter='  ')

def behave(comportement):
    if comportement == 1:
        return "toutdroit"
    if comportement == 2:
        return "ignore"
    if comportement == 3:
        return "immobile"