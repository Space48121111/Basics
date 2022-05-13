import getch
# import curses
# import time

# real-time
while True:
    key = getch.getch() # ord() 97 115 120
    print('\n\rKey pressed: ', key)
    # print(type(key)) # str
    if key == 'a':
        print('\n\rLEFT')
    elif key == 's':
        print('\n\rRIGHT')
    if key == 'x':
        break

    # time.sleep(1)


'''
win = curses.initscr()
while True:
    key = win.getch()
    print('\n\rKey pressed: ', key) # \r carriage return
    if key == 97: # a
        print('Turn left.\n\r')
    if key == 115: # s
        print('Turn right.\n\r')
    elif key == 120: # x
        break
'''


# func argument
def name(name1, name2):
    print('How are you? ', name1, '', name2)

'''
first_name = input('Please give me your first name: \n')
last_name = input('Please give me your last name: \n')
name(first_name, last_name)
'''


# func parameter
def calculator(x, y, z):
    return x + y + z

# print('The sum of your values is ', calculator(3, 6, 1))




# end
