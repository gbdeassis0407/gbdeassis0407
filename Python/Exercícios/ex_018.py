
'''
import math
ang = float(input("Digite o ângulo que deseja: "))

ang_rad = math.radians(ang)
seno = math.sin(ang_rad)
cos = math.cos(ang_rad)
tang = math.tan(ang_rad)

print("O ângulo de {} tem o SENO de {:.2f}".format(ang, seno))
print("O ângulo de {} tem o COS de {:.2f}".format(ang, cos))
print("O ângulo de {} tem o TANG de {:.2f}".format(ang, tang))
'''
# ---------------------------OR---------------------------------

from math import radians, sin, cos, tan
ang = float(input("Digite o ângulo que deseja: "))

ang_rad = radians(ang)

print("O ângulo de {} tem o SENO de {:.2f}".format(ang, sin(ang_rad)))
print("O ângulo de {} tem o COS de {:.2f}".format(ang, cos(ang_rad)))
print("O ângulo de {} tem o TANG de {:.2f}".format(ang, tan(ang_rad)))
