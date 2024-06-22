enu1 = 'bonjour'
enu2 = ('o', 'u', 'i')

resultat = list((set(enu1)|set(enu2))-(set(enu1) & set(enu2)))

print(resultat)
