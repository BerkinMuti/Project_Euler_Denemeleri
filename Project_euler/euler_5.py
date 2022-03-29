# 1 den 20 e kadar bütün sayılara bölünen en küçük sayı
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math
import functools
def ebob(x,y):
    return math.gcd(x,y)
def ekok(x,y):
    return (x*y) // ebob(x,y)
liste=range(1,21)
result=functools.reduce(ekok,liste)
print(result)