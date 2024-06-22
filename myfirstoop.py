class Produit:
    tlp=[]
    def __init__(self,nom : str, puht : float, tva : float, qte : int):
        assert puht >= 0, f"le prix unitaire hors taxe {puht} doit être >= 0" 
        assert 0 <= tva <=1, f"la taxe sur la valeur ajouté {tva} doit être entre 0.0 et 1.0"
        
        self.nom = nom
        self.puht = puht
        self.tva = tva
        self.qte = qte
        
        Produit.tlp.append(self)
    def __repr__(self):
        return f"Produit(nom:{self.nom}"+" "*(18-len(self.nom))+f",puht:{self.puht:8.3f},tva:{self.tva:.0%},qte:{self.qte})"

p1 = Produit("aftershave",11.500,0.19,10)
p2 = Produit("rasoir 3  lames",2.500,0.19,50)
for p in Produit.tlp:
    print(p)