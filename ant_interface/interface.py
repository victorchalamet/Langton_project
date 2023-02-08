""" Interface main module """
import tkinter as tk
from . import main
from . import random_interface as random

class Application():
    """ Creation of the interface """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("langton's ants")
        self.root.geometry("220x435")
        
        frame1 = tk.LabelFrame(self.root, text="number of ants")       
        frame1.pack(fill="both")
        self.nb_ants = tk.StringVar(value=1)
        self.spin_box = tk.Spinbox(frame1,from_=0,to=1000,textvariable=self.nb_ants,wrap=True)
        self.spin_box.pack()
        
        frame2 = tk.LabelFrame(self.root, text="position of ants and noise")    
        frame2.pack(fill="both")
        self.pos_list = tk.StringVar() 
        self.pos_list.set("[(0,0,0)]")
        self.entry = tk.Entry(frame2, textvariable=self.pos_list)
        self.entry.pack()
        self.noise_ratio = tk.StringVar() 
        self.noise_ratio.set("0.01")
        self.entry1 = tk.Entry(frame2, textvariable=self.noise_ratio)
        self.entry1.pack()        
        self.position = tk.IntVar()
        button1 = tk.Checkbutton(frame2, text="random position of ants", variable=self.position, onvalue = True, offvalue = False)
        button1.pack()
        self.orientation = tk.IntVar()
        button2 = tk.Checkbutton(frame2, text="random orientation of ants", variable=self.orientation, onvalue = True, offvalue = False)
        button2.pack()
        self.noise = tk.IntVar()
        button4 = tk.Checkbutton(frame2, text="able noise", variable=self.noise, onvalue = True, offvalue = False)
        button4.pack()
        
        frame3 = tk.LabelFrame(self.root, text="color and size of ants")     
        frame3.pack(fill="both")
        self.color = tk.IntVar()
        button = tk.Checkbutton(frame3, text="different color for each", variable=self.color, onvalue = True, offvalue = False)
        button.pack()
        self.size = tk.StringVar() 
        self.size.set("5")
        self.entry2 = tk.Entry(frame3, textvariable=self.size)
        self.entry2.pack()   
        
        frame4 = tk.LabelFrame(self.root, text="number of step")     
        frame4.pack(fill="both")
        self.nb_it = tk.StringVar(value=200000)
        self.spin_box1 = tk.Spinbox(frame4,from_=0, to=1000000, textvariable=self.nb_it, wrap=True)
        self.spin_box1.pack()
        
        frame5 = tk.LabelFrame(self.root, text="size of screen and speed")     
        frame5.pack(fill="both")
        self.screen_x = tk.StringVar(value=500)
        self.spin_box1 = tk.Spinbox(frame5,from_=0, to=3000, textvariable=self.screen_x, wrap=True)
        self.spin_box1.pack()
        self.screen_y = tk.StringVar(value=500)
        self.spin_box2 = tk.Spinbox(frame5,from_=0, to=3000, textvariable=self.screen_y ,wrap=True)
        self.spin_box2.pack()
        self.varanim = tk.IntVar()
        self.speed = tk.StringVar() 
        self.speed.set("1")
        self.entry1 = tk.Entry(frame5, textvariable=self.speed)
        self.entry1.pack()    
        
        button3 = tk.Checkbutton(frame5, text="disable animation",variable=self.varanim, onvalue = False, offvalue = True)
        button3.pack()        
        button3 = tk.Button(self.root, text="Launch", command=lambda: main.move(main.initialisation(random.random_initialization(eval(self.pos_list.get()),
                            int(self.nb_ants.get()), self.color.get(), self.position.get(), self.orientation.get(), int(self.screen_x.get()),
                            int(self.screen_y.get())), int(self.screen_x.get()), int(self.screen_y.get()), self.noise.get(), eval(self.noise_ratio.get()),
                            int(self.size.get())), int(self.nb_it.get()), self.varanim.get(),int(self.speed.get())))
        button3.pack(fill="both")
        self.root.mainloop()