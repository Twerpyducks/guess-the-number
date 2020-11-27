import random

def main():
  number_debug = 0 #1 to show, 0 to hide

  number_min = 1
  number_max = 99
  number = random.randint(number_min,number_max)

  number_players = int(input('How many players? (2-4)'))

  while number_players < 2 or number_players >4:
    number_players = int(input('You can only have 2-4 players. How many players?'))

  print(f'Great! We have {number_players} players today!')

  if number_debug == 1:
    print(f'Secret number {number} has been initialized!')
  else:
    print('Secret number has been initialized!')
  number_guess = int(input(f'Guess the number ({number_min} to {number_max})'))

  while number != number_guess:
    if number_guess < number_min:
      print(f'You number cannot be less than {number_min}. Try again!')
    elif number_guess > number_max:
      print(f'You number cannot be more than {number_max}. Try again!')
    else:
      if number_guess < number:
        number_min = number_guess
      else:
        number_max = number_guess
      print('Wrong guess! Next player!')
    number_guess = int(input(f'Guess the number ({number_min} to {number_max})'))

    if number_guess == number:
      print(f'You got it right! The number was {number}!')



  # dice_rolls = int(input('How many dice would you like to roll? '))
  # dice_size = int(input('How many sides are the dice? '))
  # dice_sum = 0
  # for i in range(0,dice_rolls):
  #   roll = random.randint(1,dice_size)
  #   dice_sum += roll
  #   if roll == 1:
  #     print(f'You rolled a {roll}! Critical Fail')
  #   elif roll == 6:
  #     print(f'You rolled a {roll}! Critical Success!')
  #   else:
  #     print(f'You rolled a {roll}')
  # print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
