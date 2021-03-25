#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import keyboard
import pygame


pygame.init()
window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Pygame Demonstration")

GPIO.setmode(GPIO.BCM)


#GPIO.output(5, GPIO.LOW)
#GPIO.output(6, GPIO.LOW)
#GPIO.output(13, GPIO.LOW)
#GPIO.output(19, GPIO.
mainloop=True
while mainloop:

    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            mainloop = False
        
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
        
            if pygame.key.name(event.key) == 'w':
                GPIO.output(5, GPIO.HIGH)
                GPIO.output(6, GPIO.LOW)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(19, GPIO.LOW)
                    
            if pygame.key.name(event.key) == 's':
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.HIGH)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(19, GPIO.HIGH)
                
            if pygame.key.name(event.key) == 'a':
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.HIGH)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(19, GPIO.LOW)
                    
            if pygame.key.name(event.key) == 'd':
                GPIO.output(5, GPIO.HIGH)
                GPIO.output(6, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(19, GPIO.HIGH)
    
        if event.type == pygame.KEYUP:
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)

    
 #   GPIO.cleanup(6)
  #  GPIO.cleanup(5)
   # GPIO.cleanup(13)
    #GPIO.cleanup(19)
