""" Data and results saving module """
import os
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import sys

""" Global variable """
nb_ant = int(sys.argv[1])
nb_traj = int(sys.argv[2])
steps = int(sys.argv[3])
noise_ratio = float(sys.argv[4])
nb_iteration = int(sys.argv[5])
behavior = int(sys.argv[6])
current_date = str(datetime.now()).split()[0].split('-')

def save_plot(directory, iteration, nb_ants):
    """ Save the graphics by creating the directory if it does not exist """
    global noise_ratio
    if noise_ratio != 0:
        if nb_iteration != 1:
            noise_ratio = iteration / (50*nb_iteration)
    file_name = f"ant_{f'{current_date[0][2:]}{current_date[1]}{current_date[2]}'}_{nb_ants}_{nb_traj}_{steps}_{behave(behavior)}_{round(noise_ratio, 4)}-0.png"
    path = f"{directory}/{current_date[1]}-{current_date[2]}"
    if not os.path.isdir(path):
        # if the directory doesn't exist
        os.makedirs(path)
        plt.savefig(f"{path}/{file_name}", format='png')
    else:
        if not os.path.exists(f"{path}/{file_name}"):
            # if the file name doesn't exist
            plt.savefig(f"{path}/{file_name}", format='png')
        else:
            while os.path.exists(f"{path}/{file_name}"):
                # create a new file name if it already exist
                file_name = f"{file_name.split('-')[0]}-{str(int(file_name.split('-')[1].split('.')[0])+1)}.png"
            plt.savefig(f"{path}/{file_name}", format='png')
    plt.close()

def save_data(directory, data, iteration, nb_ants):
    """ Save position arrays by creating the directory if it does not exist """
    global noise_ratio
    if noise_ratio != 0:
        if nb_iteration != 1:
            noise_ratio = iteration / (50*nb_iteration)
    file_name = f"ant_{f'{current_date[0][2:]}{current_date[1]}{current_date[2]}'}_{nb_ants}_{nb_traj}_{steps}_{behave(behavior)}_{round(noise_ratio, 4)}-0.csv"
    path = f"{directory}/{current_date[1]}-{current_date[2]}"
    if not os.path.isdir(path):
        # if the directory doesn't exist
        os.makedirs(path)
        np.savetxt(f"{path}/{file_name}", data, delimiter = '  ')
    else:
        if not os.path.exists(f"{path}/{file_name}"):
            # if the file name doesn't exist
            np.savetxt(f"{path}/{file_name}", data, delimiter = '  ')
        else:
            while os.path.exists(f"{path}/{file_name}"):
                # create a new file name if it already exist
                file_name = f"{file_name.split('-')[0]}-{str(int(file_name.split('-')[1].split('.')[0])+1)}.csv"
            np.savetxt(f"{path}/{file_name}", data, delimiter='  ')

def behave(behavior):
    if behavior == 1:
        return "straightahead"
    if behavior == 2:
        return "ignore"
    if behavior == 3:
        return "still"