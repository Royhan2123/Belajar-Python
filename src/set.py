#Belajar Set

# list => []
# tuple => ()
# set => {}

# tipe data set otomatis tidak menghitung data yang sama, seperti contoh di bawah ini
# ada dua nama Royhan, otomatis hanya satu saja di panggil.
nama = {"Royhan", "Reyhan", "Royhan", "Rizki"} # Output: {"Royhan", "Rizki", "Reyhan"}
print(nama)

nama.add("Rayhan")
print(nama)
print("")
for i in nama:
    print(i)

nama.remove("Reyhan")
print(nama)

