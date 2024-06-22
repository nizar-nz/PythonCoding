from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Ondulant(N):
    sN=str(N)
    i = 2
    while i < len(sN) and sN[i] == sN[i-2] :
        i = i+1
    return i == len(sN)

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