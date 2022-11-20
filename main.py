import random

def game():
    botNum = random.randint(1, 6)
    print('I made up a number')
    playerNum = int(input('Write your number: '))

    if botNum == playerNum:
        print('You win! I guessed', playerNum, '!')
    else:
        print('Provaleno! I guessed', botNum)
    return


print('Welcome to Bones-game!')
print('Start game?')

while True:
    playerActive = input()

    if playerActive == 'yes':
        game()
        break
    elif playerActive == 'Exit':
        break
    else:
        game()

    print('Try again')
