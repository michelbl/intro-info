
# Assignation de valeurs à des variables
variable1 = 42
print(variable1)

# Ne pas confondre avec un test d'égalité
variable1 == variable2

variable2 = 42
variable1 = variable2
print(variable1)

# On peut toujours substituer une variable avec la valeur qu'elle contient
ma_variable = "Bonjour"
print(ma_variable)
# équivalent à :
print("Bonjour")

# ne marche pas, la variable Bonjour n'est pas définie
ma_variable = Bonjour

variable_a = "Bonjour"
variable_b = "Marie"
variable_c = variable_a + " " + variable_b
print(variable_c)
print(type(variable_c))

# Exemple de liste
print(type([5, 10, 'a']))

# Exemple de dictionnaire
print(type({"cle": "valeur", "cle2": "valeur2"}))

# Exemple de booléen
print(6==6)
print(type(6==6))
