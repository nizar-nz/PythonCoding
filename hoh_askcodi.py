class Hoh:
    tarif_gateaux = {
        "baklawa": 80,
        "bjaouia": 45,
        "kaak": 65,
        "boules": 55
    }
    
    tarif_emballage = {
        "0.5 Kg": 2.5,
        "1 Kg": 3.5,
        "2 Kg": 4.5,
        "3 Kg": 5.5
    }
    
    tarif_livraison = {
        "Tn": 10,
        "Fr": 50,
        "It": 43,
        "Ge": 62,
        "Ca": 93,
        "Ea": 51,
        "As": 47
    }
    
    def __init__(self):
        self.commande = []
    
    def ajouter_gateau(self, gateau, poids):
        self.commande.append((gateau, poids))
    
    def supprimer_gateau(self, gateau):
        self.commande = [g for g in self.commande if g[0] != gateau]
    
    def calculer_prix_gateaux(self):
        total = 0
        for gateau, poids in self.commande:
            prix_par_kg = self.tarif_gateaux[gateau]
            total += prix_par_kg * poids
        return total
    
    def determiner_modele_emballage(self):
        poids_total = sum([poids for _, poids in self.commande])
        if poids_total <= 0.5:
            return "0.5 Kg"
        elif poids_total <= 1:
            return "1 Kg"
        elif poids_total <= 2:
            return "2 Kg"
        else:
            return "3 Kg"
        
    def calculer_prix_emballage(self):
        modele_emballage = self.determiner_modele_emballage()
        return self.tarif_emballage[modele_emballage]
    
    def calculer_prix_livraison(self, pays):
        poids_total = sum([poids for _, poids in self.commande])
        if poids_total <= 3:
            return self.tarif_livraison[pays]
        else:
            return "La commande dépasse le poids maximum autorisé de 3 Kg."
    
    def calculer_prix_total(self, pays):
        prix_gateaux = self.calculer_prix_gateaux()
        prix_emballage = self.calculer_prix_emballage()
        prix_livraison = self.calculer_prix_livraison(pays)
        return prix_gateaux + prix_emballage + prix_livraison

# Exemple d'utilisation
client = Hoh()
client.ajouter_gateau("baklawa", 0.3)
client.ajouter_gateau("boules", 0.4)
client.ajouter_gateau("kaak", 0.5)

pays = "Fr"
prix_total = client.calculer_prix_total(pays)

print(f"Le prix total de la commande vers {pays} est de {prix_total} dt.")