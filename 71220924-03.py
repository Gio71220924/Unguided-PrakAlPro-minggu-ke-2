#input

waktu_detik = input("Masukan Waktu:")

#Prosess
detik = waktu_detik//60
menit = waktu_detik-(detik*60)
jam = detik//3600
detik1 = detik-(jam*3600)
hari = 