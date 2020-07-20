import random

user_choice = input('ROCK, PAPER or SCISSORS')
computer_choice = random.choice(['ROCK', 'PAPER', 'SCISSORS'])

print(f'{user_choice} vs {computer_choice}')

if user_choice == computer_choice:
    result = 'It\'s a draw...'
elif (user_choice, computer_choice) in [('ROCK', 'SCISSORS'),
                                        ('SCISSORS', 'PAPER'),
                                        ('PAPER', 'ROCK')]:
    result = 'You Win!'
else:
    result = 'Computer Wins...'

print(result)
