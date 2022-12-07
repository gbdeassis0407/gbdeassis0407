'''
import math
#from math import hypot

cat_op = float(input("Comprimento do cateto oposto: "))
cat_ad = float(input("Comprimento do cateto adjacente: "))

hip = math.sqrt((cat_op ** 2) + (cat_ad ** 2))

hip = math.hypot(cat_op, cat_ad)

print("A hipoltenusa vai medir = {:.2f}".format(hip))
'''
# -------------------------OR--------------------------
'''
cat_op = float(input("Comprimento do cateto oposto: "))
cat_ad = float(input("Comprimento do cateto adjacente: "))

hip = ((cat_op ** 2) + (cat_ad ** 2))
hip = pow(hip, 0.5)

print("A hipoltenusa vai medir = {:.2f}".format(hip))
'''
# -------------------------OR--------------------------

from math import hypot
cat_op = float(input("Comprimento do cateto oposto: "))
cat_ad = float(input("Comprimento do cateto adjacente: "))

hip = hypot(cat_op, cat_ad)

print("A hipoltenusa vai medir = {:.2f}".format(hip))
