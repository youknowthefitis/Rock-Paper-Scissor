print("Welcome to the Rock, Paper, Scissors game !\nType 0 for rock, 1 for paper, 2 for scissors ")
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
import random
rno=random.randint(0,2)
user=int(input("Enter your Choice: "))
choices=["Rock","Paper","Scissors",]
Image=[rock,paper,scissors]
n=choices[user]
m=Image[user]
a=Image[rno]
b=choices[rno]
print(f"Your Choice\n{n}\n{m}")
print(f"Computer's choice\n{b}\n{a}")
if rno==user:
  print("It's a draw")
elif rno==2 and user == 0:
  print("You won")
elif rno>user :
  print("You Lose")
else:
  print("You Won")
  
