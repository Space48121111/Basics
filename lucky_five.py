try:
    while True:
        inp = input('Give me a number: ')
        if inp.isdigit():
            num = int(inp)
            if num == 5:
                print('Bingo! Good job!')
                break
            elif num < 5:
                print('Your number is too low, please try again.')
            else:
                print('Your number is too high, please try again.')
        else:
            print('Invalid input.')
            continue
except:
    print('\n\tHave a nice day.')
