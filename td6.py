
print("Choisissez un nombre entre 0 et 100 s'il-vous-plaît.")

# bloque l'execution tant que l'utilisateur n'appuie pas sur la touche Entrée
input()

essai_ordinateur = 42
nombre_a_été_trouvé = False

for i in range(3):
    print("Est-ce que le nombre à deviner est", essai_ordinateur, '? ')
    reponse = input("(oui/non)")

    while reponse != 'oui' and reponse != 'non':
        print("Je n'ai pas compris. Merci de répondre par oui ou par non.")
        reponse = input("(oui/non)")

    if reponse == 'oui':
        nombre_a_été_trouvé = True
        print("")
        break
    elif reponse == 'non':
        print("")


if nombre_a_été_trouvé:
    print("Super ! J'ai gagné.")
else:
    print("J'ai perdu !")

