#inputna.
import math
x1 = int(input("masukan x1:"))
x2 = int(input("Masukan x2:"))
y1 = int(input("Masukan y1:"))
y2 = int(input("Masukan y2:"))

#Prosesna.
jarak_2titik = math.sqrt((x2-x1)**2 + (y2-y1)**2)
jarak_2titik = int(jarak_2titik*10)/10

#Outputna
print("Jarak 2 titik = %.1f" %(jarak_2titik))