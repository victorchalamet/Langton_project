""" Module de définition des fourmi et de leur comportement """
import turtle
import random

""" Variable global """
visited_global = {}
orientation = [(0,1),(1,0),(0,-1),(-1,0)]

class Ant:
    """ Création d'une fourmi sur l'écran """
    global visited_global
    ant_speed = 0
    
    def __init__(self, donnees_fourmis, size_factor):
        self.visited_local = [] # liste de coordonées d'une fourmi
        self.ant_size = 1*size_factor/21
        self.id_fourmi = donnees_fourmis['id']
        self.ant = turtle.Turtle()
        self.direction_initiale = donnees_fourmis['direction_init']
        self.ant.setheading(self.direction_initiale) # initialise la direction
        self.couleur = donnees_fourmis['couleur']
        self.ant.color(self.couleur)
        self.ant.penup() # lève le stylo
        self.ant.shape("square") # initialise la forme
        self.ant.shapesize(self.ant_size, self.ant_size, 0) # initialise la taille
        self.ant.speed(self.ant_speed) # initialise la vitesse
        self.x_initiale = donnees_fourmis['x_init']
        self.y_initiale = donnees_fourmis['y_init']
        self.ant.goto(self.x_initiale * 21 * self.ant_size, self.y_initiale * 21 * self.ant_size) # aller à la position initiale
        self.ant.hideturtle() # cache la fourmi
    
    def avancer(self):
        """ Fait avancer la fourmi """
        self.ant.forward(self.ant_size * 21)
        
    def tourner_droite(self):
        """ Fait tourner la fourmi de 90° vers la droite """
        self.ant.right(90)
        
    def tourner_gauche(self):
        """ Fait tourner la fourmi de 90° vers la gauche """
        self.ant.left(90)
    
    def new_position(self):
        """ Définie comment se comporte une fourmi et remplie nos données """
        global visited_global
        global orienation
        x, y = self.ant.pos()
        x, y = round(x), round(y)
        if (x, y) not in visited_global:
            # case non visitée ou blanche
            self.ant.color(self.couleur)
            self.ant.stamp()
            self.tourner_droite()
            self.avancer()
            visited_global[(x, y)] = self.id_fourmi + 1
            self.visited_local.append((x, y))       
        else:
            # case visitée par cette fourmi            
            self.ant.color("white")            
            self.ant.stamp()            
            self.tourner_gauche()       
            self.avancer()            
            self.visited_local.append((x, y)) 
            del visited_global[(x, y)]
    
    def initial_noise(self,screen_x, screen_y, noise_ratio, color="black"):
        """ Création du bruit """
        global visited_global
        compteur = 0
        self.ant.penup()
        self.ant.color(color)
        while compteur != (screen_x * screen_y * noise_ratio):
            x, y = random.uniform(-screen_x//2, screen_x//2), random.uniform(-screen_y//2, screen_y//2)
            x, y = round(x), round(y)
            if (x, y) not in visited_global:
                self.ant.goto(x*21*self.ant_size, y*21*self.ant_size)   
                self.ant.stamp()
                compteur += 1
                visited_global[(round(x * 21 * self.ant_size), round(y * 21 * self.ant_size))] = self.id_fourmi + 1
        self.ant.goto(screen_x + 1, screen_y + 1)

def initialisation(donnees_fourmis, screen_x, screen_y, noise, noise_ratio, size_factor):
    global visited_global
    """ Avec donnees_fourmis un dictionnaire contenant les infos de chaque
    fourmis: (x_init, y_init, direction_init, couleur, id) """
    """ Initialisation de l'écran """    
    nb_fourmis = len(donnees_fourmis)
    turtle.TurtleScreen._RUNNING = True # évite l'erreur Terminator
    visited_global = {}
    screen = turtle.Screen()
    screen.title("Fourmi de Langton")
    screen.mode("logo") # change l'orienttion initiale: vers le haut
    screen.clearscreen()
    screen.bgcolor("light gray")
    screen.screensize(screen_x*size_factor, screen_y*size_factor)
    turtle.tracer(0, 0)
    liste_ant = [0]*nb_fourmis
    if noise:
        ant = Ant({'x_init': 0, 'y_init': 0, 'direction_init': 0,
                    'couleur': (0,0,0), 'id': 0}, size_factor).initial_noise(screen_x,
                    screen_y, noise_ratio)
    for numero_fourmi in range(nb_fourmis):
        ant = Ant(donnees_fourmis[numero_fourmi], size_factor)
        liste_ant[numero_fourmi] = ant
    return liste_ant

def move(liste_ant, steps, animation, speed=200):
    """ Fait bouger toutes les fourmis définies """
    if animation :
        turtle.tracer(speed, 0)
        
    for step in range(steps):
        for ant in liste_ant:           
            ant.new_position()
    
    if not animation:
        # turtle.update()
        pass
    turtle.exitonclick()
    
    return liste_ant
