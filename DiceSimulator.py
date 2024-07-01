import pygame
import random
import numpy as np
import math

#pygame setup
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 600, 600
pygame.display.set_caption("Dice Simulator")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
scale = 100
circle_pos = [WIDTH/2, HEIGHT/3]  # x, y
angle = 360

button_text = [['Roll: D4', 'Roll: D6','Roll: D8','Custom Die'],[ 'Roll: D10','Roll: D12','Roll: D20', 'Stats']] #list for looping through for button text

d6 = []
#Each append call is adding the points of a unit cube centered around the orgin
d6.append(np.matrix([-.5,-.5,-.5]))
d6.append(np.matrix([.5,-.5,-.5]))
d6.append(np.matrix([-.5,.5,-.5]))
d6.append(np.matrix([-.5,-.5,.5]))
d6.append(np.matrix([.5,.5,-.5]))
d6.append(np.matrix([.5,-.5,.5]))
d6.append(np.matrix([-.5,.5,.5]))
d6.append(np.matrix([.5,.5,.5]))

d4 = []
#Creating the unit tetrahedron
d4.append(np.matrix([-.5,math.sqrt(3)/4,0]))
d4.append(np.matrix([.5,math.sqrt(3)/4,0]))
d4.append(np.matrix([0,math.sqrt(3)/4,math.sqrt(3)/2]))
d4.append(np.matrix([[0,math.sqrt(3)/4 - math.sqrt(6)/3,math.sqrt(3)/6]]))

d8 = []
#Creating the unit octahedron
d8.append(np.matrix([-.5,-1*math.sqrt(2)/4,-1*math.sqrt(2)/4]))
d8.append(np.matrix([.5,-1*math.sqrt(2)/4,-1*math.sqrt(2)/4]))
d8.append(np.matrix([-.5,math.sqrt(2)/4,math.sqrt(2)/4]))
d8.append(np.matrix([.5,math.sqrt(2)/4,math.sqrt(2)/4]))
d8.append(np.matrix([0,.5,-.5]))
d8.append(np.matrix([0,-.5,.5]))