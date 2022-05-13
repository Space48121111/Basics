
while True:
    try:
        num = int(input('How old is your dog? '))
        if num == 0:
            print("Your dog can't be age 0, can she?'")
        elif 0 < num < 5:
            print('Your puppy is so cute!')
        elif 5 <= num <= 10:
            print('Your dog is entering into adulthood.')
        else:
            print('Your old dog still looks cute.')
    except ValueError:
        print('Give me an integer number, plz.')
        continue
    except KeyboardInterrupt:
        print('\n\tStart all over again.')
        break
