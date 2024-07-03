# disini kita akan membuat sebuah perulangan menggunakan for
# seperti contoh berikut


nama = "Royhan" # <= jadi disini saya akan membuat var nama tersebut menjadi 10 kali menggunakan for

print("=============")
for _ in range(10): # <= disini kita memanggil range untuk membuat jumlah data seberapa banyak diulang.
    print(nama) # <= lalu kita printkan var nama, dan otomatis var
    # nama tersebut akan berulang menjadi 10 kali
print("==============")
print("")

# Lalu bagaimana dengan list ?
# contohnya seperti berikut :

namesHero = ["Hulk", "Ironman", "Superman", "Batman"]
print(namesHero)
print("")

for i in namesHero: # <= jadi disini kita buat dulu var i di dalam var namesHero
    print(f"Nama Nama Hero : {i}") # <= lalu otomatis kita panggil seperti ini
# dan otomatis hasilnya akan meliputi semua hero beserta
# text Nama Nama Hero yang dimana datanya menjadi 4
print("")