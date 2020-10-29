# Pour une liste de nombres, comment calculer la somme des nombres ?

liste_des_nombres_a_additionner = [5, 2, 7, 2, 5, 6]

resultat_intermediaire = 0
for nombre_a_additionner in liste_des_nombres_a_additionner:
    resultat_intermediaire = resultat_intermediaire + nombre_a_additionner
resultat_final = resultat_intermediaire
print("Somme avec une boucle :", resultat_final)

somme_de_liste = sum(liste_des_nombres_a_additionner)
print("Somme par une méthode plus simple :", somme_de_liste)


# Et le produit des nombres ?

liste_des_nombres_a_multiplier = [5, 2, 7, 2, 5, 6]
resultat_intermediaire = 1
for nombre_a_multiplier in liste_des_nombres_a_multiplier:
    resultat_intermediaire = resultat_intermediaire * nombre_a_multiplier
resultat_final = resultat_intermediaire
print("Produit avec une boucle :", resultat_final)


# Déterminer le maximum et le minimum ?

liste_de_nombres = [3, 9, 2, 14]

minimum_liste = min(liste_de_nombres)
print("Le minimum est :", minimum_liste)

maximum_liste = max(liste_de_nombres)
print("Le maximum est :", maximum_liste)

# Liste de listes

element0 = [1, 2, 3, 4]
element1 = [1, 2, 3, 4]
element2 = [1, 2, 3, 4]
element3 = [1, 2, 3, 4]
element4 = [1, 2, 3, 4]
element5 = [1, 2, 3, 4]
element6 = [1, 2, 3, 4]
element7 = [1, 2, 3, 4]
element8 = [1, 2, 3, 4]
element9 = [1, 2, 3, 4]

liste_de_liste = [
    element0,
    element1,
    element2,
    element3,
    element4,
    element5,
    element6,
    element7,
    element8,
    element9,
]

print(liste_de_liste)

liste_de_liste_2 = []
for i in range(10):
    liste_de_liste_2.append([1, 2 ,3, 4])

print(liste_de_liste_2)


# Table de multiplication

table_multiplication = []
for i in range(10):
    #table_de_i = [0*i, 1*i, 2*i, 3*i, 4*i, 5*i, 6*i, 7*i, 8*i, 9*i]

    table_de_i = []
    for j in range(10):
        table_de_i.append(j * i)

    table_multiplication.append(table_de_i)

print("Tables de multiplication :")
print(table_multiplication)

print("Le produit de 3 par 7 vaut :", table_multiplication[3][7])
