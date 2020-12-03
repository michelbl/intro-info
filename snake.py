import time
import os
import random

import kbhit


kb = kbhit.KBHit()

historique_positions_x = [3]
historique_positions_y = [2]
taille_du_serpent = 1

position_pomme_x = 5
position_pomme_y = 7

score = 0

# valeurs possibles : -1 (reculer sur l'axe), 0 (ne pas bouger), 1 (avancer sur l'axe)
direction_x = 1
direction_y = 0


def visualiser_plateau(historique_positions_x, historique_positions_y, score, taille_du_serpent):
    os.system('clear')  # Sur Windows : os.system('cls')

    plateau_de_jeu = '..........\n' * 8 + 'Score : ' + str(score)

    for i in range(taille_du_serpent):
        position_x = historique_positions_x[-(i+1)]
        position_y = historique_positions_y[-(i+1)]

        index = ((position_y - 1) * 11) + (position_x - 1)
        plateau_de_jeu = plateau_de_jeu[:index] + 'X' + plateau_de_jeu[index + 1:]

    index_pomme = ((position_pomme_y - 1) * 11) + (position_pomme_x - 1)
    plateau_de_jeu = plateau_de_jeu[:index_pomme] + 'O' + plateau_de_jeu[index_pomme + 1:]

    print(plateau_de_jeu)


visualiser_plateau(
    historique_positions_x=historique_positions_x,
    historique_positions_y=historique_positions_y,
    score=score,
    taille_du_serpent=taille_du_serpent,
)

while True:
    time.sleep(0.2)

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

    ancienne_position_x = historique_positions_x[-1]
    nouvelle_position_x = ancienne_position_x + direction_x
    historique_positions_x.append(nouvelle_position_x)

    ancienne_position_y = historique_positions_y[-1]
    nouvelle_position_y = ancienne_position_y + direction_y
    historique_positions_y.append(nouvelle_position_y)

    if (nouvelle_position_x < 1) or (nouvelle_position_x > 10):
        print("Le joueur a pris un mur à gauche ou à droite !")
        break

    if (nouvelle_position_y < 1) or (nouvelle_position_y > 8):
        print("Le joueur a pris un mur en haut ou en bas !")
        break

    if ((nouvelle_position_x == position_pomme_x) and (nouvelle_position_y == position_pomme_y)):
        # changer la position de la pomme
        while ((nouvelle_position_x == position_pomme_x) and (nouvelle_position_y == position_pomme_y)):
            position_pomme_x = random.randint(1, 10)
            position_pomme_y = random.randint(1, 8)

        # rajouter un point au joueur
        score = score + 1

        taille_du_serpent = taille_du_serpent + 1

    visualiser_plateau(
        historique_positions_x=historique_positions_x,
        historique_positions_y=historique_positions_y,
        score=score,
        taille_du_serpent=taille_du_serpent,
    )

print('Le jeu est fini')
