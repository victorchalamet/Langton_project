""" Module for initializing the parameters of each ant """
import random

def random_color(ants_data, r_color):
    """ Give a random color to each ant """
    if r_color:
        rbyte = lambda: random.randint(0, 255)
        for i in range(len(ants_data)):
            ants_data[i]['color'] = ('#%02X%02X%02X' % (rbyte(), rbyte(), rbyte()))
    else:
        for i in range(len(ants_data)):   
            ants_data[i]['color'] = ("black")
          
def random_orientation(ants_data):
    """ Gives a random orientation to each ant """
    orientation_list = [0,90,180,270]
    for i in range(len(ants_data)):
        ants_data[i]['direction_init'] = random.choice(orientation_list)

def random_position(ants_data, screen_x, screen_y):
    """ Gives a random position to each ant """
    for i in range(len(ants_data)):
            ants_data[i]['x_init'] = random.randint(-screen_x//10, screen_x//10)
            ants_data[i]['y_init'] = random.randint(-screen_y//10, screen_y//10)

def dic_conversion(ants_data, nb_ant):
    """ Convert a list to an ant info dictionary """
    dic_ants_data = []
    for ant in range(nb_ant):
        dic_ants_data.append({}) # create the dictionary of each ant
        dic_ants_data[ant]['id'] = ant
        dic_ants_data[ant]['direction_init'] = ants_data[ant][2]
        dic_ants_data[ant]['x_init'] = ants_data[ant][0]
        dic_ants_data[ant]['y_init'] = ants_data[ant][1]
    return dic_ants_data

def random_initialization(ants_data, nb_ant, r_color, r_position, r_orientation, screen_x, screen_y): 
    """ Returns a dictionary with all the useful information for the definition of ants """        
    ants_data = dic_conversion(ants_data, nb_ant)
    random_color(ants_data, r_color)
    if not r_position and not r_orientation:
        return ants_data
    elif r_position and not r_orientation:
        random_position(ants_data, screen_x, screen_y)
        return ants_data
    elif r_orientation and not r_position:
        random_orientation(ants_data)
        return ants_data
    else:
        random_position(ants_data, screen_x, screen_y)
        random_orientation(ants_data)
        return ants_data