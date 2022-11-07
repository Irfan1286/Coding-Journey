# Its used from functools lrucache

from functools import lru_cache
import time

@lru_cache(maxsize=3)   # maxsize = 3 means that the line will check if that same fuction has been run within the
def some_task(num):     # previous 3 same command
    for i in range(num):
        print(i)
    time.sleep(2)

if __name__ == '__main__':
    print('This task is running...')
    some_task(5)
    print('This task is running again...')
    some_task(3)
    print('This is running one last time...')
    some_task(4)
    print('next...')
    some_task(2)

