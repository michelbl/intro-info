import random


print("Choisissez un nombre entre 0 et 100 s'il-vous-plaît.")

# bloque l'execution tant que l'utilisateur n'appuie pas sur la touche Entrée
input()

nombre_a_été_trouvé = False
nombre_posible_min = 0
nombre_possible_max = 100

for i in range(10):
    essai_ordinateur = (nombre_posible_min + nombre_possible_max) // 2

    print("Est-ce que le nombre à deviner est", essai_ordinateur, '? ')
    reponse = input("inférieur ('<'), égal ('=') ou supérieur ('>') ? ")

    while reponse != '<' and reponse != '=' and reponse != '>':
        print("Je n'ai pas compris. Merci de répondre par oui ou par non.")
        reponse = input("inférieur ('<'), égal ('=') ou supérieur ('>') ? ")

    if reponse == '=':
        nombre_a_été_trouvé = True
        print("")
        break
    elif reponse == '<':
        nombre_possible_max = essai_ordinateur - 1
        print("")
    elif reponse == '>':
        nombre_posible_min = essai_ordinateur + 1
        print("")

if nombre_a_été_trouvé:
    print("Super ! J'ai gagné.")
else:
    print("J'ai perdu !")
