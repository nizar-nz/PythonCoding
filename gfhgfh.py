class Bidon():
    def __init__ (self, L:float, l:float, h:float, contenance:int, plastique:str='pla',
                  couleur:str='blanc'):
        #controledesaisie
        assert L>0, "la longueur doit etre supérieure à 0"
        assert l>0, "la largeur doit etre supérieure à 0"
        assert h>0, "l'hauteur doit etre supérieur à 0"
        assert contenance > 0, "la valeur de la contenance doit etre supérieure à 0"
        
        self.L = L
        self.l = l
        self.h = h
        Vmax = L * l * h
        if Vmax < contenance * 1000 :
            raise exception ("contenance impossible ! Vérifier la contenance ou les dimensions !")
        elif Vmax * 0.6 > contenance * 1000 :
            raise exception ("contenance trop petite ! Vérifier la contenance ou les dimensions !")
        self.contenance = contenance
        self.plastique = plastique
        self.couleur = couleur
        
    def __repr__ (self) :
        return f"{self.__class__.__name__}({self.L},{self.l},{self.h},{self.contenance},'{self.plastique}','{self.couleur}')"
    
    def calcul_qte_conteneur (self, conteneur:str='20p') :
        if conteneur == '20p' :
            Lc, lc, hc = 590, 235.2, 239.3
        elif conteneur == '40hc' :
            Lc, lc, hc = 1203.4, 235.2, 270
        return int ((Lc//self.L) * (lc//self.l) * (hc//self.h))

class Fut(Bidon):
    def __init__ (self, r:float, h:float, contenance:int, plastique:str='pla',
                  couleur:str='blanc'):
        super().__init__(r*2, r*2, h, contenance)

b1 = Bidon (20, 10, 30, 5)
b2 = Bidon (40, 40, 70, 100)
print (b1.calcul_qte_conteneur())
print (b2.calcul_qte_conteneur())
f1 = Fut(15,60,40)
print(f1)
print(f1.calcul_qte_conteneur('20p'))
print(f1.calcul_qte_conteneur('40hc'))
        
        
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
        

  
    
      
      
