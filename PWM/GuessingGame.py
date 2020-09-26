num=9
guessCount=0
maxGuess=3
while guessCount<maxGuess:
    gus=int(input('Enter the num'))

    if gus==num:
        print('Right')
        break
    guessCount += 1

else:
    print('You loss')
