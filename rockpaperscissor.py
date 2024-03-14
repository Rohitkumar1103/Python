import random

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >=3 or user <0:
  print("You typed an invalid number,You Loose")
else:
  print(game_images[user])

  computer = random.randint(0,2)

  print("Computer chose:")
  print(game_images[computer])

  if user == 0 and computer == 2:
    print("You Win!")
  elif computer == 0 and user == 2:
    print("You Loose")
  elif computer > user:
    print("You Loose")
  elif user > computer:
    print("You Win!")
  elif computer ==user :
    print("It is a tie")