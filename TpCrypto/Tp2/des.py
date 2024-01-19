from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def ajouter_remplissage(texte):
    longueur_remplissage = 8 - len(texte) % 8
    remplissage = chr(longueur_remplissage) * longueur_remplissage
    return texte + remplissage

def retirer_remplissage(texte_rempli):
    longueur_remplissage = ord(texte_rempli[-1])
    return texte_rempli[:-longueur_remplissage]

def chiffrer_des(texte_clair, cle):
    chiffreur = DES.new(cle, DES.MODE_ECB)
    texte_rempli = ajouter_remplissage(texte_clair)
    texte_chiffre = chiffreur.encrypt(texte_rempli.encode('utf-8'))
    return texte_chiffre

def dechiffrer_des(texte_chiffre, cle):
    chiffreur = DES.new(cle, DES.MODE_ECB)
    texte_rempli = chiffreur.decrypt(texte_chiffre)
    texte_clair = retirer_remplissage(texte_rempli.decode('utf-8'))
    return texte_clair

cle = 'monsecret'
texte_clair = 'Hello DES!'

texte_chiffre = chiffrer_des(texte_clair, cle)
print(f'Texte chiffré (hex) : {texte_chiffre.hex()}')

texte_dechiffre = dechiffrer_des(texte_chiffre, cle)
print(f'Texte déchiffré : {texte_dechiffre}')


