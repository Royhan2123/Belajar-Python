# ini adalah contoh untuk menginputkan angka dan kita akan menjumlahkan serta mengkalikan nya
# seperti contoh berikut :

print("Masukkan Angka pertama :")
satu = int(input()) # <= disini kita akan membuat sebuah int terlebih dahulu baru di dalamnya
# kita masukkan kode input,supaya data nya dari satu tidak terbaca menjadi string
print("")

print("Masukkan Angka kedua : ")
dua = int(input())
print("")

print("Masukkan Angka ketiga : ")
ketiga = int(input())
print("")

# lalu kita buat dulu sebuah variabel disini untuk menghasilkan total nyaa
total = satu + dua * ketiga

# lalu kita panggil disini dengan menggunakan string templates
print(f"Hasil dari pertambahan {satu} + {dua} x {ketiga} adalah : {total}")