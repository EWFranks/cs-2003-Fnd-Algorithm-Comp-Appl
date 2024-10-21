# Eliga Franks
# Lab 02 – Spring 20

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)

    def __eq__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den

        return firstnum == secondnum

    def __le__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den
        if firstnum <= secondnum:
            return True
        return False

file = open("lab02data.txt", "r")

lines = file.readlines()

with open("lab02data.txt", "r") as file:
    row = file.readline()
    row = file.readline()

    while row != '':

        array = row.split()  # ["1","3","8","-5"]

        x = Fraction(int(array[0]), int(array[1]))
        y = Fraction(int(array[2]), int(array[3]))

        print()

        print("The first fraction is:", x)

        print("The second fraction is:", y)

        print("The sum of the two fractions is:", x + y)

        print("The difference of the two fractions is:", (x - y))

        print("The product of the two fractions is:", x * y)

        print("The first fraction divided by the second fraction is:", (x / y))

        print("The first fraction is ≤ the second fraction:", (x <= y))

        row = file.readline()

