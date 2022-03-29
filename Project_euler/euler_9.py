# a**2 + b**2 = c**2 ve a<b<c olan a+b+c=1000 olan abc sayı çarpımını bulun
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.

def toplamkontrol(a, b, c):
    if a+b+c == 1000:
        return 1
    return 0

def karekontrol(a,b,c):
    if c**2== a**2 + b**2:
        return 1
    return 0

def anafonk():

    for i in range(1,1000):
        for j in range(1,1000):
            for k in range(1,1000):
                if toplamkontrol(i,j,k)==1 and karekontrol(i,j,k) and  i<j<k:
                    return i*j*k

print("carpim = {}".format(anafonk()))