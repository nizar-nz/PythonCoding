age = input("entrer votre age: ")
if age.isdigit():
    age = int(age)
    if 16 <= age <= 70 :
        poid = int(input("entrer votre poid(kg): "))
        taille = int(input("entrer votre taille(cm): "))
        imc = poid / (taille / 100) ** 2
        print(imc)
        if imc < 16.5:
            print("famine")
        elif 16.5<=imc<18.5:
            print("migreur")
        elif 18.5<=imc<25:
            print("corpulence normale")
        elif 25<=imc<30:
            print("surpoid")
        elif 30<=imc<35:
            print("obésité moderé")
        elif 35<=imc<40:
            print("obésité sevère")
        else:
            print("obésité morbide ou massive")    