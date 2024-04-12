# jadi disini kita akan membuat sebuah logika perbandingan menggunakan if else dan or not
# kita akan membuat perbandingan antara nilaiAbsen dan nilaiTugas
# seperti contoh berikut :

nilaiTugas = 60
nilaiAbsen = 90


# perlu di ketahui bahwasannya python, tidak menggunakan lambang seperti && dan ||,
# kita langsung buat saja menjadi (and) atau (or)
if nilaiTugas >= 65 and nilaiAbsen >= 75:
    print("Anda Lulus")
else: print("Anda Gagal")
# <= otomatis hasilnya adalah Anda Gagal, karena ada satu yang bersifat false
print("")

# disini kita akan membuat contoh or nyaa.
if nilaiTugas >= 65 or nilaiAbsen >= 75:
    print("Anda Lulus")
else: print("Anda Gagal")
# <= otomatis anda lulus, dikarenakan ada satu yang bersifat true
print("")

# ini contoh not
x = 5
if x == 5: # <= disini kita akan menentukan jika x == 5 maka dia akan menghasilkan :
    print("X = 5")
else: print("X = bukan 5") # <= jika tidak.
# atau
a = True
print(not a)

