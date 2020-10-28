import random
secret = random.randint(1, 99)
guess = 0
tries = 0

print('Hey! I am the Dread Pirate Roberts, and I have a secret!')
print('it is a number from 1 to 99. I will give you 6 tries.')

while guess != secret and tries < 6:
    guess = int(input('What is your guess?'))
    if guess < secret:
        print('Your guess is lower than my secret')
    elif guess > secret:
        print('Your guess is higer than my secret')


    tries = tries + 1

if guess == secret:
        print('Wow! You got it! you found my secret!')
else:
        print('No more Guesses! Better Luk next time')
        print('The secret number was', secret)
        input('아무키나 눌러 종료하십시오')
