# importer les bibliothèques nécessaires
from random import randint
# fixer le nombre secret
X = randint(0,100)
# définir les variables (nbr total de tentatives, num d'essai, rachat)
nbr_tot_tentatives = 10
num_essai = 1
rachat = True
# initialiser le nombre à deviner
valeur_entree = -1
# boucle du jeu
while valeur_entree != X and num_essai <= nbr_tot_tentatives :
  # afficher le numéro d'essai / nombre total de tentative
  print("tentative :" + str(num_essai)+ "/" + str(nbr_tot_tentatives))
  # deviner un nombre entre 0 et 100
  valeur_entree = int(input("Deviner un nombre entre 0 et 100: "))
  # comparer la valeur entrée avec la le nombre secret 
  if valeur_entree > X:
    print(str(valeur_entree)+" > X")
  elif valeur_entree < X:
    print(str(valeur_entree)+" < X")
  # incrementer le nombres d'essai  
  num_essai += 1
  # vérifier la condition de rachat 
  if rachat and -5 <= valeur_entree - X <= 5 :
    nbr_tot_tentatives += 1
    rachat = False
# fin du jeu    
if valeur_entree != X :
  print("Désolée tu as perdu!")
  print("le nombre secret est:",X)
else :
  print("Bravo, tu as deviner! en "+str(num_essai-1)+" tentatives")