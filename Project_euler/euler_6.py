# ilk 100 sayının toplamının karesinin ilk 100 sayının karesi toplamının farkı
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

karetoplam = 0
toplamkare = 0

for i in range(1,101):
    karetoplam += i**2
for i in range(1,101):
    toplamkare+=i

toplamkare = toplamkare**2

sonuc=toplamkare-karetoplam
print(sonuc)