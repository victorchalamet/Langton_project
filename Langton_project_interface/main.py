""" Module for defining ants and their behavior """
import turtle
import random

""" Global variable """
visited_global = {}
orientation = [(0,1),(1,0),(0,-1),(-1,0)]

class Ant:
    """ Creation of an ant on the screen """
    global visited_global
    ant_speed = 0
    
    def __init__(self, ants_data, size_factor):
        self.visited_local = [] # list of coordinates of an ant
        self.ant_size = 1*size_factor/21
        self.ant_id = ants_data['id']
        self.ant = turtle.Turtle()
        self.initial_direction = ants_data['direction_init']
        self.ant.setheading(self.initial_direction) # initialize the direction
        self.color = ants_data['color']
        self.ant.color(self.color)
        self.ant.penup() # lift the pen
        self.ant.shape("square") # initialize the form
        self.ant.shapesize(self.ant_size, self.ant_size, 0) # initialize the shape
        self.ant.speed(self.ant_speed) # initialize the speed
        self.x_initial = ants_data['x_init']
        self.y_initial = ants_data['y_init']
        self.ant.goto(self.x_initial * 21 * self.ant_size, self.y_initial * 21 * self.ant_size) # go to the initial position
        self.ant.hideturtle() # hide the ant
    
    def advance(self):
        """ Advance the ant """
        self.ant.forward(self.ant_size * 21)
        
    def turn_right(self):
        """ Rotates the ant 90° to the right """
        self.ant.right(90)
        
    def turn_left(self):
        """ Rotates the ant 90° to the left """
        self.ant.left(90)
    
    def new_position(self):
        """ Define how an ant behaves and stores our data """
        global visited_global
        global orienation
        x, y = self.ant.pos()
        x, y = round(x), round(y)
        if (x, y) not in visited_global:
            # unvisited or white box
            self.ant.color(self.color)
            self.ant.stamp()
            self.turn_right()
            self.advance()
            visited_global[(x, y)] = self.ant_id + 1
            self.visited_local.append((x, y))       
        else:
            # visited box            
            self.ant.color("white")            
            self.ant.stamp()            
            self.turn_left()       
            self.advance()            
            self.visited_local.append((x, y)) 
            del visited_global[(x, y)]
    
    def initial_noise(self, screen_x, screen_y, noise_ratio, color="black"):
        """ Creation of noise """
        global visited_global
        counter = 0
        self.ant.penup()
        self.ant.color(color)
        while counter != (screen_x * screen_y * noise_ratio):
            x, y = random.uniform(-screen_x//2, screen_x//2), random.uniform(-screen_y//2, screen_y//2)
            x, y = round(x), round(y)
            if (x, y) not in visited_global:
                self.ant.goto(x*21*self.ant_size, y*21*self.ant_size)   
                self.ant.stamp()
                counter += 1
                visited_global[(round(x * 21 * self.ant_size), round(y * 21 * self.ant_size))] = self.ant_id + 1
        self.ant.goto(screen_x + 1, screen_y + 1)

def initialisation(ants_data, screen_x, screen_y, noise, noise_ratio, size_factor):
    global visited_global
    """ With ants_data a dictionary containing information about each ant: (x_init, y_init, init_direction, color, id) """
    """ Screen initialization """    
    nb_fourmis = len(ants_data)
    turtle.TurtleScreen._RUNNING = True # avoid Terminator error
    visited_global = {}
    screen = turtle.Screen()
    screen.title("Langton's ant")
    screen.mode("logo") # changes initial orientation to top
    screen.clearscreen()
    screen.bgcolor("light gray")
    screen.screensize(screen_x*size_factor, screen_y*size_factor)
    turtle.tracer(0, 0)
    ant_list = [0]*nb_fourmis
    if noise:
        ant = Ant({'x_init': 0, 'y_init': 0, 'direction_init': 0,
                    'color': (0,0,0), 'id': 0}, size_factor).initial_noise(screen_x,
                    screen_y, noise_ratio)
    for ant_id in range(nb_fourmis):
        ant = Ant(ants_data[ant_id], size_factor)
        ant_list[ant_id] = ant
    return ant_list

def move(ant_list, steps, animation, speed=200):
    """ Makes all defined ants move """
    if animation :
        turtle.tracer(speed, 0)
        
    for step in range(steps):
        for ant in ant_list:           
            ant.new_position()
    
    turtle.exitonclick()
    
    return ant_list
