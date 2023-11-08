import random

art = [r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
play_table = ["Rock", "Paper", "Scissors"]
victory_table = [2, 0, 1]

player_choice = int(input("Rock (0), paper (1) or scissors (2)?\n"))
cpu_choice = random.randint(0,2)

print("You played " + play_table[player_choice])
print(art[player_choice])
print("The computer played " + play_table[cpu_choice])
print(art[cpu_choice])


if player_choice == cpu_choice:
    print ("Draw")
elif cpu_choice == victory_table[player_choice]:
    print("You won")
else:
    print("You lose")
