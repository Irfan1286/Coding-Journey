import time

c = 0
initial_t = time.time()
while c < 10:
    print('Good morning Irfan')
    time.sleep(.5)
    c += 1
print(f'program ran in {time.time() - initial_t}')      # time.time() begins timer on variable and is used to substract final time.time()
reset = time.time()
print(time.time() - reset)          # When time.time is used again it resets the timer from variable
time.sleep(1)
print(time.time() - initial_t)

localtime = time.localtime()
print(localtime)

bettertime = time.asctime(time.localtime())
print(f'this is a better time format ({bettertime})')     # time.asctime gives a nice format to display
