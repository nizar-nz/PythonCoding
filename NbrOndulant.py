from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Ondulant(N):
    sN=str(N)
    ev=sN[0]
    od=sN[1]
    Ond = True
    i = 2
    while i < len(sN) and Ond == True :
        if i % 2 == 0 :
            Ond = sN[i] == ev
        else :
            Ond = sN[i] == od
        i = i+1
    return Ond

def Play():
    mess = "Veuiller introduire un nombre >= 100"
    if windows.lE_entrer.text().isdigit():
        no=int(windows.lE_entrer.text())
        if no > 100 :
            if Ondulant(no):
                mess = str(no) + " est ondulant"
            else :
                mess = str(no) + " n'est pas ondulant"
    windows.l_resultat.setText(mess)

app = QApplication([])
windows = loadUi ("InterfaceOndulant.ui")
windows.show()
windows.b_verif.clicked.connect ( Play )

app.exec_()