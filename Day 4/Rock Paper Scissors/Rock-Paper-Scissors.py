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

#Write your code below this line 👇

#Your choice
list_of_choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"{list_of_choices[user_choice]}")

#Computer choice
computer_choice = random.randint(0, len(list_of_choices)-1)
print(f"Computer chose:\n{list_of_choices[computer_choice]}")

#Comparison
if user_choice == 0 :
  if computer_choice == 0 :
    print("You drew!")
  elif computer_choice == 1:
    print("You lose!")
  else :
    print("You win!")
elif user_choice == 1 :
  if computer_choice == 0 :
    print("You win")
  elif computer_choice == 1:
    print("You drew!")
  else :
    print("You lose!")
else :
  if computer_choice == 0 :
    print("You lose")
  elif computer_choice == 1:
    print("You win!")
  else :
    print("You drew!")