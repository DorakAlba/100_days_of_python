from art import logo, vs
from game_data import data
import random
from replit import clear

def game():
  playing = True
  exclude = []
  print (logo)
  print("Time for game!")
  integer = random.randint(0, len(data)-1)
  exclude.append (integer)
  competer1, number1 = get_info (integer)
  while playing:
    print (competer1)
    print (vs)
    integer = give_entry(exclude)
    exclude.append (integer)
    competer2, number2 = get_info (integer)
    print(competer2)
    answer = input ("Who more popular? a or b  ").lower()
    if answer == "a":
      if number1 >= number2:
        clear()
        print (f"you right, that's {number1} vs {number2}")
        competer1, number1 = competer2, number2
      else:
        playing = False

        print (f"you wrong, that's {number1} vs {number2}")
    else:
      if number2 >= number1:
        clear()
        print (f"you right, that's {number1} vs {number2}")
        competer1, number1 = competer2, number2
      else:
        playing = False
        print (f"you wrong, that's {number1} vs {number2}")

  game()

  
def get_info(integer):
    info = f"{data[integer]['name']} is {data[integer]['description']} from {data[integer]['country']}"
    number = data[integer]['follower_count']
    return info, number


def give_entry(exlude):
  integer = random.randint(0, len(data)-1)
  return give_entry(exlude) if integer in exlude else integer

game()
