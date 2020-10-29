# Pour une liste de nombres, comment calculer la somme des nombres ?

liste_des_nombre_a_additionner = [5, 2, 7, 2, 5, 6]

resultat_intermediaire = 0
for nombre_a_additionner in liste_des_nombre_a_additionner:
    resultat_intermediaire = resultat_intermediaire + nombre_a_additionner
resultat_final = resultat_intermediaire
print("Somme avec une boucle :", resultat_final)

somme_de_liste = sum(liste_des_nombre_a_additionner)
print("Somme par une méthode plus simple :", somme_de_liste)


# Et le produit des nombres ?

liste_des_nombre_a_multiplier = [5, 2, 7, 2, 5, 6]
resultat_intermediaire = 1
for nombre_a_multiplier in liste_des_nombre_a_multiplier:
    resultat_intermediaire = resultat_intermediaire * nombre_a_multiplier
resultat_final = resultat_intermediaire
print("Produit avec une boucle :", resultat_final)



# Déterminer le maximum et le minimum ?


