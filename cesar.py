
def chiffre_une_lettre(caractère):
    #print("Lettre :", lettre)

    if (caractère < 'A') or (caractère > 'Z'):
        print('Le caractère', caractère, "n'est pas une lettre majuscule! Pas de décalage.")
        return caractère

    lettre = caractère

    codage_numerique = ord(lettre)-64

    #print("Nombre correspondant :", codage_numerique)

    codage_numerique_apres_decalage = codage_numerique + 3
    if codage_numerique_apres_decalage > 26:
        codage_numerique_apres_decalage = codage_numerique_apres_decalage - 26

    #print('Code de la lettre encryptée', codage_numerique_apres_decalage)

    lettre_apres_decalage = chr(codage_numerique_apres_decalage+64)

    #print("Lettre codée :", lettre_apres_decalage)

    return lettre_apres_decalage


def dechiffre_une_lettre(caractère, décalage):
    #print("Lettre :", lettre)

    if (caractère < 'A') or (caractère > 'Z'):
        print('Le caractère', caractère, "n'est pas une lettre majuscule! Pas de décalage.")
        return caractère

    lettre = caractère

    codage_numerique = ord(lettre)-64

    #print("Nombre correspondant :", codage_numerique)

    codage_numerique_apres_decalage = codage_numerique - décalage
    if codage_numerique_apres_decalage <= 0:
        codage_numerique_apres_decalage = codage_numerique_apres_decalage + 26

    #print('Code de la lettre décryptée', codage_numerique_apres_decalage)

    lettre_apres_decalage = chr(codage_numerique_apres_decalage+64)

    #print("Lettre décodée :", lettre_apres_decalage)

    return lettre_apres_decalage



lettre_encodee = chiffre_une_lettre(caractère="A")
print("Resultat du codage de la lettre A :", lettre_encodee)

print()

lettre_decodee = dechiffre_une_lettre(caractère="A", décalage=3)
print("Resultat du decodage de la lettre A :", lettre_decodee)


"""BONJOUR MONDE
ERQMRXU PRQGH

DWWDTXHUDOHVLDPDLQWHQDQW
ATTAQUERALESIAMAINTENANT
"""

message_à_chiffrer = 'BONJOUR MONDE'

message_chiffré = ''
for lettre_du_message in message_à_chiffrer:
    lettre_chiffrée = chiffre_une_lettre(caractère=lettre_du_message)
    message_chiffré = message_chiffré + lettre_chiffrée

print('Le message chiffré est', ''.join(message_chiffré))


message_à_déchiffrer = 'DWWDTXHUDOHVLDPDLQWHQDQW'

message_déchiffré = ''
for lettre_du_message in message_à_déchiffrer:
    lettre_déchiffrée = dechiffre_une_lettre(caractère=lettre_du_message, décalage=3)
    message_déchiffré = message_déchiffré + lettre_déchiffrée

print('Le message déchiffré est', ''.join(message_déchiffré))


message_mystère = "XQOTURRDQPQOEMDRAZOFUAZZQBMDPOMXMSQPQEXQFFDQEPQXMXBTMNQFBMDQJQYBXQPMZEXUYMSQOUPQEEGEUXKMGZQPUEFMZOQPQOMDMOFDQEPAZONPQHUQZFQPMZEXQFQJFQOAPQZODKBFASDMBTUQXQOTURRDQYQZFBMDPOMXMSQMGEEUOAZZGOAYYQXQOTURRDQPQOEMDAGXQOAPQPQOEMDHAUDXQEPURRDQZFEZAYEQEFGZQYFTAPQPQOTURRDQYQZFFDEEUYBXQGFUXUEQBMDVGXQEOEMDPMZEEQEOADDQEBAZPMZOQEEQODFQEOQCGUQJBXUCGQXQZAYOTURRDQPQOEMDXQFQJFQOTURRDEANFUQZFQZDQYBXMMZFOTMCGQXQFFDQPGFQJFQOXMUDADUSUZMXBMDGZQXQFFDQPUEFMZOQRUJQFAGVAGDEPGYYQOFPMZEXADPDQPQXMXBTMNQFBAGDXQEPQDZUDQEXQFFDQEPMZEXQOMEPGZPOMXMSQPDAUFQAZDQBDQZPMGPNGFBMDQJQYBXQMHQOGZPOMXMSQPQHQDEXMPDAUFQMQEFDQYBXMOBMDPNPQHUQZFQQFMUZEUVGECGICGUPQHUQZFLBGUEJPQHUQZFMQFOUXEMSUFPGZQBQDYGFMFUAZOUDOGXMUDQPQXMXBTMNQFXMXAZSGQGDPGPOMXMSQPMZEXQJQYBXQHACGOAZEFUFGQXMOXPGOTURRDQYQZFCGUXEGRRUFPQFDMZEYQFFDQMGPQEFUZMFMUDQEUXEMUFPVCGUXEMSUFPGZOTURRDQYQZFPQOEMDBAGDCGQOQXGUOUBGUEEQPOTURRDQDXQYQEEMSQPMZEXQOMEPQXMXBTMNQFXMFUZXQOTURRDQPQOEMDZMCGQOXEBAEEUNXQEKOAYBDUEXMOXZGXXQCGUZQYAPURUQBMEXQFQJFQUXEMSUFPGZOMEBMDFUOGXUQDPQOTURRDQYQZFBMDEGNEFUFGFUAZYAZAMXBTMNFUCGQOQEEGNEFUFGFUAZEDQBAEQZFEGDGZBDUZOUBQMZMXASGQYMUEEAZFANFQZGQEBMDPQEBQDYGFMFUAZECGQXOAZCGQEPQEXQFFDQEPQXMXBTMNQFPMZEXQOMESZDMXXMOXQEFPAZZQBMDXMBQDYGFMFUAZQFXQZAYNDQPQOXEBAEEUNXQEQEFMXADEEMZEOAYYGZQYQEGDQMHQOOQXGUPQEOTURRDQYQZFEPQOEMDXQOTURRDQYQZFPQOEMDMBGFDQGFUXUEOAYYQXYQZFPGZQYFTAPQBXGEOAYBXQJQOAYYQXQOTURRDQPQHUSQZDQEQGXUXZARRDQMGOGZQEOGDUFPQOAYYGZUOMFUAZOMGEQPGFDERMUNXQZAYNDQPQOXEOQCGUBQDYQFPQEEMKQDEKEFYMFUCGQYQZFOQXXQEOUCGMZPXMYFTAPQPQOTURRDQYQZFQEFOAZZGQYMUEMGEEUBMDOQCGQOAYYQFAGFQZOAPMSQBMDEGNEFUFGFUAZYAZAMXBTMNFUCGQUXBQGFFDQFDEDMBUPQYQZFOMEEBMDMZMXKEQPQRDCGQZOQEOQDFMUZQEXQFFDQEMBBMDMUEEQZFNQMGOAGBBXGEEAGHQZFCGQXQEMGFDQEPMZEGZQXMZSGQZMFGDQXXQ"

for essai_décalage in range(1, 27):
    print('Le décalage courant est', essai_décalage)

    message_déchiffré = ''
    for lettre_du_message in message_mystère:
        lettre_déchiffrée = dechiffre_une_lettre(caractère=lettre_du_message, décalage=essai_décalage)
        message_déchiffré = message_déchiffré + lettre_déchiffrée

    print('Le message déchiffré est', ''.join(message_déchiffré))

