# Alec Korsah (ajk5qv)

import pygame
import gamebox
import random
import math

camera = gamebox.Camera(800, 600)

dinosaur = gamebox.from_color(100,480,'blue',55,130)
ground = gamebox.from_color(0,600,'tan',1600,120)
cactus_1 = gamebox.from_color(600,480,'green',45,120)
cactus_2 = gamebox.from_color(1200,480,'green', 45,150)
cactus_3 = gamebox.from_color(1800,480,'green',45,130)
pterodactyl_1 = gamebox.from_color(1000,300,'purple',50,50)



score = 0

game_on = False

gravity = 2

def tick(keys):
    """
    This function allows the action of collision to end the game, it enables all the controls, and moves all of cactuses and pterodactyls
    :param keys:
    :return: Nothing.
    """
    global game_on
    global score
    global pterodactyl_1
    if pygame.K_SPACE in keys:
        game_on = True

    if game_on == True:
        score += 1
        score = int(score)
        if dinosaur.y == 480:
            if pygame.K_SPACE in keys:
                dinosaur.yspeed = -23.0005
                dinosaur.y = dinosaur.y + dinosaur.yspeed + 10
        if dinosaur.y != 480:
            dinosaur.yspeed += 1
            dinosaur.y = dinosaur.y + dinosaur.yspeed
        if dinosaur.touches(ground):
            dinosaur.yspeed = 0
            dinosaur.y = 480
        if dinosaur.right_touches(cactus_1) or dinosaur.bottom_touches(cactus_1):
            game_on = False
        if dinosaur.touches(pterodactyl_1):
            game_on = False
        if dinosaur.right_touches(cactus_2) or dinosaur.bottom_touches(cactus_2):
            game_on = False
        if dinosaur.right_touches(cactus_3) or dinosaur.right_touches(cactus_3):
            game_on = False
        if cactus_1.x < -200:
            cactus_1.x += random.randint(1800,2000)
        if cactus_2.x < -300:
            cactus_2.x += random.randint(1800,2000)
        if cactus_3.x < -400:
            cactus_3.x += random.randint(1800,2000)
        if pterodactyl_1.x < -1500:
            pterodactyl_1.y = random.randint(100,600)
            pterodactyl_1.x += 3000

        if game_on == False:
            score = 0
            cactus_1.x = 600
            cactus_2.x = 1200
            cactus_3.x = 1800
            dinosaur.y = 480
            pterodactyl_1.x = 1000
        if dinosaur.y == 480:
            if pygame.K_DOWN in keys:
                dinosaur.y += 30
                dinosaur.size = [60,58]
            if pygame.K_DOWN not in keys:
                dinosaur.size = [60,150]
        if game_on == True:
            cactus_1.x -= 8
            cactus_3.x -= 8
            cactus_2.x -= 8
            pterodactyl_1.x -= 8
    camera.draw(dinosaur)
    camera.draw(cactus_1)
    camera.draw(cactus_2)
    camera.draw(cactus_3)
    camera.draw(pterodactyl_1)
    camera.draw(ground)
    camera.display()
    camera.clear('grey')
    scorebox = gamebox.from_color(90,30, "black",175,35)
    score_text = gamebox.from_text(90, 30, "Score:  " + str(score),40,'white')
    camera.draw(scorebox)
    camera.draw(score_text)


gamebox.timer_loop(30, tick)
