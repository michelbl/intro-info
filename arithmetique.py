

mot = [
    "Bibliothèque François-Mitterrand"
    "Campo-Formio",
    "Chevaleret",
    "Corvisart",
    "Gare d'Austerlitz",
    "Glacière",
    "Les Gobelins",
    "Maison Blanche",
    "Nationale",
    "Olympiades",
    "Place d'Italie",
    "Porte de Choisy",
    "Porte d'Italie",
    "Porte d'Ivry",
    "Quai de la Gare",
    "Saint-Marcel",
    "Tolbiac",
]


# 2 + 3 + 3 + 1 + 2 = 11

dict_lettre = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
}

# liste des lettres de A à Z
# entiers de 1 à 26
# assembler ces 2 listes pour faire un dictionnaire

# Provoque nue exception KeyError
#dict_lettre[mot]

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