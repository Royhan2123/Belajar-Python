# disini kita akan membuat sebuah list
# seperti contoh berikut :

# berikut adalah contoh penggunaan list dengan menggunakan append, mungkin ini cara yang sedikit ribet
# jadi kita membaut sebuah variabel nama yang berisikan list kosong.
nama = []
# lalu setelahnya kita panggil lagi var nama tersebut dan tambahkan append. => nama.append()
# append di gunakan untuk menambahkan data
nama.append("Roy")  # <= di dalam append tersebut isikan data nya mau berupa string ataupun int
nama.append(5)
nama.append(True)
print(nama)

print("")

# berikut penggunaan list yang simple
namas = ["Roy", "Rey", "Ray"]
namas.append("Riy")  # <= otomatis var nama yang berisikan 3 data akan menjadi 4 data
print(namas)
print("")
namas.remove("Roy")  # ketika kita buat seperti ini otomatis data nya akan berubah dan otomatis
# data Roy dari var namas akan terhapus ketika kita memanggil ulang var nya
print(namas)
print("")
namas[1] = "Royhan"  # <= otomatis data Ray yang sekarang terganti posisi menjadi 1 akan berubah menjadi
# Royhan.
print(namas)
