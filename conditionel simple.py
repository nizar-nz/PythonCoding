MonAge = 15
tolerance = 1
print("bonjour,je m'appelle mohamed")
age = int(input("est ce que tu peux deviner mon âge? "))
if age == MonAge :
    print("Bravo!")
if MonAge - tolerance <= age <= MonAge + tolerance:
    print('tu es presque!')
else :
    print(':-(')