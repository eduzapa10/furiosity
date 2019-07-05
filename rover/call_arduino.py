# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 01:37:11 2019

@author: Alvaro M
"""

def call_arduino():
    print('Receiving Arduino')
    #!/usr/bin/env python
    
    import serial
    
    port = "/dev/ttyACM0"
    rate = 9600
    
    s1 = serial.Serial(port,rate)
    s1.flushInput()
    
    comp_list = ["Movement complete\r\n", "Hello Pi, This is Arduino UNO... \r\n"]
    while True:
        if s1.inWaiting()>0:
            inputValue = s1.readline()
            print(inputValue)
            if inputValue in comp_list:
                try:
                    choice = input("Choose direction: w,s,a or d")
                    if choice ==  'w':
                            n = 1
                    elif choice == 's':
                            n = 2
                    elif choice == 'a':
                            n = 3
                    else:
                            n = 4
                    s1.write('%d'%n)
                except:
                    print("Input error, please input correctly")
                    s1.write('0')
                            
    
