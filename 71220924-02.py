#Input
inci1 = int(input("Masukan satuan inch:"))

#proses
kaki = inci1//12
inch = inci1-(kaki*12)
yard = kaki//3
kakii = kaki-(yard*3)
mil = yard//1760
yard = yard-(mil*1760)

#output
print(f"{inci1} inch = {mil} mile {yard} yard {kakii} feet {inch} inch")



