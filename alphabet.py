from numpy import array
N=26
ALPHABET = array([str]*N)
for l in range (N):
    if l%2==0:
        ALPHABET[l]=chr(65+l)
    else:
        ALPHABET[l]=chr(97+l)
print(ALPHABET)
