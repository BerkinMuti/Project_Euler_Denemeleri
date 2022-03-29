# bastan ve sondan okunuşu aynı olan ve 2 tane 3 basamaklı sayının çarpımı olan en buyuk sayıyı bul
#Find the largest palindrome made from the product of two 3-digit numbers.
from math import ceil
def is_polindrome(sayi):

    sayi = str(sayi)

    uzunluk = len(sayi)

    ilk = sayi[0:uzunluk // 2]

    son = sayi[int(ceil(uzunluk/2)):]

    if ilk == son[::-1]:
        return 1
    return 0
sonuc = 0

for i in range(100,1000):
    for j in range(100,1000):
        k = i * j
        if is_polindrome(k) == 1 and k > sonuc:
            sonuc = k
print(sonuc)