
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
app = QApplication([])
windows = loadUi ("C:/bac2023/Prototype2022.ui")

def Chance(ch):
    if not (ch.isdigit() and len(ch)==8 and ch[0] in ["2","4",'5','9']):
        msg="Vérifier le numéro de télephone!"
    else:
        msg="Désolé vous n'avez pas gagné."
        s=0
        for i in range (len(ch)) :
            s+=int(ch[i])*i
        if premier(s):
            msg="Félicitations, vous avez gagné."
    return msg
def premier(n):
    d=2
    while d<n and n%d !=0:
        d+=1
    return n == d

def Play():
    x=windows.l2.text()
    msg=Chance(x)
    windows.l3.setText(msg)
    
windows.show()
windows.Jouer.clicked.connect ( Play )

app.exec_()
