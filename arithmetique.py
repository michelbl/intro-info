
liste_des_stations = [
    "Bibliothèque François-Mitterrand",
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

for station in liste_des_stations:
    print(station)

    somme = 0

    for caractere in station:
        caractere_majuscule = caractere.upper()

        if ord(caractere_majuscule) in range(65,91): # Tests si caractere_majuscule est bien une lettre
            somme = somme + ord(caractere_majuscule)-64
        else:
            print("Le caractère", caractere_majuscule, "n'est pas reconnu.")

    print(somme)
