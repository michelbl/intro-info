
"""ma_variable = 20
if ma_variable < 15:
    print("le test est négatif")
    print(ma_variable)
else:
    print("le test est négatif")
"""

"""prenom = "Hippolyte"
if len(prenom) > 8:
    print("Vous avez un long prénom.")

"""

"""
resultat_input = input("abc")
print(resultat_input)

str()
list()
int("35678")
"""
"""
var1 = "35678"
var2 = 35678

print(var1 + var1)
print(var2 + var2)

3567835678
"""
"""
age = int(input("Quel est votre âge ?"))

if age < 18:
    print("Vous êtes mineur.")
    if age < 4:
        print("Et plus précisemment : un bébé.")
    elif age < 12:
        print("Et plus précisemment : un enfant.")
    else:
        print("Et plus précisemment : un adolescent.")
else:
    print("Vous êtes majeur.")
"""

"""x = 0
for compteur in ['a', 'b', 'c']:
    print("Début du bloc")
    print("compteur vaut :", compteur)
    x = x + 1
    print("x vaut maintenant", x)
    print("Fin du bloc")
    print()

print("x vaut à la fin", x)
print("compteur vaut à la fin :", compteur)

print(list(range(10)))
"""
"""
for prenom in ["Marcel", "Augustin", "Pierre"]:
    print("Bonjour", prenom)

"""

#Méthode 1
"""
for nombre in range(16):
    print(2*nombre)
"""

## Méthode 2 (avec modulo pour tester la parité)
"""
for compteur in range(31):
    if compteur % 2 == 0:
        print(compteur)
"""

## Méthode 3 (avec uniquement range)

"""
for compteur in range(0, 31, 2):
    print(compteur)
"""

## Afficher en ordre décroissant les nombres de 10 à 1.

## Méthode 1

"""
for nombre in range(10):
    print(10-nombre)
"""
## Méthode 2

"""for compteur in range(10, 0, -1):
    print(compteur)
"""
## Calculer 1 x 2 x 3 x 4 x 5 x 6 avec une boucle.

#print(1 * 2 * 3 * 4 * 5 * 6)

"""resultat_intermediaire = 1
for compteur in range(1, 7):
    resultat_intermediaire = resultat_intermediaire * compteur
resultat_final = resultat_intermediaire
print(resultat_final)
"""

"""z = 1
for compteur in range(6):
    z = (compteur + 1) * z
    print(z)
"""
## Pour chaque nombre entre 1 et 30, afficher si le nombre est pair ou impair.

for compteur in range(1, 31):
    if compteur % 2 == 0:
        print('Le nombre', compteur, "est pair.")
    else:
        print('Le nombre', compteur, "est impair.")
