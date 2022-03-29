# 4 milyonu geçmeyen butun cift fibonacci sayilarinin toplamı
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
a,b=0,1
cifttoplam=0
for i in range(34):
    c=a
    a=a+b
    b=c
    if b > 4000000:
        break
    elif b%2==0:
     print(b)
     cifttoplam+=b

print("Cift Toplam:",cifttoplam)