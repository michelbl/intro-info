
print("Choisissez un nombre entre 0 et 100 s'il-vous-plaît.")

# bloque l'execution tant que l'utilisateur n'appuie pas sur la touche Entrée
input()

essai_ordinateur = 42

print("Est-ce que le nombre à deviner est", essai_ordinateur, '? ')
reponse = input("(oui/non)")

while reponse != 'oui' and reponse != 'non':
    print("Je n'ai pas compris. Merci de répondre par oui ou par non.")
    reponse = input("(oui/non)")

if reponse == 'oui':
    print("Super ! L'ordinateur a gagné.")
elif reponse == 'non':
    print("Je vais réessayer.")

    print("Est-ce que le nombre à deviner est", essai_ordinateur, '? ')
    reponse = input("(oui/non)")

    while reponse != 'oui' and reponse != 'non':
        print("Je n'ai pas compris. Merci de répondre par oui ou par non.")
        reponse = input("(oui/non)")

    if reponse == 'oui':
        print("Super ! L'ordinateur a gagné.")
    elif reponse == 'non':
        print("Je vais réessayer.")

        print("Est-ce que le nombre à deviner est", essai_ordinateur, '? ')
        reponse = input("(oui/non)")

        while reponse != 'oui' and reponse != 'non':
            print("Je n'ai pas compris. Merci de répondre par oui ou par non.")
            reponse = input("(oui/non)")

        if reponse == 'oui':
            print("Super ! L'ordinateur a gagné.")
        elif reponse == 'non':
            print("Je vais réessayer.")
