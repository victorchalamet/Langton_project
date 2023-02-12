""" Module managing random initializations """
import random

def random_orientation(ants_data):
    """ Gives a random orientation to each ant """
    direction_list = [0,90,180,270]
    for i in range(len(ants_data)):
        ants_data[i]['init_direction'] = random.choice(direction_list)

def random_position(ants_data, screen_x, screen_y):
    """ Gives a random position to each ant """
    for i in range(len(ants_data)):
            ants_data[i]['x_init'] = random.randint(-screen_x//10, screen_x//10)
            ants_data[i]['y_init'] = random.randint(-screen_y//10, screen_y//10)

def dic_init(nb_ant, behavior):
    """ Create a dictionary with the first informations of the ants """
    ants_data_dic = []
    for ant in range(nb_ant):
        ants_data_dic.append({}) # create the dictionary of each ant
        ants_data_dic[ant]['id'] = ant
        ants_data_dic[ant]['behavior'] = behavior
        ants_data_dic[ant]['init_direction'] = 0
    return ants_data_dic

def random_initialization(nb_ant, behavior, screen_x=1000, screen_y=1000):
    """ Returns a dictionary with all the useful information for the definition of ants """
    ants_data = dic_init(nb_ant, behavior)
    random_position(ants_data, screen_x, screen_y)
    random_orientation(ants_data)
    return ants_data
