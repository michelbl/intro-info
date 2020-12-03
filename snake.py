import time
import os

import kbhit


kb = kbhit.KBHit()

position_x = 3  # le personnage est sur la 3e colonne
position_y = 2  # le personnage est sur la 2e ligne


def visualiser_plateau(position_x, position_y):
    os.system('clear')  # Sur Windows : os.system('cls')

    plateau_de_jeu = ''

    for i in range(position_y-1):
        plateau_de_jeu = plateau_de_jeu + '..........\n'

    plateau_de_jeu = plateau_de_jeu + ('.' * (position_x-1)) + 'X' + ('.' * (10-position_x)) + '\n'

    for i in range(8-position_y):
        plateau_de_jeu = plateau_de_jeu + '..........\n'
    
    print(plateau_de_jeu)


visualiser_plateau(position_x=position_x, position_y=position_y)

while True:
    time.sleep(0.1)

    # on souhaite savoir si le joueur a appuyé sur une touche
    if kb.kbhit():

        caractère_frappé = kb.getch()
        code_du_caractère = ord(caractère_frappé)
        if caractère_frappé == 'd':
            position_x = position_x + 1
        elif caractère_frappé == 'q':
            position_x = position_x - 1

    if (position_x < 1) or (position_x > 10):
        print("Le joueur a pris un mur à gauche ou à droite !")
        break

    if (position_y < 1) or (position_y > 8):
        print("Le joueur a pris un mur en haut ou en bas !")
        break

    visualiser_plateau(position_x=position_x, position_y=position_y)

print('Le jeu est fini')
