import random

def main():
  number_debug = 0 #1 to show, 0 to hide

  number_min = 1
  number_max = 99
  number = random.randint(number_min,number_max)

  #number_players = int(input('How many players? (2-4)'))
  #number_playerlist = ["A", "B", "C", "D"]

  #while number_players < 2 or number_players >4:
    #number_players = int(input('You can only have 2-4 players. How many players?'))

  #print(f'Great! We have {number_players} players today!')

  if number_debug == 1:
    print(f'Secret number {number} has been initialized!')
  else:
    print('Secret number has been initialized!')
  number_guess = int(input(f'Guess the number ({number_min} to {number_max}):'))

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
      print(f'You lose! The number was {number}!')

if __name__== "__main__":
  main()
