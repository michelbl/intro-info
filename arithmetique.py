
mot = "BCCAB"
#mot = ["B", "C", "C", "A", "B"]

# 2 + 3 + 3 + 1 + 2 = 11

dict_lettre = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
}

# liste des lettres de A à Z
# entiers de 1 à 26
# assembler ces 2 listes pour faire un dictionnaire

dict_lettre[mot]

dict_lettre['A']  # donne 1

somme = 0

for lettre in mot:
    print(lettre)
    print(dict_lettre[lettre])
    somme = somme + dict_lettre[lettre]
    print()

print(somme)

"""

print(dict_lettre['B'])
"""