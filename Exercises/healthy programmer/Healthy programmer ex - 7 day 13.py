# Healthy Programmer
#  a worker works from 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log      Every 30 min 220ml
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

import pygame
import time

t = time.strftime('%H: %M: %S')
start = '09: 00: 00'
end = '17: 00: 00'

pygame.mixer.init()


if t >= start and t <= end:
    count = 0
    while count < 1:
        user = 8
        while user != 'drank':
            time.sleep(5)
            pygame.mixer.music.load('water.mp3')
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()







