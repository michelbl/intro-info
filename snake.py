import time
import os

position = 3

os.system('clear')

plateau_de_jeu = ('.' * (position-1)) + 'X' + ('.' * (10-position))
print(plateau_de_jeu)

for i in range(7):
    time.sleep(0.5)
    os.system('clear')

    # déplace le joueur vers la droite
    position = position + 1

    plateau_de_jeu = ('.' * (position-1)) + 'X' + ('.' * (10-position))
    print(plateau_de_jeu)

print('Le jeu est fini')
