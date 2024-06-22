ch = input()
p=int(input())
nb=int(input())
res=''
for i in range(len(ch)):
    if p <= i <= p + nb - 1:
        res = res + ch[i]