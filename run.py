from ant import statistics as stat
from ant import main
from ant import random
from ant import save
import matplotlib.pyplot as plt
import time
import sys
import numpy as np
from scipy.optimize import curve_fit

""" System settings """
nb_ant = int(sys.argv[1])
nb_traj = int(sys.argv[2])
steps = int(sys.argv[3])
noise_ratio = float(sys.argv[4])
nb_iteration = int(sys.argv[5])
behavior = int(sys.argv[6])
t_init = time.time()
dir_list = []

def script(behavior=3, nb_ant=1):
    # Default settings: still, one ant
    """ Launch all iterations """
    global noise_ratio
    global dir_list
    noise = []
    law_parameter = []
    for iteration in range(1, nb_iteration+1):
        if noise_ratio != 0:
            if nb_iteration != 1:
                noise_ratio = iteration / (50*nb_iteration)
        t0 = time.time() # initialize the calculation time
        statistics = stat.AntStat(steps) # initialize arrays
        for traj in range(nb_traj):
            ants_data = random.random_initialization(nb_ant=nb_ant, behavior=behavior)
            ant_list = main.initialisation(ants_data)
            final_ant_list = main.move(ant_list, steps=steps, noise_ratio=noise_ratio)
            for ant in final_ant_list:
                data_ant = ant.get_data()
                statistics.add_data(data_ant)
        
        """ Data recovery """
        r2_mean, r2_var = statistics.get_stat()
        
        """ Creating results for constant noise as a graph """
        times = list(range(1, steps+1))
        reduced_time = list(range(int(steps*0.09), steps+1)) # removes part of the data because useless
        
        def power_law(x, a, b):
            """ Regression function """
            return a * np.power(x, b)
        
        popt, pcov = curve_fit(power_law, reduced_time, r2_mean[-len(reduced_time):]) # optimal parameters
        
        plt.subplot(211)
        plt.title(f"Nb of ant: {nb_ant}, Nb of traj: {nb_traj}, Nb of steps: {steps}, Noise ratio: {round(noise_ratio, 4)}",
                  fontsize = 8)
        plt.ylabel("average squared distance",fontsize = 7)
        plt.loglog(times[10:], r2_mean[10:])
        plt.grid()
        regress = plt.plot(reduced_time, power_law(reduced_time, *popt), label='power law', color="red")# regression
        plt.legend(regress, [f"{pcov}"], loc = 'lower right')
        
        plt.subplot(212)
        plt.xlabel("Time (in steps)",fontsize = 10)
        plt.ylabel("mean squared distance variance",fontsize = 7)
        plt.loglog(times[10:], r2_var[10:])
        plt.grid()
        
        save.save_plot("Pictures", iteration, nb_ant) # Saves the data
        save.save_data("Position", r2_mean, iteration, nb_ant) # Saves the data
        
        """ Creation of the graph of the evolution of the slope of the mean squared distance over time """
        sublist_len = 500
        init = len(reduced_time)//sublist_len
        leading_coefficient_list = [0 for i in range(init)]
        times_list = [0 for i in range(init)]
        correlation_coefficient_list = [0 for i in range(init)]
        for i in range(init):
            isolated_time = np.array(reduced_time[i*sublist_len : (i+1)*sublist_len]) # time's sublist
            isolated_r2 = r2_mean[i*sublist_len : (i+1)*sublist_len] # r2_mean's sublist
            coef_dir, corr_coef = stat.coeffdir(np.log(isolated_time), np.log(isolated_r2))
            
            leading_coefficient_list[i] = coef_dir
            times_list[i] = isolated_time.mean()
            correlation_coefficient_list[i] = corr_coef
        
        plt.subplot(211)
        plt.title(f"Regression leading coefficient: {round(popt[1], 3)}")
        plt.ylabel("Leading coefficient", fontsize=10)
        plt.plot(times_list[1:], leading_coefficient_list[1:])
        plt.grid()
        
        plt.subplot(212)
        plt.ylabel("Correlation coefficient")
        plt.xlabel("Time (in steps)", fontsize=10)
        plt.scatter(times_list[1:], correlation_coefficient_list[1:], marker='+')
        plt.grid()
        
        save.save_plot("Coef", iteration, nb_ant) # Saves the data
        
        noise.append(noise_ratio)
        law_parameter.append(popt[1])

        dir_list.append(popt[1])
        print(f"Calculation time: {time.time()-t0}")
    
    if nb_iteration != 1:
        # do not draw unnecessary graphs
        """ Creation of the graph of the parameter of the law depending on the noise """
        plt.plot(noise, law_parameter)
        plt.title(f"Nb of ant: {nb_ant}, Nb of traj: {nb_traj}, Nb of steps: {steps}, Nb of iteration: {nb_iteration}",fontsize = 8)
        plt.xlabel("Noise", fontsize = 7)
        plt.grid()
        plt.ylabel("Power law parameter", fontsize = 7)
        
        save.save_plot("Results/noise", iteration, nb_ant) # Saves the data

""" Loops definition """
if __name__ == '__main__':
    if nb_ant != 1:
        for nb_ants in range(2,10,3):
            script(behavior, nb_ant=nb_ants)
    else:
        script(behavior, nb_ant)

""" Results analysis graph """
if nb_ant != 1 and nb_iteration == 1:
    nb_ant_list = [i for i in range(2,10,3)]
    plt.title(f"Nb of traj: {nb_traj}, Nb of steps: {steps}, Noise ratio: {round(noise_ratio, 4)}", fontsize=8)
    plt.xlabel("Number of ant", fontsize=10)
    plt.ylabel("Power law parameter", fontsize=7)
    plt.grid()
    plt.plot(nb_ant_list, dir_list)
    
    save.save_plot("Results/ant", iteration=1, nb_ant=nb_ant) # Saves the data
    
print(f"Total calculation time: {time.time()-t_init}")