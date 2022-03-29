# 10001. asal sayıyı bulan algoritma
#What is the 10 001st prime number?
from math import ceil

def asalmi(sayi):
    for i in range(2, ceil(sayi**1/2)):
        if sayi % i == 0:
            return 0
    return 1

counter = 6
sayi = 13

while counter != 10001:
    sayi += 2
    if asalmi(sayi) == 1:
        counter += 1
print(sayi)