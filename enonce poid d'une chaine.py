On définit le poids d’une chaîne comme étant la somme des produits de la
position de chaque voyelle dans cette chaîne par son rang dans l’alphabet
français.
Si la chaîne ne contient pas de voyelles alors son poids est égal à zéro.
N.B : les voyelles sont A, E, I, O, U, Y et leurs rangs respectifs sont :
    1, 5, 9, 15, 21, 25
Exemple :
La chaîne ‘BONNE‘ contient 2 voyelles ‘O’ et ‘E’, sont poids est égal à
2*15+5*5=55
La chaîne ‘CHANCE‘ contient 2 voyelles ‘A’ et ‘E’, son poids est égal à :
    3*1+6*5=33
Travail à faire :
Ecrire un programme Python qui permet de lire une chaîne non vide,
composée seulement par des lettres alphabétiques majuscules puis calcule
et affiche le poids de cette chaîne.
L’affichage du résultat sera de la forme suivante:
Le poids du mot 'APCPEDAGOGIE' est 1*1 + 5*5 + 7*1 + 9*15 + 11*9 + 12*5 = 327