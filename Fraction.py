# -*- coding: utf-8 -*-
"""
Charles Truscott, as drafted in notebook and MIT lessons
Massachusetts Institute of Technology 6.000.1x

runfile('C:/Users/17/Desktop/GuidedbyMIThopefullyMITXSeriesgrad.py', wdir='C:/Users/17/Desktop')
<138401/10230> 13.528934506353862
138401   /   10230 = 13.528934506353861192570869990225
"""

class Fraction(object):
    def __init__(self, num, denom):
            self.num = num
            self.denom = denom
    def __str__(self):
        return "<" + str(self.num) + "/" + str(self.denom) + ">"
    def make_decimal(self):
        decimal = float(self.num) / float(self.denom)
        return decimal
    def reciprocal(self):
        return Fraction(self.denom, self.num)
    def add(self, other):
        new_num = (self.num * other.denom) + (self.denom * other.num)
        new_denom = (self.denom * other.denom)
        return Fraction(new_num, new_denom)
    
new_frac = Fraction(1, 93)
thirteen = Fraction(13, 1)
one_half = Fraction(1, 2)
one_55th = Fraction(1, 55)

x = new_frac.add(thirteen)
y = one_half.add(one_55th)
z = x.add(y)

z.make_decimal()

print(z, z.make_decimal())
