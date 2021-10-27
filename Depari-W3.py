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

#Punya mas Awan buat quiz

# count = int(input("Berapa data: "))

# nama_pelanggan = []
# umur_pelanggan = []

# #fungsi format (i+1) karena semua di python mulai dari 0
# for i in range(count):
#     print("Data ke {}". format(i+1))
#     nama = input("Nama : ")
#     umur = int(input("umur : "))

#     nama_pelanggan.append(nama)
#     umur_pelanggan.append(umur)

# for i in range(count):
#     print("Pelanggan {} berusia {}". format(nama_pelanggan[i], umur_pelanggan[i]))


#2 While Loops
#pengulangan yang kita eksekusi terus menerus selama kondisinya terpenuhi

#berhentiin while pake ctrl + c
# i = 1
# while i<6:
#     print(i)

# for i in range(5):
#     print(i)

#continue artinya tidak akan menjalankan perintah dibawahnya

#fungsi break untuk stop angka di mana kita minta dia berhenti

#or itu untuk 1 kriteria terpenuhi, and itu untuk 2 kriteria terpenuhi
# for i in range(5):
#     if i == 2:
#         break
#     print(i)

# print (" ")

# for i in range(5):
#     if i == 2 or i == 3:
#         continue
    # print(i)

# for i in range(3):
#     print("i: {}". format(i))
#     for j in range (3):
#         print("j: {}". format(j))

# for baris in range(5):
#     for kolom in range(5):
#         print("{}.{}". format(baris+1, kolom+1), end=" ")
#     print()

x = [1,2,3,4,5]
y = [2,4,3,5,6]
z = 0

for i in x :
    for j in y :
        if i == j:
            z = z+1

print(z)

