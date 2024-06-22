from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def play():
    msg = "Veuillez introduire un nombre > 0 "
    ch = windows.le.text()
    if ch.isdigit() and int(ch) > 0 :
        N = int(ch)
        if SuperPairplus(N) :
            msg = ch + " est super-pairplus"
        else:
            msg = ch + " n'est pas super-pairplus"
    windows.res.setText(msg)
def SuperPairplus(N):
    # condition 1
    if N % 2 != 0 :
        return False
    # condition 2
    chn = str(N)
    for i in range(len(chn)):
        if int(chn[i]) % 2 != 0 :
            return False
    # condition 3
    i = N // 2
    while i > 1 :
        if N % i == 0 and i % 2 != 0 :
            return False
        i = i - 1
    return True
app = QApplication([])
windows = loadUi ("interfacesuperpairplus.ui")
windows.show()
windows.bt.clicked.connect ( play )
app.exec_()


