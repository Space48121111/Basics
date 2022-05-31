import getch
import threading # a separate flow of execution
import time

global turned
global stop
turned = False
stop = False
def turn_signal():
    amount = 5

    while amount != 3: # bool amount == 9
        print('Tick')
        amount -= 1

def drive():
    global turned
    global stop
    while True:
        key = getch.getch() # ord() 97 115 120
        print('\n\rKey pressed: ', key)
        # print(type(key)) # str
        if key == 'a':
            print('\n\rLEFT')
            # turn_signal()
            turned = True
        elif key == 's':
            print('\n\rRIGHT')
            # turn_signal()
            turned = True
        elif key == 'x':
            print('X pressed, program exits.')
            stop = True
            break

def turn():
    global turned
    global stop
    while True:
        amount = 0
        if turned:
            while amount != 3: # bool amount == 9
                print('\nTick', turned)
                time.sleep(1)
                amount += 1
            turned = False
        elif stop:
            break

threading.Thread(target = drive).start()
threading.Thread(target = turn).start()




# end
