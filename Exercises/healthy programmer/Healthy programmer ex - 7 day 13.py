# Healthy Programmer
#  a worker works from 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log      Every 30 min 220ml
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

from pygame import mixer
import time

timing = time.strftime('%H: %M: %S', time.localtime())
start = '09: 00: 00'
end = '17: 00: 00'

minute = time.strftime('%M', time.localtime())

def music(file, requiredinp):   # plays music
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(50)    # The int in () is number of times to loop
    while True:
        user = input()
        if user == requiredinp:
            mixer.music.stop()
            break


def log(file_name, message):    # Writes to file
    with open(file_name, 'a') as file:
        file.writelines(f'[{timing}] {message}\n')
    print(message)


if __name__ == '__main__':
    eyes_time = time.time()     # this initializes starting time
    water_start = time.time()
    exercise_start = time.time()
    while timing > start and timing < end:
        if time.time() - water_start > 20:    # It's used to find how much time has passed and
            print('Type "Done" and enter to stop alarm')
            water_start = time.time()  # THis resets the init_time again
            music('water.mp3', 'Done')
            log('Health.txt', 'DRANK WATER')

        if time.time() - exercise_start > 2700:    # the integer is the difference
            print('Type "Done" and enter to stop alarm')
            exercise_start = time.time()
            music('Exercise.mp3', 'Done')
            log('Health.txt', 'You have done the Exercise')

        if time.time() - eyes_time > 1800:    # the integer is the difference
            print('Type "Done" and enter to stop alarm')
            eyes_time = time.time()
            music('eyes.mp3', 'Done')
            log('Health.txt', 'Eyes Exercise Performed')
