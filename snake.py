import time
import os

import kbhit


kb = kbhit.KBHit()

position_x = 3  # le personnage est sur la 3e colonne
position_y = 2  # le personnage est sur la 2e ligne

position_pomme_x = 5
position_pomme_y = 7

def visualiser_plateau(position_x, position_y):
    os.system('clear')  # Sur Windows : os.system('cls')

    plateau_de_jeu = '..........\n' * 8

    index = ((position_y - 1) * 11) + (position_x - 1)
    plateau_de_jeu = plateau_de_jeu[:index] + 'X' + plateau_de_jeu[index + 1:]

    index_pomme = ((position_pomme_y - 1) * 11) + (position_pomme_x - 1)
    plateau_de_jeu = plateau_de_jeu[:index_pomme] + 'O' + plateau_de_jeu[index_pomme + 1:]

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
        elif caractère_frappé == 'z':
            position_y = position_y - 1
        elif caractère_frappé == 's':
            position_y = position_y + 1

    if (position_x < 1) or (position_x > 10):
        print("Le joueur a pris un mur à gauche ou à droite !")
        break

    if (position_y < 1) or (position_y > 8):
        print("Le joueur a pris un mur en haut ou en bas !")
        break

    visualiser_plateau(position_x=position_x, position_y=position_y)

print('Le jeu est fini')
