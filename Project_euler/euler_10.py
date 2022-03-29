# 2 milyondan küçük asalların toplamı
# Find the sum of all the primes below two million.

asallar=[2,3,5,7,11]

def asami(a):
    for i in asallar:
        if i**2>a:
            asallar.append(a)
            return 1
        if a%i==0 and a!=i:
            return 0
    asallar.append(a)
    return 1


for i in range(13,2000000,2):
    if asami(i)==1:

        print(i)
print("toplamın değeri =",sum(asallar))