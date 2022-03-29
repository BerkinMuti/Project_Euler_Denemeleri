# 600851475143 sayısının en büyük asal çarpanı
#What is the largest prime factor of the number 600851475143 ?

sayi = 600851475143
i = 2

while sayi != 1:
    while sayi % i == 0:
        sayi /= i
        if sayi == 1:
            i -= 1
    i += 1

print(i)