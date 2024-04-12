# disini kita akan membuat sebuah string, mungkin sama seperti bahasa pemograman lainnya
# disini kita langsung menggunakan koma dua atas saja("isi_data")
# seperti contoh berikut :

nama = "Royhan"
alamat = "Jln panglima Tempur"
umur = 12

# contoh penggunaan string templates di bahasa pemograman phyton.
# f akan otomatis kepanggil ketika kita memanggil {} <= variabel ke dalam string.
# f = format
print(f"Nama saya adalah {nama}\nAlamat Saya di {alamat}\nUmur Saya adalah {umur}")


# cara membuat int menjadi string, biasanya menggunakan .toString
# tetapi ketika di python menggunakan str. <= str adalah kode untuk membuat menjadi string
# jadi kita buat dulu str(nama_var_bersifat_int)
print(nama + alamat + str(umur))