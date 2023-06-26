import time

def dec1(function):
    def exec():
        print('executing...')
        function()
        print('executed successfully!')
    return exec()

@dec1      # Now the below statement goes into the above defined decorator
def compliment():
    time.sleep(3)
    print('Irfan Is a good boy')
    time.sleep(.5)
    return
#compliment = dec1(compliment)

compliment

