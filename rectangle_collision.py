""" RectangleRun is a simple game made in python for  beginners for learning.This repo can be used as a base for other games
"""
#import libary
from pyray import *
import math
#define basic variables
screen_height = 600
screen_width = 600
posx = 50 #position of enemy
posy = 50
posx1 = 350 # position of player
posy1 = 250
width = 80
height = 60 # dimensions for enemy
width1 = 80
height1 = 60 # dimensions for player
is_collided = False # for collision
is_selected = False
mode_speed = 0 #speed selected for difficulty
speed = 0 #speed for enemy
time = get_time() # time for speed caculation and score
score = 0 #score
set_target_fps(60)
init_window(screen_height,screen_width, "raylib")

def collision(posx,posy,posx1,posy1,width,height,width1,height1): # This is the fuction that calcuates collision using AABB (explation will be given at the end)
     if (posx < posx1 + width1 and
        posx + width > posx1 and
        posy < posy1 + height1 and
        posy + height > posy1):
        return True
     return False   

while not window_should_close():
    begin_drawing()
    clear_background(RED)
    if is_selected == False: #basic menu if condition
         draw_text("press Easy(E) OR Hard(H)",0,40,40,WHITE)
         if is_key_down(KEY_E):
              mode_speed = 1 # changes speed to default 1 for easy mode
              is_selected = True
              
         if is_key_down(KEY_H):
              mode_speed = 2 # changes speed to default 2 for hard mode
              is_selected = True
              

    if is_selected == True: # condition to continue after selecting mode

         if is_collided == False: # this block of code will run the whole game as long as the rectangles have not collided
             # movement logic for player
             if is_key_down(KEY_W):posy1 -= 5
             if is_key_down(KEY_S):posy1 += 5
             if is_key_down(KEY_A):posx1 -= 5
             if is_key_down(KEY_D):posx1 += 5
             # boundairy logic for player
             if posx1 > screen_width - width1 :posx1 = screen_width - width1
             if posy1 > screen_height - height1 :posy1 = screen_height - height1
             if posy1 < 0: posy1 = 0
             if posx1 < 0: posx1 = 0
             # Basic AI for the enemy. it just adds speed to the position to match the position of player
             if posx1 > posx:posx += speed
             if posx1 < posx:posx -= speed
             if posy1 > posy:posy += speed
             if posy1 < posy:posy -= speed

         
         

         if is_collided == False:# condition to draw the enemy and player
              draw_rectangle(posx,posy,width,height,WHITE)
              draw_rectangle(posx1,posy1,width1,height1,BLUE)

         is_collided = collision(posx,posy,posx1,posy1,width,height,width1,height1)

         if is_collided == True: # the menue or options after losing
              clear_background(RED)
              draw_text(F"score: {score}",50,50,50,WHITE)
              draw_text("press R to restart",50,100,50,WHITE)
              if is_key_down(KEY_R): #resets every single variable to default hence restarting the game
                   posx = 50
                   posy = 50
                   posx1 = 350
                   posy1 = 250
                   width = 80
                   height = 60
                   width1 = 80
                   height1 = 60
                   is_collided = False
                   is_selected = False
                   speed = 1
                   time = get_time()
                   score = 0

         

         if is_collided == False: score = int(get_time() - time)# this line is used to calcuate score
         if is_collided == False: speed = mode_speed + int(score / 2 ) # used to increase score. speed is derived from score and according to difficulty selected
         if speed < 1: speed = 1# sets minmum speed for enemy
         elif speed > 4:speed = 4# sets max speed for enemy
     

    end_drawing()
close_window()
"""
Think of AABB (Axis-Aligned Bounding Box) collision as a quick way to check if two non-rotated boxes(if rotation enters the chat things get angry and complex) are touching by looking for the empty space between them rather than the collision itself.

The computer simply compares the boundaries of the two rectangles, asking four questions: is the first box entirely to the left, entirely to the right, entirely above, or entirely below the second box? If the answer to all four questions is "no"—meaning there is no gap separating them horizontally and no gap separating them vertically—then the computer knows for a fact that the two shapes must be crashing into each other.
"""
"""
This is a learning project, so it may contain bugs or logical loopholes. I am constantly working to improve it and would love to hear your contribution to the repo. Thanks for your time checking out my code !
"""
