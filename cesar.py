
"""BONJOUR MONDE
ERQMRXU PRQGH

DWWDTXHUDOHVLDPDLQWHQDQW
ATTAQUERALESIAMAINTENANT
"""

def chiffre_une_lettre(lettre):
    #print("Lettre :", lettre)

    codage_numerique = ord(lettre)-64

    #print("Nombre correspondant :", codage_numerique)

    codage_numerique_apres_decalage = codage_numerique + 3
    if codage_numerique_apres_decalage > 26:
        codage_numerique_apres_decalage = codage_numerique_apres_decalage - 26

    #print('Code de la lettre encryptée', codage_numerique_apres_decalage)

    lettre_apres_decalage = chr(codage_numerique_apres_decalage+64)

    #print("Lettre codée :", lettre_apres_decalage)

    return lettre_apres_decalage


def dechiffre_une_lettre(lettre):
    #print("Lettre :", lettre)

    codage_numerique = ord(lettre)-64

    #print("Nombre correspondant :", codage_numerique)

    codage_numerique_apres_decalage = codage_numerique - 3
    if codage_numerique_apres_decalage < 0:
        codage_numerique_apres_decalage = codage_numerique_apres_decalage + 26

    #print('Code de la lettre décryptée', codage_numerique_apres_decalage)

    lettre_apres_decalage = chr(codage_numerique_apres_decalage+64)

    #print("Lettre décodée :", lettre_apres_decalage)

    return lettre_apres_decalage



lettre_encodee = chiffre_une_lettre(lettre="A")
print("Resultat du codage de la lettre A :", lettre_encodee)

print()

lettre_decodee = dechiffre_une_lettre(lettre="A")
print("Resultat du decodage de la lettre A :", lettre_decodee)
