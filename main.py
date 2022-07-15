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

game_images = [rock, paper, scissors]
your_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors. \n"))
print(game_images[your_choice])
cpu_choice = random.randint(0,2)
print(game_images[cpu_choice])

if your_choice >= 3 or your_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif your_choice == 0 and cpu_choice == 2:
  print("You win!")
elif cpu_choice == 0 and your_choice == 2:
  print("You lose")
elif cpu_choice > your_choice:
  print("You lose")
elif your_choice > cpu_choice:
  print("You win!")
elif cpu_choice == your_choice:
  print("It's a draw")