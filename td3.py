
## Listes

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

jours_inversés = list(reversed(jours_de_la_semaine))
print("Jours de la semaine inversés :", jours_inversés)

"""
# Autres méthodes :

jours_de_la_semaine.reverse()
print("Les jours inversés sont :", jours_de_la_semaine)
"""

"""
jours_inversés_2e_methode = jours_de_la_semaine[::-1]
print("Les jours inversés sont :", jours_inversés_2e_methode)

jours_de_la_semaine_impairs = jours_de_la_semaine[::2]
print("Les jours impais sont :", jours_de_la_semaine_impairs)
"""

print("Caractère d'index 5 :", "Bonjour !"[5])
print("Fin de chaîne de caractères :", "Bonjour !"[3:])
print("Chaînede caractère inversée :", "Bonjour !"[::-1])

print("Nombre de mois dans l'année :", len(mois_de_l_annee))

## Dictionnaires

nb_jours = {
    "janvier": 31,
    "février": 28,
    "mars": 31,
    "avril": 30,
    "mai": 31,
    "juin": 30,
    "juillet": 31,
    "août": 31,
    "septembre": 30,
    "otobre": 31,
    "novembre": 30,
    "décembre": 31,
}

print(nb_jours)

jours_travaillés = {
    'lundi': True,
    'mardi': True,
    'mercredi': True,
    'jeudi': True,
    'vendredi': True,
    'samedi': False,
    'dimanche': False,
}

print(jours_travaillés)

doubles = {
    0: 0,
    1: 2,
    2: 4,
    3: 6,
    4: 8,
    5: 10,
    6: 12,
    7: 14,
    8: 16,
    9: 18,
}

print(doubles)

print("Mars compte", nb_jours["mars"], "jours.")

print("Jeudi est-il travaillé ? :", jours_travaillés["jeudi"])

if jours_travaillés["jeudi"]:
    print("Jeudi est travaillé")
else:
    print("Jeudi n'est pas travaillé")

print("Le double de 6 est ", doubles[6])

print("Nombre d'éléments dans le dictionnaire nb_jours :", len(nb_jours))
