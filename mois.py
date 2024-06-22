couleurs =  ['rouge', 'orange', 'vert', 'jaune', 'bleu', 'indigo', 'violet','noir', 'blanc','gris','maron','rose']
couleurs.insert(4, 'vert pistache')
for c in couleurs:
    if c.upper().find('T')!=-1:
        couleurs.remove(c)
print(couleurs)