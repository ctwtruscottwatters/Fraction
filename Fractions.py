import sys
import os
import datetime
import base64

""" x: < 13/93 > y: < 1955/1993 > z: < 4/11 > a: < 207724/8649 > b: < 7820/21923 > c: < 372/143 > d: < 196053476430761073330659760423566015424403280004115787589590963842248961/961410160206664622086998474872525329540550991672782179554222730174333739159409986394206895176171912560363787697067327321683201 >
p: False !p: True r (is that a is less than b and less than c): False s (d is greater than c, already established the ordering principle): False
0.13978494623655913 < 0.9809332664325138 < 0.36363636363636365; not 0.13978494623655913 < 0.9809332664325138 < 0.36363636363636365; 24.01711180483293 < 0.35670300597545956 < 2.6013986013986012; 2.6013986013986012 < 2.0392282560090423e-55


Charles Truscott Watters
"""


class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return "< " + str(self.numerator) + "/" + str(self.denominator) + " >"
    def decimal(self):
        return float(self.numerator) / float(self.denominator)
    def __lt__(self, other):
        return self.decimal() < other.decimal()
    def __gt__(self, other):
        return self.decimal() > other.decimal()
    def __ge__(self, other):
        return self.decimal() >= other.decimal()
    def __le__(self, other):
        return self.decimal() <= other.decimal()
    def add(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = (self.denominator * self.denominator)
        return Fraction(new_numerator, new_denominator)
    def subtract(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = (self.denominator * self.denominator)
        return Fraction(new_numerator, new_denominator)
    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    def divide(self, other):
        new_numerator = (self.numerator * other.denominator)
        new_denominator = (self.denominator * other.numerator)
        return Fraction(new_numerator, new_denominator)
    def exponentiate(self, power):
        new_numerator = self.numerator ** power
        new_denominator = self.denominator ** power
        return Fraction(new_numerator, new_denominator)

def main():
    x = Fraction(13, 93)
    y = Fraction(1955, 1993)
    z = Fraction(4, 11)
    a = x.add(y)
    b = y.multiply(z)
    c = z.divide(x)
    d = x.exponentiate(64)
    print("x: {} y: {} z: {} a: {} b: {} c: {} d: {}".format(x, y, z, a, b, c, d))

    p = x < y < z
    q = not p
    r = a < b < c
    s = d > c
    print("p: {} !p: {} r (is that a is less than b and less than c): {} s (d is greater than c, already established the ordering principle): {}".format(p, q, r, s))
    print("{} < {} < {}; not {} < {} < {}; {} < {} < {}; {} < {}".format(x.decimal(), y.decimal(), z.decimal(), x.decimal(), y.decimal(), z.decimal(), a.decimal(), b.decimal(), c.decimal(), c.decimal(), d.decimal()))

#    string_of_fraction = base64.b64encode(str(d).encode())
#    print(string_of_fraction)
if __name__ == "__main__": main()