# Introduction
I had to model a Langton's ant [1] and exploit some data such as it's distance from it's initial position during the time. In short I initalize a 2D space full of white boxes. I drop an ants on the space, starting from (0,0), and give it the following behavior:
- If the box it's standing on is white, colors the boxe in black, rotates 90 degrees clockwise, move forward by 1 box.
- If the box it's standing on is black, colors the boxe in white, rotates 90 degrees counter-clockwise, move forward by 1 box.

I also defined multiple behavior if multiple ants were to close. First what i mean by "close" is when there's already an ant on an other ant's next box. If this happen:
- 1 -> colors the box in white/black (depending on its current color), move forward.
- 2 -> proceed as if there were no other ant.
- 3 -> remain still

## How to install it ?
One can use
```bash
pip install Langton-project
```
in the terminal in order to install every packages that i used in this project. **In this case you'll have to write you own python file** and launch it (or just copying the run.py or run_interface.py files)

## How does it work ?
To clone the repository use
```bash
git clone https://github.com/victorchalamet/Langton_project
```
You can launch the run.py file and give some argument in the terminal, for instance:
```bash
python3 run.py 2 30 12000 0.05 12 3
```
will launch the script with 2 ants, both following the behavior associated with 3, each ant will make 12000 steps and the data will be averaged over 30 iterations, each iteration will give each ant a new random set of initial parameters (position and orientation). Futhermore 5% of the 2D space will be filled with black boxes that will alter their path.

The *run_interface.py* file can be launch to see the ants move and draw beautiful figures. How to initialize ants with the interface: you wil have to specify the number of ants, their initial position and orientation (0, 90, 180, 270), if you want noise and how many, if you want the posistion or the orientation to be random (be carefull, if you want to initialize multiple ants with the interface you will have to specify an initial position even though you have checked the "random positions" box), the size of the ants (only pick odd intergers), if you want a random color (suggested with more than one ant), the number of steps, the size of the screen, the speed of the animation and finally if you want to disable the animation.
It can produce beautiful figure:

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d3/LangtonsAnt.png" alt="After 11000 steps"/>
</p>

### Bibliography
[1] C. Langton, (1986) « Studying artificial life with cellular automata », Physica 22D 120-149
