
mois_de_l_annee = [
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre",
]

print(mois_de_l_annee)

jours_de_la_semaine = [
    "lundi",
    "mardi",
    "mercredi",
    'jeudi',
    "vendredi",
    "samedi",
    "dimanche",
]

print(jours_de_la_semaine)

entiers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
entiers_autre_maniere = list(range(10))

print(entiers)
print(entiers_autre_maniere)

mois_numero_3 = mois_de_l_annee[3]
print('Ceci est un "message" !')
print("Le type de mois_numero_3 est : " + str(type(mois_numero_3)))
print("Le mois d'index 3 est : " + mois_numero_3)
print("Le mois d'index 3 est :", mois_numero_3)
print("argument1", "argument2", 42, [1,4,7], {"clef": "valeur"})

jour_numero_3 = jours_de_la_semaine[3]
print("Le jour d'index 3 est :", jour_numero_3)

entier_numero_3 = entiers[3]
print("L'entier d'index 3 est :", entier_numero_3)

print('Tranche de liste entre 2 et 4 :', mois_de_l_annee[2:4])
print("Tranche de liste après l'index 2 :", mois_de_l_annee[2:])
print("Tranche de liste contenant les 3 derniers éléments :", mois_de_l_annee[-3:])
print('Tranche de liste contenant les 3 permiers éléments :', mois_de_l_annee[:3])
