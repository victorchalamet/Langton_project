""" Module for defining ants and their behavior """
import random
import numpy as np

""" Global variable """
visited_global = {}
current_position = {}
visited_black = {}
orientation_white = [(1,0), (0,-1), (-1,0), (0,1)]
orientation_black = [(-1,0), (0,1), (1,0), (0,-1)]

class Ant:
    """ Creation of an ant on the screen"""
    global visited_global
    global current_position
    global visited_black

    def __init__(self, ants_data):
        self.visited_local = []
        self.ant_id = ants_data['id']
        self.x_initial= ants_data['x_init']
        self.y_initial = ants_data['y_init']
        self.behavior = ants_data['behavior']
        self.position = np.array([self.x_initial, self.y_initial])
        self.initial_direction = ants_data['init_direction'] // 90
        self.direction = self.initial_direction

    def advance(self, orientation):
        """ Move the ant """
        self.position = self.position + orientation[self.direction]

    def turn_right(self):
        """ Rotates the ant 90° to the right """
        self.direction = (self.direction+1) % 4

    def turn_left(self):
        """ Rotates the ant 90° to the left """
        self.direction = (self.direction+3) % 4
        
    def mvt_behavior(self, x, y, turn, orientation):
        """ Define several behaviors of an ant depending on adjacent ants """
        global current_position
        straight_ahead = [(0,1), (1,0), (0,-1), (-1,0)]
        next_position = straight_ahead[self.direction]+self.position
        if self.behavior == 1:
            # move straight ahead
            if tuple(next_position) not in current_position.values():
                self.advance(straight_ahead)
        elif self.behavior == 2:
            # ignore
            turn
            self.advance(orientation)
        elif self.behavior == 3:
            # remain still
            pass
        else:
            print("This behavior isn't define yet")
    
    def next_position(self,orientation):
        return orientation[self.direction]+self.position
    
    def new_position(self, noise_ratio):
        """ Defines how an ant behaves and stores the data """
        global visited_global
        global current_position
        global orientation_black
        global orientation_white
        (x,y) = self.position
        if (x,y) not in visited_global:
            # not visited box
            if random.random() < noise_ratio:
                next_position = (self.next_position(orientation_white), orientation_white,self.turn_right)
            else:
                next_position = (self.next_position(orientation_black), orientation_black,self.turn_left)
            if tuple(next_position[0]) in current_position.values():
                # another ant on the next box
                self.mvt_behavior(x, y, next_position[2], next_position[1])
            else:
                next_position[2]()
                self.position = next_position[0]
            visited_global[(x,y)] = self.ant_id+1
            current_position[self.ant_id] = tuple(next_position[0])
            self.visited_local.append((x,y))
        elif (x,y) not in visited_black:
            # visited black boxes
            next_position = self.next_position(orientation_white)
            if tuple(next_position) in current_position.values():
                # another ant on the next box
                self.mvt_behavior(x,y,self.turn_left(),orientation_white)
            else:
                self.turn_right()
                self.position = next_position
            visited_black[(x,y)] = self.ant_id
            current_position[self.ant_id] = tuple(next_position)
            self.visited_local.append((x,y))
        else:
            # visited white boxes
            next_position = self.next_position(orientation_black)
            if tuple(next_position) in current_position.values():
                # another ant on the next box
                self.mvt_behavior(x,y,self.turn_right(),orientation_black)
            else:
                self.turn_left()
                self.position = next_position
            del visited_black[(x,y)]             
            current_position[self.ant_id] = tuple(next_position)
            self.visited_local.append((x,y))

    def get_data(self):
        """ Turn our data into arrays """
        return np.asarray(self.visited_local, dtype=int)

def initialisation(ants_data):
    global visited_global
    global current_position
    """ With ants_data a dictionary containing information about each ant: (x_init, y_init, init_direction, id, behavior) """
    nb_ants = len(ants_data)
    visited_global = {}
    current_position = {}
    ant_list = [0]*nb_ants
    for ant_id in range(nb_ants):
        ant = Ant(ants_data[ant_id])
        x = round(ants_data[ant_id]['x_init'])
        y = round(ants_data[ant_id]['y_init'])
        current_position[ants_data[ant_id]['id']] = (x,y)
        ant_list[ant_id] = ant
    return ant_list

def move(ant_list, steps, noise_ratio):
    """ Makes all defined ants move """
    for step in range(steps):
        for ant in ant_list:
            ant.new_position(noise_ratio)
    return ant_list