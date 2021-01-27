
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = ["rock", "paper", "scissor"]

player_select = int(input("Select \"0\" for \"rock\" \"1\" for \"paper\" \"2\" for \"scissor\n"))

if player_select > 2 or player_select < 0:
  print("You've selected an invalid number")
else:
  if player_select == 0:
    print(f"You've selected \n" + rock)
  elif player_select == 1:
    print(f"You've selected \n" + paper)
  elif player_select == 2:
    print(f"You've selected \n" + scissors)

  com_select = random.choice(choice)

  if com_select == "rock":
    print(f"Computer've selected \n" + rock)
  elif com_select == "paper":
    print(f"Computer've selected \n" + paper)
  elif com_select == "scissor":
    print(f"Computer've selected \n" + scissors)
  

  if player_select == 0 and com_select == "paper":
    print("You lost")
  elif player_select == 1 and com_select == "scissor":
    print("You lost")
  elif player_select == 2 and com_select == "rock":
    print("You lost")
  elif player_select == 0 and com_select == "scissor":
    print("You won")
  elif player_select == 2 and com_select == "paper":
    print("You won") 
  elif player_select == 1 and com_select == "rock":
    print("You won") 
  elif player_select == 0 and com_select == "rock":
    print("Game have tied")
  elif player_select == 1 and com_select == "paper":
    print("Game have tied")
  elif player_select == 2 and com_select == "scissor":
    print("Game have tied")

   


