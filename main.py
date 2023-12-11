# Roche papier Ciseaux

import random

rpcimg = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

rcplist = ['Roche', 'Papier', 'Ciseau']

print("Bienvenue à Roche Papier Ciseau! ")

cpu = random.randint(0, 2)

user = int(input("choisir 0 pour Roche, 1 pour Papier, 2 pour ciseaux: "))

print(f"Vous avez choisi : {rcplist[user]}")
print(rpcimg[user])
print(f"L'ordinateur à choisi : {rcplist[cpu]}")
print(rpcimg[cpu])

if(user == cpu):
    print("Égalité")
elif(user == 0 and cpu == 2):
    print("Vous gagnez!")
elif(user == 1 and cpu == 0):
    print("Vous gagnez!")
elif(user == 2 and cpu == 1):
    print("Vous gagnez!")
else:
    print("Vous avez perdu!")
