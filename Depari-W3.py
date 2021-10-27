#Loop adalah perintah untuk berulang di python sehingga kode nya lebih ringkas

#Loop ada 2 di python
#1 For Loops = pengulangan menggunakan urutan tertentu
#fungsi pengulangan yang terjadi dari semua yang ada di rentang loop nya

#kalau mau print satu, satu bisa pilih atau lakuin kayak dibawah
# sayur = ["bayam","terong","tomat"]

# print(sayur[0])
# print(sayur[1])
# print(sayur[2])

#pengulangan for loops hanya terjadi pada kolom for loops

# nama_sayur = ['tomat','kangkung','bayam','toge','tahu','tempe']

# for sayur in nama_sayur:
#     print(sayur)
#     print("---")

# print('lol')

#range adalah fungsi dari sekuensial nomor, mulai dari 0 dna dikurangi 1.
#keyword range(start,stop,step/selisih)
#range hanya untuk number
#yang wajib di isi adalah stop. karena start & step sudah ada nilainya

# for b in range(3) :
#     print(b)

# print(" ")

# for i in range(1, 3) :
#     print(i)

# print (" ")

# for c in range(1, 9, 3):
#     print(c)

# Punya gua salah
# b = ["ayam","babi","cicak","domba","entok"]
# c = input("Enter hewan: ") 

# d = len(b)

# print(d)

# for c in b:
#     print(b)


#julio hasilnya

# nama = []
# list = []

# kuota = input("Jumlah orang: ")
# kuota = int(kuota)

# for n in range(kuota):
#     nama = input("Enter name: ")
#     list = []
#     list.append (nama)

# print(list)

#Punya mas Awan

count = int(input("Berapa data: "))

nama_pelanggan = []
umur_pelanggan = []

for i in range(count):
    print("Data ke {}". format(i+1))
    nama = input("Nama : ")
    umur = int(input("umur : "))

    nama_pelanggan.append(nama)
    umur_pelanggan.append(umur)

for i in range(count):
    print("Pelanggan {} berusia {}". format(nama_pelanggan[i], umur_pelanggan[i]))


#2 While Loops