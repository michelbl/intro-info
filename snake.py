import time
import os

import kbhit


kb = kbhit.KBHit()

position = 3

os.system('clear')  # Sur Windows : os.system('cls')

plateau_de_jeu = ('.' * (position-1)) + 'X' + ('.' * (10-position))
print(plateau_de_jeu)

while True:
    time.sleep(0.01)
    os.system('clear')

    # on souhaite savoir si le joueur a appuyé sur une touche
    if kb.kbhit():

        caractère_frappé = kb.getch()
        code_du_caractère = ord(caractère_frappé)
        if caractère_frappé == 'd':
            position = position + 1
        elif caractère_frappé == 'g':
            position = position - 1

    if (position < 1) or (position > 10):
        print("Le joueur a pris un mur !")
        break

    plateau_de_jeu = ('.' * (position-1)) + 'X' + ('.' * (10-position))
    print(plateau_de_jeu)

print('Le jeu est fini')
