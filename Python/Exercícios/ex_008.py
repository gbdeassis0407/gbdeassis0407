dms = float(input("Digite sua distancia em metros = "))

cm = dms * 100
mm = dms * 1000
km = dms / 1000
polegada = dms * 39.370
jardas = dms * 1.0936

print("sua distancia em cm = {:.2f}cm ".format(cm))
print("sua distancia em mm = {:.2f}mm ".format(mm))
print("sua distancia em km = {:.4f}km ".format(km))
print("sua distancia em polegada = {:.2f}in ".format(polegada))
print("sua distancia em jardas = {:.4f}yd ".format(jardas))
