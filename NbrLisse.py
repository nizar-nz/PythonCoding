from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import sqrt
def play():
    mess = "Veuillez introduire un nombre > 1 : "
    N = windows.le_n.text()
    if (N.isdigit()) and (int(N)>1):
        if lisse(int(N)) :
            mess=N+" est un nombre lisse"
        else:
            mess=N+" n'est pas un nombre lisse"
    windows.lbl_res.setText(mess)
def lisse(N):
    if premier(N):
        return N<=sqrt(N)
    for i in range(N//2,1,-1):
        if N%i==0 and premier(i) :
            return i<=sqrt(N)

def premier(N):
    i = N//2
    while N % i != 0 :
        i=i-1
    return i==1
app=QApplication([])
windows=loadUi("interfacelisse.ui")
windows.show()
windows.bt_verif.clicked.connect(play)
app.exec_()
