import time
import os
import random

import kbhit


kb = kbhit.KBHit()

position_x = 3  # le personnage est sur la 3e colonne
position_y = 2  # le personnage est sur la 2e ligne

position_pomme_x = 5
position_pomme_y = 7

score = 0

# valeurs possibles : -1 (reculer sur l'axe), 0 (ne pas bouger), 1 (avancer sur l'axe)
direction_x = 1
direction_y = 0


def visualiser_plateau(position_x, position_y, score):
    os.system('clear')  # Sur Windows : os.system('cls')

    plateau_de_jeu = '..........\n' * 8 + 'Score : ' + str(score)

    index = ((position_y - 1) * 11) + (position_x - 1)
    plateau_de_jeu = plateau_de_jeu[:index] + 'X' + plateau_de_jeu[index + 1:]

    index_pomme = ((position_pomme_y - 1) * 11) + (position_pomme_x - 1)
    plateau_de_jeu = plateau_de_jeu[:index_pomme] + 'O' + plateau_de_jeu[index_pomme + 1:]

    print(plateau_de_jeu)


visualiser_plateau(position_x=position_x, position_y=position_y, score=score)

while True:
    time.sleep(0.1)

    # on souhaite savoir si le joueur a appuyé sur une touche
    if kb.kbhit():

        caractère_frappé = kb.getch()
        code_du_caractère = ord(caractère_frappé)

        if caractère_frappé == 'd':
            direction_x = 1
            direction_y = 0

        elif caractère_frappé == 'q':
            direction_x = -1
            direction_y = 0

        elif caractère_frappé == 'z':
            direction_x = 0
            direction_y = -1

        elif caractère_frappé == 's':
            direction_x = 0
            direction_y = 1

    position_x = position_x + direction_x
    position_y = position_y + direction_y

    if (position_x < 1) or (position_x > 10):
        print("Le joueur a pris un mur à gauche ou à droite !")
        break

    if (position_y < 1) or (position_y > 8):
        print("Le joueur a pris un mur en haut ou en bas !")
        break

    if ((position_x == position_pomme_x) and (position_y == position_pomme_y)):
        # changer la position de la pomme
        while ((position_x == position_pomme_x) and (position_y == position_pomme_y)):
            position_pomme_x = random.randint(1, 10)
            position_pomme_y = random.randint(1, 8)

        # rajouter un point au joueur
        score = score + 1

    visualiser_plateau(position_x=position_x, position_y=position_y, score=score)

print('Le jeu est fini')
