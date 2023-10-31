#ajk5qv cjo6pn
import gamebox
import pygame
p1 = gamebox.from_color(0, 250, "blue", 40, 40)
p2 = gamebox.from_color(0, 200, "red", 40, 40)
safety_line = gamebox.from_color(50,600,"white",10,1300)
finish_line = gamebox.from_color(750,600,"white",10,1300)
scorebox = gamebox.from_color(90, 30, "black", 175, 35)
camera = gamebox.Camera(800,600)
game_on = False
def starting_screen():
    instructions_line1 = gamebox.from_text(400, 100,"P1(Blue) is trying to get across the finish line without being tagged or touching any obstacles", 25, 'black')
    instructions_line2 = gamebox.from_text(400,200,"P2(Red) is trying to tag player 1", 25,'black')
    instructions_line3 = gamebox.from_text(400, 400, "Press Space to Start",40,'black')
    names = gamebox.from_text(400, 20, "Alec (ajk5qv)  and Chris (cjo6pn)",40,'black')
    game_name = gamebox.from_text(400, 60, "Tag 2.0",40,'black')
    instructions_for_game = gamebox.from_text(400, 300, "Player 1 move with WASD Player 2 move with arrows",40,'black')
    camera.clear('grey')
    camera.draw(instructions_for_game)
    camera.draw(game_name)
    camera.draw(names)
    camera.draw(instructions_line1)
    camera.draw(instructions_line2)
    camera.draw(instructions_line3)
    camera.display()
if game_on == False:
    starting_screen()
def tick(keys):
    global game_on
    global timer
    if game_on == False:
        timer = 400
        if pygame.K_SPACE in keys:
            game_on = True

    if pygame.K_SPACE in keys:
        game_on = True
    if game_on == True:
        timer += -1
        if pygame.K_w in keys:
            p1.move(0, -4)
        if pygame.K_a in keys:
            p1.move(-4, 0)
        if pygame.K_d in keys:
            p1.move(4, 0)
        if pygame.K_s in keys:
            p1.move(0, 4)
        if pygame.K_UP in keys:
            p2.move(0, -3)
        if pygame.K_DOWN in keys:
            p2.move(0, 3)
        if pygame.K_LEFT in keys:
            p2.move(-3, -0)
        if pygame.K_RIGHT in keys:
            p2.move(3, -0)
    if game_on == True:
        camera.draw(p1)
        camera.draw(p2)
        camera.draw(safety_line)
        camera.draw(finish_line)
        camera.draw(scorebox)
        timer_text = gamebox.from_text(90, 30, "Timer:  " + str(timer), 40, 'white')
        camera.draw(timer_text)
        camera.display()
        camera.clear('black')
    if game_on == False:
        p1.x = 0
        p1.y = 250
        p2.x = 0
        p2.y = 200
    if p1.x > 800 or p1.x < 0 or p1.y > 600 or p1.y < 0:
        game_on = False
        camera.clear('Green')
        out_message = gamebox.from_text(400, 200, "OUT OF BOUNDS, START OVER" ,70,'white')
        camera.draw(out_message)
        camera.display()
    if p1.touches(finish_line):
            game_on = False
            camera.clear('blue')
            winning_message = gamebox.from_text(400, 200, "Player 1 Wins!" ,100,'white')
            camera.draw(winning_message)
            camera.display()
            if pygame.K_SPACE in keys:
                game_on = True
    if timer == 0:
            game_on = False
            camera.clear('red')
            losing_message1 = gamebox.from_text(400, 200, "Player 2 Wins", 100, 'white')
            camera.draw(losing_message1)
            camera.display()
            if pygame.K_SPACE in keys:
                game_on = True
    if p1.touches(p2) and p1.x > 70:
            game_on = False
            camera.clear('red')
            losing_message1 = gamebox.from_text(400, 200, "Player 2 Wins", 100, 'white')
            camera.draw(losing_message1)
            camera.display()
            if pygame.K_SPACE in keys:
                game_on = True
gamebox.timer_loop(30, tick)








