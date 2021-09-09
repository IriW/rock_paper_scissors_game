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
#Choices List
game_images = [rock, paper, scissors]

#getting user input
choice_request = int(input("Type '0' for Rock, '1' for Paper or '2' for Scissors:\n"))

if choice_request < 0 or choice_request >= 3:
    print("Wrong value chosen. You lost!")
else:
    print(f"User choice is: {game_images[choice_request]}")
    #Random choice made by machine
    machine_choices = random.randint(0, 2)
    print(f"Machine choice is: {game_images[machine_choices]}")
    if machine_choices  == choice_request:
        print("It's a Draw!")
    elif choice_request == 0 and machine_choices == 2:
        print("You won!")
    elif choice_request == 2 and machine_choices == 0:
        print("You lost!")
    elif machine_choices > choice_request:
        print("You lost!")
    elif machine_choices < choice_request:
        print("You won!")
    else:
        print("You most probably won.")