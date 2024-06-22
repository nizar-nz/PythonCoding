n = int(input("Entrez un entier strictement positif :"))  
while n < 1:  
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))
i = 2   
cpt = 0   
p = n / 2   
msg1 = ""  
print("Diviseurs propres sans répétition de", n, " :", end=' ')  
while i <= p :  
    if n % i == 0:  
        cpt += 1  
        print(i, end=' ')  
    i += 1  
  
if not cpt :  
    print("aucun ! Il est premier.")  
else : 
    print("(soit", cpt, "diviseurs propres)")