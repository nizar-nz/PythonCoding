from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def VIP(N:int):
    chn = str(N)
    for i in range(0,len(chn)-2):
        if chn[i] == chn[i+1] == chn[i+2] or (
            int(chn[i]) == int(chn[i+1]) + 1 == int(chn[i+2]) + 2) or (
            int(chn[i]) == int(chn[i+1]) - 1 == int(chn[i+2]) - 2) or (
                chn.count(chn[i]) >= 4 ):
            return True
    return False
def GenVip(N:int):
    minus = N
    plus = N
    while not VIP(minus) and not VIP(plus):
        minus = minus - 1
        plus = plus + 1
    if VIP(minus) :
        return minus
    else:
        return plus
def btn_verif_click():
    mess = "vérifier que le numéro saisie est correcte! \nle numéro doit comporter 8 chiffres et commenser par 9,5,4 ou 2."
    num = windows.le_num.text()
    if num.isdigit() and len(num) == 8:
        if num[0] == str(9) or num[0] == str(5) or num[0] == str(4) or num[0] == str(2):
            if VIP(int(num)):
                mess = num + " est un numéro VIP"
            else:
                mess = num + " n'est pas un numéro VIP, \nle numéro VIP le plus proche est: " + str(GenVip(int(num)))
    windows.lbl_res.setText(mess)
app = QApplication([])
windows = loadUi ("InterfaceNumVIP.ui")
windows.show()
windows.btn_verif.clicked.connect ( btn_verif_click )

app.exec_()