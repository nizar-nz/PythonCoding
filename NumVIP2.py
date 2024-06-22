from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def play():
    n=windows.l1.text()
    msg="vérifier que le numéro saisie est correcte!\nle numéro doit comporter 8 chiffres et commenser par 9,5,4 ou 2"
    if n.isdigit() and len(n)==8 and "9542".find(n[0])!=-1:
        if vip(n):
            msg=n+" est un numéro VIP"
        else:
            msg=n+" n'est pas un numéro VIP\nle numéro VIP le plus proche est:"+GenVip(n)
    windows.res.setText(msg)
def vip(n):
    for i in range (2,len(n)):
        if n[i]==n[i-1]==n[i-2]:
            return True
    for i in range (0,len(n)-2):
        if int(n[i])==int(n[i+1])-1==int(n[i+2])-2 or int(n[i])==int(n[i+1])+1==int(n[i+2])+2:
            return True
    for i in range (len(n)):
        if n.count(n[i])>=4:
            return True
    return False         
def GenVip(n):
    i=1
    while not (vip(str(int(n)+i)) or vip(str(int(n)-i))):
        i=i+1
    if vip(str(int(n)+i)):
        return str(int(n)+i)
    else:
        return str(int(n)-i)

app = QApplication([])
windows = loadUi ("InterfaceNumVIP2.ui")
windows.show()
windows.btt.clicked.connect ( play )
app.exec_()






