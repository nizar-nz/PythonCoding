from random import randint
from numpy import array
size = 26
key = array([int]*size)

def get_message():
    mess = ""
    valid = True
    while mess == "" or not valid:
        mess = input("entrer le message à crypter: ").upper()
        i = 0
        while i < len(mess) and (mess[i] == ' ' or 'A' <= mess[i] <= 'Z'):
            i=i+1
        valid = i == len(mess) and mess.find('  ') == -1
        if not valid :
            print("vérifier que le message contient uniquement des lettres et des espaces!")
            print("vérifier que les mots du message sont séparer par un seul espace!")
    return (mess)

def already_exist(i:int):
    j = 0
    while j < i :
        if key[j] == key[i] :
            return True
        j = j + 1
    return False

def key_crypt_init():
    for i in range(size):
        exist = True
        while exist:
            key[i]=randint(33,99)
            exist = already_exist(i)

def pre_crypt_mess(m:str):
    RES=''
    for i in range(len(m)):
        if m[i] == ' ':
            RES = RES + '32'
        else:
            RES = RES + str(key[(ord(m[i])-65)])
    return (RES)

def crypt_mess(ch:str):
    mc = ''
    for i in range(0,len(ch),2):
        mc = mc + chr(int(ch[i]+ch[i+1]))
    return mc

key_crypt_init()
mess = get_message()
print(mess)
res = pre_crypt_mess(mess)
print(res)
mc = crypt_mess(res)
print(mc)
