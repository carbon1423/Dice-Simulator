import pygame
import random
import numpy as np
import math
import statistics
# pygame setup
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 600, 600
pygame.display.set_caption("Honors Seminar Dice Simulator")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()


scale = 100

circle_pos = [WIDTH/2, HEIGHT/3]  # x, y

angle = 360

button_text = [['Roll: D4', 'Roll: D6','Roll: D8','Custom Die'],[ 'Roll: D10','Roll: D12','Roll: D20', 'Stats']]

d6 = []
# all the cube vertices
d6.append(np.matrix([-.5,-.5,-.5]))
d6.append(np.matrix([.5,-.5,-.5]))
d6.append(np.matrix([-.5,.5,-.5]))
d6.append(np.matrix([-.5,-.5,.5]))
d6.append(np.matrix([.5,.5,-.5]))
d6.append(np.matrix([.5,-.5,.5]))
d6.append(np.matrix([-.5,.5,.5]))
d6.append(np.matrix([.5,.5,.5]))

d4 = []
# d4.append(np.matrix([-.5,-1 * math.sqrt(3)/4,-3/8,]))
# d4.append(np.matrix([.5,-1 * math.sqrt(3)/4,-3/8]))
# d4.append(np.matrix([0, math.sqrt(3)/4,-3/8]))
# d4.append(np.matrix([0,0,3/8]))
d4.append(np.matrix([-.5,math.sqrt(3)/4,0]))
d4.append(np.matrix([.5,math.sqrt(3)/4,0]))
d4.append(np.matrix([0,math.sqrt(3)/4,math.sqrt(3)/2]))
d4.append(np.matrix([[0,math.sqrt(3)/4 - math.sqrt(6)/3,math.sqrt(3)/6]]))


d8 = []
d8.append(np.matrix([-.5,-1*math.sqrt(2)/4,-1*math.sqrt(2)/4]))
d8.append(np.matrix([.5,-1*math.sqrt(2)/4,-1*math.sqrt(2)/4]))
d8.append(np.matrix([-.5,math.sqrt(2)/4,math.sqrt(2)/4]))
d8.append(np.matrix([.5,math.sqrt(2)/4,math.sqrt(2)/4]))
d8.append(np.matrix([0,.5,-.5]))
d8.append(np.matrix([0,-.5,.5]))


d10 = []
d10.append(np.matrix([-.95,-.649,1.155]))
d10.append(np.matrix([0,-1.155,1.153]))
d10.append(np.matrix([.95,-.649,1.155]))
d10.append(np.matrix([1.54,-.465,.271]))
d10.append(np.matrix([1.54,.465,-.271]))
d10.append(np.matrix([.95,.649,-1.155]))
d10.append(np.matrix([0,1.149,-1.146]))
d10.append(np.matrix([-.95,.649,-1.155]))
d10.append(np.matrix([-1.54,.465,-.271]))
d10.append(np.matrix([-1.54,-.465,.271]))
d10.append(np.matrix([0,1.489,1.164]))
d10.append(np.matrix([0,-1.489,-1.164]))

d12 = []
d12.append(np.matrix([-.5,-.77,0]))
d12.append(np.matrix([.5,-.77,0]))
d12.append(np.matrix([.81,.18,0]))
d12.append(np.matrix([0,.77,0]))
d12.append(np.matrix([-.81,.18,0]))
d12.append(np.matrix([-.81,-1.2,.85]))
d12.append(np.matrix([0,-1.46,1.38]))
d12.append(np.matrix([.81,-1.19,.85]))
d12.append(np.matrix([1.31,-.51,1.38]))
d12.append(np.matrix([1.31,.34,.85]))
d12.append(np.matrix([.81,1.03,1.38]))
d12.append(np.matrix([0,1.29,.85]))
d12.append(np.matrix([-.81,1.03,1.38]))
d12.append(np.matrix([-1.31,.34,.85]))
d12.append(np.matrix([-1.31,-.51,1.38]))
d12.append(np.matrix([0,-.93,2.23]))
d12.append(np.matrix([.81,-.34,2.23]))
d12.append(np.matrix([.5,.61,2.23]))
d12.append(np.matrix([-.5,.61,2.23]))
d12.append(np.matrix([-.81,-.35,2.23]))

d20 = []
d20.append(np.matrix([.5,.43,0])) #duplicate point to set it apart from d6
d20.append(np.matrix([.5,.43,0]))
d20.append(np.matrix([-.5,.43,0]))
d20.append(np.matrix([0,-.43,0]))
d20.append(np.matrix([0,1.08,.58]))
d20.append(np.matrix([-.81,-.32,.58]))
d20.append(np.matrix([.81,-.32,.58]))
d20.append(np.matrix([.81,.61,.93]))
d20.append(np.matrix([-.81,.61,.93]))
d20.append(np.matrix([0,-.79,.93]))
d20.append(np.matrix([0,.72,1.51]))
d20.append(np.matrix([-.5,-.14,1.51]))
d20.append(np.matrix([.5,-.14,1.51]))

points = []
projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


projected_points = [
    [n, n] for n in range(len(points))
]
def connect_points(i, j, points):
    pygame.draw.line(
        screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

def fill_shape(points, color_scale,i,j,k,l=None,m=None ):
    if l == None:
        pygame.draw.polygon(
            screen, ((100 * color_scale) % 255,(100 * color_scale) % 255,(100 * color_scale) % 255), [(points[i][0], points[i][1]), (points[j][0], points[j][1]),(points[k][0], points[k][1])]
        )
    elif m == None:
        pygame.draw.polygon(
            screen, ((100 * color_scale) % 255,(100 * color_scale) % 255,(100 * color_scale) % 255), [(points[i][0], points[i][1]), (points[j][0], points[j][1]),(points[k][0], points[k][1]),(points[l][0], points[l][1])]
        )
    else:
        pygame.draw.polygon(
            screen, ((100 * color_scale) % 255,(100 * color_scale) % 255,(100 * color_scale) % 255), [(points[i][0], points[i][1]), (points[j][0], points[j][1]),(points[k][0], points[k][1]),(points[l][0], points[l][1]),(points[m][0], points[m][1])]
        )
clock = pygame.time.Clock()
running = True

rolls = {
    'd4': [0],
    'd6': [0],
    'd8': [0],
    'd10': [0],
    'd12': [0],
    'd20': [0],
    'Custom': [0]
}

def buttons():
    for i in range(4):
        screen.fill((100,100,100),(50 + i*125,400,125,75))
    for i in range(4):
        screen.fill((100,100,100),(50 + i*125,475,125,75))

def dice_roll(i,j):
    dice = [[random.randint(1,4),random.randint(1,6),random.randint(1,8)],
            [random.randint(1,10),random.randint(1,12),random.randint(1,20)]]
    return dice[i][j]

def statscreen(up):
    if up:
        screen.fill((255,255,255),(50,50,HEIGHT-100,WIDTH-100))
        pygame.draw.line(screen,(0,0,0),(525,75),(550,75))
        pygame.draw.line(screen,(0,0,0),(525,50),(525,75))
        pygame.draw.line(screen,(0,0,0),(530,55),(545,70),3)
        pygame.draw.line(screen,(0,0,0),(530,70),(545,55),3)
        for i in range(1,8):
            pygame.draw.line(screen,(0,0,0),(50,62*i+50),(WIDTH-50,62*i+50))
        for i in range(1,4):
            pygame.draw.line(screen,(0,0,0),(125*i+50,50),(125*i+50,HEIGHT-50))
        dicestrings = list(rolls.keys())
        for i in range(1,8):
            font = pygame.font.Font('Roboto-Light.ttf',20)
            text = font.render(dicestrings[i-1], True, (0,0,0))
            text_width, text_height = font.size(dicestrings[i-1])
            screen.blit(text,(112-text_width//2,81-text_height//2+i * 62))
        headerstrings = ['Statistics','Average','Mode','Number']
        for i in range(4):
            font = pygame.font.Font('Roboto-Light.ttf',20)
            text = font.render(headerstrings[i], True, (0,0,0))
            text_width, text_height = font.size(headerstrings[i])
            if i != 3:
                screen.blit(text,(112 - text_width//2 + i * 125, 81-text_height // 2))
        font = pygame.font.Font('Roboto-Light.ttf',15)
        text = font.render('Number', True, (0,0,0))
        text_width, text_height = font.size('Number')
        screen.blit(text,(487 - text_width // 2, 55))
        text = font.render('of', True, (0,0,0))
        text_width, text_height = font.size('of')
        screen.blit(text,(487 - text_width // 2, 55 + text_height))
        text = font.render('Rolls', True, (0,0,0))
        text_width, text_height = font.size('Rolls')
        screen.blit(text,(487 - text_width // 2, 55 + text_height *2))
        averages = []
        modes = []
        num_of_rolls = []
        for key in dicestrings:
            averages.append(stats[key]['average'])
            modes.append(str(stats[key]['mode']))
            num_of_rolls.append(str(len(stats[key]['number'])))
        for i in range(1,8):
            font = pygame.font.Font('Roboto-Light.ttf',20)
            text = font.render(averages[i-1], True, (0,0,0))
            text_width, text_height = font.size(averages[i-1])
            screen.blit(text,(237-text_width//2,81-text_height//2+i * 62))
        for i in range(1,8):
            font = pygame.font.Font('Roboto-Light.ttf',20)
            text = font.render(modes[i-1], True, (0,0,0))
            text_width, text_height = font.size(modes[i-1])
            screen.blit(text,(362-text_width//2,81-text_height//2+i * 62))
        for i in range(1,8):
            font = pygame.font.Font('Roboto-Light.ttf',20)
            text = font.render(num_of_rolls[i-1], True, (0,0,0))
            text_width, text_height = font.size(num_of_rolls[i-1])
            screen.blit(text,(487-text_width//2,81-text_height//2+i * 62))
def customsetupscreen(up):
    if up:
        screen.fill((255,255,255),(50,50,HEIGHT-100,WIDTH-100))
        pygame.draw.line(screen,(0,0,0),(525,75),(550,75))
        pygame.draw.line(screen,(0,0,0),(525,50),(525,75))
        pygame.draw.line(screen,(0,0,0),(530,55),(545,70),3)
        pygame.draw.line(screen,(0,0,0),(530,70),(545,55),3)
        font = pygame.font.Font('Roboto-Light.ttf',30)
        text = font.render('Select Die Size', True, (0,0,0))
        text_width, text_height = font.size('Select Die Size')
        screen.blit(text,(300 - text_width // 2, 75 - text_height // 2))
        pygame.draw.line(screen,(0,0,0),(50,95),(550,95))
        pygame.draw.line(screen,(0,0,0),(50,170),(550,170))
        for i in range(1,6):
            pygame.draw.line(screen,(0,0,0),(50 + 85 * i,95),(50 + 85 * i,170))
        dicestrings = list(rolls.keys())[:-1]
        for i in range(len(dicestrings)):
            font = pygame.font.Font('Roboto-Light.ttf',20)
            text = font.render(dicestrings[i], True, (0,0,0))
            text_width, text_height = font.size(dicestrings[i])
            screen.blit(text,(92 - text_width // 2 + 85 * i, 132 - text_height // 2))
        pygame.draw.line(screen,(0,0,0),(50,220),(550,220))
        font = pygame.font.Font('Roboto-Light.ttf',30)
        text = font.render('Enter Numbers on the Sides', True, (0,0,0))
        text_width, text_height = font.size('Enter Numbers on the Sides')
        screen.blit(text,(300 - text_width // 2, 195 - text_height // 2))
        pygame.draw.line(screen,(0,0,0),(300,220),(300,550))
        for i in range(1,4):
            pygame.draw.line(screen,(0,0,0),(50, 220 + i * 82),(300, 220 + i * 82))
        for i in range(1,3):
            pygame.draw.line(screen,(0,0,0),(50 + i * 83, 220),(50 + i * 83, 466))
        pygame.draw.line(screen,(0,0,0),(175,466),(175,550))
        numpad = [['1','2','3'],['4','5','6'],['7','8','9'],['0','Enter']]
        for i in range(3):
            for j in range(3):
                font = pygame.font.Font('Roboto-Light.ttf',30)
                text = font.render(numpad[j][i], True, (0,0,0))
                text_width, text_height = font.size(numpad[j][i])
                screen.blit(text,(95 - (text_width // 2) + i * (550/6),265 - (text_height // 2) + j * (550/6)))
        for i in range(2):
            font = pygame.font.Font('Roboto-Light.ttf',30)
            text = font.render(numpad[3][i], True, (0,0,0))
            text_width, text_height = font.size(numpad[3][i])
            screen.blit(text,(112 - text_width//2 + i * 125, 508 - text_height // 2))
        if die_is_selected and int(selected_die[1:])-len(sides_of_custom) != 0:
            font = pygame.font.Font('Roboto-Light.ttf',20)
            text = font.render("Number of Sides Left to Fill", True, (0,0,0))
            text_width, text_height = font.size("Number of Sides Left to Fill")
            screen.blit(text,(425 - text_width //2, 355 - text_height // 2 ))
        if die_is_selected and int(selected_die[1:])-len(sides_of_custom) != 0:
            font = pygame.font.Font('Roboto-Light.ttf',30)
            text = font.render(str(int(selected_die[1:])-len(sides_of_custom)), True, (0,0,0))
            text_width, text_height = font.size(str(int(selected_die[1:])-len(sides_of_custom)))
            screen.blit(text,(425 - text_width//2, 385 - text_height // 2))
        if die_is_selected and int(selected_die[1:])-len(sides_of_custom) == 0:
            font = pygame.font.Font('Roboto-Light.ttf',30)
            text = font.render("Press Enter", True, (0,0,0))
            text_width, text_height = font.size("Press Enter")
            screen.blit(text,(425 - text_width //2, 355 - text_height // 2 ))
        
rotated = False
roll = 1
statscreenup = False
customsetup = False
d4_rolls = []
d6_rolls = []
d8_rolls = []
d10_rolls = []
d12_rolls = []
d20_rolls = []
custom_rolls = []
sides_of_custom = []
selected_die = None
die_selection = ['d4','d6','d8','d10','d12','d20']
die_is_selected = False
Custom_never_rolled = True
can_be_reset = False
custom_rolled = False
while running:
    stats = {
        'd4': {
            'average': format(statistics.mean(rolls['d4']), '.2f'),
            'mode' : statistics.mode(rolls['d4']),
            'number' : d4_rolls
        },
        'd6': {
            'average': format(statistics.mean(rolls['d6']), '.2f'),
            'mode' : statistics.mode(rolls['d6']),
            'number' : d6_rolls
        },
        'd8': {
            'average': format(statistics.mean(rolls['d8']), '.2f'),
            'mode' : statistics.mode(rolls['d8']),
            'number' : d8_rolls
        },
        'd10': {
            'average': format(statistics.mean(rolls['d10']), '.2f'),
            'mode' : statistics.mode(rolls['d10']),
            'number' : d10_rolls
        },
        'd12': {
            'average': format(statistics.mean(rolls['d12']), '.2f'),
            'mode' : statistics.mode(rolls['d12']),
            'number' : d12_rolls
        },
        'd20': {
            'average': format(statistics.mean(rolls['d20']), '.2f'),
            'mode' : statistics.mode(rolls['d20']),
            'number' : d20_rolls
        },
        'Custom': {
            'average': format(statistics.mean(rolls['Custom']), '.2f'),
            'mode' : statistics.mode(rolls['Custom']),
            'number' : custom_rolls
        }
    }
    dt = clock.tick(60) / 1000  # limits FPS to 60
    mouseX, mouseY = pygame.mouse.get_pos()
    screen.fill((25,25,25)) 
    buttons()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for i in range(3):
            for j in range(2):
                if event.type == pygame.MOUSEBUTTONDOWN and (400 + (j * 75)) < mouseY < (475 + (j * 75)) and (50 + i * 125) < mouseX < ((50 + i * 125) + 125) and statscreenup == False and customsetup == False:
                    # print(i,j)
                    angle = .1
                    roll = dice_roll(j, i)
                    custom_rolled = False
                    # print(roll)
                    if i == 0 and j == 0:
                        points = d4
                        scale = 100
                        if rolls['d4'][0] == 0:
                            rolls['d4'].remove(0)
                        rolls['d4'].append(roll)
                        d4_rolls.append(1)
                        # print(d4_rolls)
                    elif i == 1 and j == 0:
                        points = d6
                        scale = 100
                        if rolls['d6'][0] == 0:
                            rolls['d6'].remove(0)
                        rolls['d6'].append(roll)
                        d6_rolls.append(1)
                        # print(d6_rolls)
                    elif i == 2 and j ==0:
                        points = d8
                        scale = 100
                        if rolls['d8'][0] == 0:
                            rolls['d8'].remove(0)
                        rolls['d8'].append(roll)
                        d8_rolls.append(1)
                        # print(d8_rolls)
                    elif i == 0 and j == 1:
                        points = d10
                        scale = 50
                        if rolls['d10'][0] == 0:
                            rolls['d10'].remove(0)
                        rolls['d10'].append(roll)
                        d10_rolls.append(1)
                        # print(d10_rolls)
                    elif i == 1 and j == 1:
                        points = d12
                        scale = 50
                        if rolls['d12'][0] == 0:
                            rolls['d12'].remove(0)
                        rolls['d12'].append(roll)
                        d12_rolls.append(1)
                        # print(d12_rolls)
                    elif i == 2 and j == 1:
                        points = d20
                        scale = 75
                        if rolls['d20'][0] == 0:
                            rolls['d20'].remove(0)
                        rolls['d20'].append(roll)
                        d20_rolls.append(1)
                        # print(d20_rolls)
                    else:
                        points = []
                    rotated = False
        if event.type == pygame.MOUSEBUTTONDOWN and 425 < mouseX < 550 and 475 < mouseY < 550 and customsetup == False:
            statscreenup = True
            # print(stats)     
        if event.type == pygame.MOUSEBUTTONDOWN and 425 < mouseX < 487 and 428 < mouseY < 475:
            customsetup = True
        for i in range(0,6):
            if event.type == pygame.MOUSEBUTTONDOWN and customsetup and (50 + i * 85 < mouseX < 135 + i * 85) and (95 < mouseY < 170):
                if can_be_reset:
                    sides_of_custom = []
                    rolls['Custom'] = [0]
                    Custom_never_rolled = True
                selected_die = die_selection[i]
                die_is_selected = True
        for i in range(0,3):
            if event.type == pygame.MOUSEBUTTONDOWN and customsetup and 50 + (500/6 * i) < mouseX < 500/6 + 50 + (500/6 * i) and 220 < mouseY < 220 + 500/6 and die_is_selected and len(sides_of_custom) < int(selected_die[1:]) :
                sides_of_custom.append(i + 1)
                # print(sides_of_custom)
        for i in range(0,3):
            if event.type == pygame.MOUSEBUTTONDOWN and customsetup and 50 + (500/6 * i) < mouseX < 500/6 + 50 + (500/6 * i) and 220 + 500/6 < mouseY < 220 + 1000/6 and die_is_selected and len(sides_of_custom) < int(selected_die[1:]) :
                sides_of_custom.append(i + 4)
                # print(sides_of_custom)
        for i in range(0,3):
            if event.type == pygame.MOUSEBUTTONDOWN and customsetup and 50 + (500/6 * i) < mouseX < 500/6 + 50 + (500/6 * i) and 220 + 1000/6 < mouseY < 220 + 1500/6 and die_is_selected and len(sides_of_custom) < int(selected_die[1:]) :
                sides_of_custom.append(i + 7)
                # print(sides_of_custom)
        if event.type == pygame.MOUSEBUTTONDOWN and customsetup and 50 < mouseX < 500/6 + 50 and 220 + 1500/6 < mouseY < 550 and die_is_selected and len(sides_of_custom) < int(selected_die[1:]) :
            sides_of_custom.append(0)
        if event.type == pygame.MOUSEBUTTONDOWN and 487 < mouseX < 550 and 428 < mouseY < 475 and statscreenup == False and customsetup == False and len(sides_of_custom) == int(selected_die[1:]):
            if rolls['Custom'][0] == 0 and Custom_never_rolled:
                rolls['Custom'].remove(0)
            randomindex = random.randint(0,len(sides_of_custom)-1)
            roll = sides_of_custom[randomindex]
            rolls['Custom'].append(sides_of_custom[randomindex])
            custom_rolls.append(1)
            # print(rolls['Custom'])
            custom_rolled = True
        if event.type == pygame.MOUSEBUTTONDOWN and statscreenup and 525 < mouseX < 550 and 50 < mouseY < 75:
            statscreenup = False
        if event.type == pygame.MOUSEBUTTONDOWN and customsetup and 525 < mouseX < 550 and 50 < mouseY < 75:
            customsetup = False
        if event.type == pygame.MOUSEBUTTONDOWN and customsetup and 225 < mouseX < 300 and 495 < mouseY < 550 and die_is_selected and len(sides_of_custom) == int(selected_die[1:]):
            customsetup = False
            die_is_selected = False
            can_be_reset = True
            # print(True)

    rotation_z = np.matrix([
    [math.cos(angle), -1*math.sin(angle), 0],
    [math.sin(angle), math.cos(angle), 0],
    [0, 0, 1],
    ])
    rotation_y = np.matrix([
        [math.cos(2*angle), 0, math.sin(2*angle)],
        [0, 1, 0],
        [-1*math.sin(2*angle), 0, math.cos(2* angle)],
    ])
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, math.cos(angle), -1*math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)],
    ])
    if angle < 2 * math.pi and angle != 0:
        angle += 5 * dt
    if angle >= 2 * math.pi:
        angle = 0
        rotated = True

    # fill the screen with a color to wipe away anything from last frame
    projected_points = [
    0 for n in range(len(points))
]
    i = 0
    if points != [] and custom_rolled == False:
        for point in points:
            rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
            rotated2d = np.dot(rotation_y, rotated2d)
            rotated2d = np.dot(rotation_x, rotated2d)

            projected2d = np.dot(projection_matrix, rotated2d)

            x = int(projected2d[0][0] * scale) + circle_pos[0]
            y = int(projected2d[1][0] * scale) + circle_pos[1]

            projected_points[i] = [x, y]
            # pygame.draw.circle(screen, RED, (x, y), 5)
            i += 1

        if points == d4:
            fill_shape(projected_points,1.5,0,1,2)
            fill_shape(projected_points,1,1,2,3)
            fill_shape(projected_points,1,0,2,3)            
            fill_shape(projected_points,2,0,1,3)

        if points == d6:
            fill_shape(projected_points, 1, 3, 5, 7, 6)
            fill_shape(projected_points, 1.5, 1, 4, 7, 5)
            fill_shape(projected_points, 1.5, 2, 4, 7, 6)
            fill_shape(projected_points, 1.5, 0, 1, 5, 3)
            fill_shape(projected_points, 1.5, 0, 2, 6, 3)
            fill_shape(projected_points, 2, 0, 1, 4, 2)
        if points == d8:
            fill_shape(projected_points, .5 , 4, 2 , 3)
            fill_shape(projected_points, 1, 0, 4, 2)
            fill_shape(projected_points, 1, 1, 4, 3)
            fill_shape(projected_points, 1, 0, 1, 4)
            fill_shape(projected_points, 1.5, 0, 5, 2)
            fill_shape(projected_points, 1.5, 1, 5, 3)
            fill_shape(projected_points, 1.5, 0, 1, 5)
            fill_shape(projected_points, 2, 5, 2, 3)
        if points == d10:
            fill_shape(projected_points, .75 , 10, 0 ,9, 8)
            fill_shape(projected_points, .75 , 10, 0 ,1, 2)
            fill_shape(projected_points, .75 , 10, 2 ,3, 4)
            fill_shape(projected_points, 1 , 10, 4 ,5, 6)
            fill_shape(projected_points, 1 , 10, 6 ,7, 8)
            fill_shape(projected_points, 1.25 , 11, 1 ,0,9)
            fill_shape(projected_points, 1.25 , 11, 3 ,2,1)
            fill_shape(projected_points, 1.5 , 11, 5 ,4, 3)
            fill_shape(projected_points, 1.5 , 11, 7 ,8, 9)
            fill_shape(projected_points, 2 , 11, 5 ,6, 7)
        if points == d12:
            fill_shape(projected_points,.5,0,1,2,3,4)
            fill_shape(projected_points,1,1,0,5,6,7)
            fill_shape(projected_points,1,1,2,9,8,7)
            fill_shape(projected_points,1,2,3,11,10,9)
            fill_shape(projected_points,1,4,3,11,12,13)
            fill_shape(projected_points,1,0,4,13,14,5)
            fill_shape(projected_points,9/8,17,18,12,11,10)
            fill_shape(projected_points,1.25,16,17,10,9,8)
            fill_shape(projected_points,1.25,19,18,12,13,14)
            fill_shape(projected_points,1.75,16,15,6,7,8)
            fill_shape(projected_points,1.75,15,19,14,5,6)
            fill_shape(projected_points,2,19,18,17,16,15)
        if points == d20:
            fill_shape(projected_points,.75,10,11,12)
            fill_shape(projected_points,1,8,10,11)
            fill_shape(projected_points,1,9,11,12)
            fill_shape(projected_points,1,7,10,12)
            fill_shape(projected_points,1.25,4,7,10)
            fill_shape(projected_points,1.25,4,8,10)
            fill_shape(projected_points,1.25,5,6,11)
            fill_shape(projected_points,1.25,5,9,11)
            fill_shape(projected_points,1.25,6,9,12)
            fill_shape(projected_points,1.25,6,7,12)
            fill_shape(projected_points,1.5,3,6,9)
            fill_shape(projected_points,1.5,3,5,9)
            fill_shape(projected_points,1.5,2,5,8)
            fill_shape(projected_points,1.5,2,4,8)
            fill_shape(projected_points,1.5,1,4,7)
            fill_shape(projected_points,1.5,1,6,7)
            fill_shape(projected_points,1.75,1,3,6)
            fill_shape(projected_points,1.75,2,3,5)
            fill_shape(projected_points,1.75,1,2,4)
            fill_shape(projected_points,2,1,2,3)
    #this probably needs to be optimized so that larger shapes only have to draw their faces not every combination of three points
        if rotated and (points == d4 or points == d6 or points == d8 or points == d10 or points == d12):
            font = pygame.font.Font('Roboto-Light.ttf',50)
            text = font.render(f'{roll}', True, (50, 50, 50))
            text_width, text_height = font.size(f'{roll}')
            screen.blit(text,((WIDTH//2) - text_width//2 ,(HEIGHT//3) - text_height//2))
        elif rotated and points == d20:
            font = pygame.font.Font('Roboto-Light.ttf',25)
            text = font.render(f'{roll}', True, (50, 50, 50))
            text_width, text_height = font.size(f'{roll}')
            screen.blit(text,((WIDTH//2) - text_width//2 ,(HEIGHT//2.9) - text_height//2))
    if custom_rolled:
        font = pygame.font.Font('Roboto-Light.ttf',50)
        text = font.render(f'{roll}', True, (250, 250, 250))
        text_width, text_height = font.size(f'{roll}')
        screen.blit(text,((WIDTH//2) - text_width//2 ,(HEIGHT//3) - text_height//2))
    for i in range(2):
        for j in range(4):
            if i != 0 or j != 3:
                font = pygame.font.Font('Roboto-Light.ttf',20)
                text = font.render(button_text[i][j], True, (255,255,255))
                text_width, text_height = font.size(button_text[i][j])
                screen.blit(text,(112 + (j * 125) - text_width//2 ,425 + (i*75) - text_height//2))
            else:
                font = pygame.font.Font('Roboto-Light.ttf',15)
                text = font.render(button_text[i][j], True, (255,255,255))
                text_width, text_height = font.size(button_text[i][j])
                screen.blit(text,((487) - text_width//2 ,420 - text_height//2))
                pygame.draw.line(screen,(25,25,25),(425,428),(550,428))
                pygame.draw.line(screen,(25,25,25),(487,428),(487,475))
                text = font.render('Set Up', True, (255,255,255))
                text_width, text_height = font.size('Set Up')
                screen.blit(text,((456) - text_width//2 ,447 - text_height//2))
                text = font.render('Roll', True, (255,255,255))
                text_width, text_height = font.size('Roll')
                screen.blit(text,((518) - text_width//2 ,447 - text_height//2))
    statscreen(statscreenup)
    customsetupscreen(customsetup)
    pygame.display.flip()
pygame.quit()