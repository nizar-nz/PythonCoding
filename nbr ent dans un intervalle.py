# Fonction personnalisée pour vérifier si une chaîne représente un entier valide
def est_entier(val):
    val = val.strip()  # Supprime les espaces en début et en fin de chaîne
    if val and (val[0] in ('-', '+')):
        return val[1:].isdigit()
    return val.isdigit()

# Saisie de la borne inférieure avec contrôle
borne_inferieure = ''
while not est_entier(borne_inferieure):
    borne_inferieure = input("Entrez un nombre entier valide pour la borne inférieure : ")
borne_inferieure = int(borne_inferieure)

# Saisie de la borne supérieure avec contrôle
borne_superieure = ''
while not est_entier(borne_superieure) or int(borne_superieure) < borne_inferieure :
    borne_superieure = input("Entrez un nombre entier valide pour la borne supérieure : ")
borne_superieure = int(borne_superieure)

# Saisie du nombre avec contrôle
nombre = ''
while not est_entier(nombre) :
    nombre = input("Entrez un nombre entier valide : ")
nombre = int(nombre)

# Vérification si le nombre appartient à l'intervalle
if borne_inferieure <= nombre <= borne_superieure:
    print(f"Le nombre {nombre} appartient à l'intervalle [{borne_inferieure}, {borne_superieure}].")
else:
    print(f"Le nombre {nombre} n'appartient pas à l'intervalle [{borne_inferieure}, {borne_superieure}].")
