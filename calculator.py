# import random

def calculator(num1, num2):
    try:
        sum = num1 + num2
        product = num1 * num2
        diff = num1 - num2
        print('Your sum is ', sum)
        print('Your product is ', product)
        print('Your difference is ', diff)
    except KeyboardInterrupt:
        print('\nHave a nice day!')

n1, n2 = [float(x) for x in input('Please \
enter 2 numbers(separate them by space): ').split()]
calculator(n1, n2)



def points():
    while True:
        try:
            inp = input('Give me an integer point number: ').strip()
            if int(inp) < 10:
                print('Oops, your point is below the average.', inp)
                continue
            else:
                print('Well done.', inp)
                break
        except ValueError:
            print('Invalid input.', inp)
        except KeyboardInterrupt:
            print('\nHave a nice day!')
            break

# points()


'''
try:
    while True:
        num = random.randint(1, 2)
        guess = int(input('Please enter a number: '))
        if guess == num:
            print('Yay, you nailed it.', num)
        else:
            print("You can't even get the head and tail right.", num)
except KeyboardInterrupt:
    print('\nHave a nice day!')
'''


# end
