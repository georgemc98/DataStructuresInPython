import math
import time

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)





    def __add__(self, newFraction):
        newNum = self.num * newFraction.den + self.den * newFraction.num
        newDen= self.den * newFraction.den

        common = gcd(newNum,newDen)

        return Fraction(newNum/common, newDen/common)


    def gcd(a, b):
        i = 1
        while (i <= a and i <= b):
            if (a % i == 0 and b % i == 0):
                gcd = i
            i = i + 1
        return gcd


    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den

        return firstNum == secondNum



myFrac = Fraction(3, 5)
newFrac = Fraction(1, 2)

frac1 = Fraction(1,2)
frac2 = frac1

print(frac1 == newFrac, frac1 == frac2)

print(myFrac, str(myFrac))

def sum(n):
    start = time.time()
    sum =0
    for i in range(1, n+1):
        sum = sum + 1
    end = time.time()

    return sum, end - start

print("sum is %d required %10.7f seconds" %sum(1000000))

def sum_of_n3(n):
    start = time.time()
    result = (n * (n+1))/2
    end = time.time()

    return result, end-start


