# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:23:31 2019

@author: Edu
"""
import os
# raw_input() is used to define inputs in older versions of python, and is the
# one that works on the RaspberryPi. In the computer use input().

def menu():
    # Main menu of the rover modes. 
    print('Stand-by Mode')
    choice = raw_input()
    if choice == 'locomotion': 
        # Enters Locomotion mode
        loco()
    if choice == 'camera':
	activate_camera()
	menu()
    else:
        # If invalid choice of mode
        print('Invalid mode. Do you want to exit? y/n')
        choice = raw_input()
        if choice == 'n': # Remain
            menu()
        elif choice == 'y': # Exit 
            return
        else: # Invalid value, exit program
            print('Invalid choice. Exiting program')
            return

def activate_camera():
    # Start camera daemon
    os.system("sudo systemctl start camera.service")

    
def loco():
    # Locomotion mode
    print('Locomotion Mode')
    move = True # True to stay in the mode False to return to the main menu
    choices = ('w','a','s','d') # only four choices to move
    while move == True:
        choice = raw_input() # Select movement
        if choice in choices:
            print(choice)
        else:
            print('Invalid choice! Exit locomotion mode? y/n')
            choice = raw_input()
            if choice == 'y': # Exit locomotion mode
                move = False
            elif choice == 'n': # Remain in locomotion mode
                move = True
            else: # Invalid value, returns to main menu
                print('Invalid choice. Returning to main menu')
                move = False  
    # When move = False we exit the loop end go back to the main menu
    menu()
