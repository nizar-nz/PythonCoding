def getTotalX(a, b):
    # Write your code here
    s = []
    for j in b:
        for i in a:
            if j % i == 0:
                s.append(j//i)
    sf =[]
    for d in s :
        c = 0
        for j in b:
            if j % d == 0:
                c += 1
        if c == len(b):
            c = 0
            for i in a:
                if d % i == 0:
                    c += 1
            if c == len(a):
                sf.append(d)
    print(sf)
    return len(sf)

a = [2, 6]
b = [24, 36]
print(getTotalX(a,b))