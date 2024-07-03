# Belajar Argument List


# disini kita akan membhuat sebuah perjumlahan satu dan dua
def jumlahkan(satu, dua):
    # disini saya menambahkan parameter satu, dua, lalu di bawahnya saya buat variabel total
    total = satu + dua
    # yang dimana menampung parameter satu dan dua tersebut.
    print(f"Total {[satu, dua]} = {total}")
    # lalu saya memanggil mereka di function jumlahkan tersebut


jumlahkan(10, 10)  # sehingga disini saya hanya menginputkan \
# data nya saja, dan otomatis sudah ketambah

print("")


# lalu bagaimana ketika kita langsung menggunakan list di dalam paramter tersebut ???
# contoh nya di bawah ini :
def jumlahkanList(*list_angka):  # kita membuat sebuah paramter yang bernama list_angka
    # jika kita ingin menambahkan parameter baru lagi ke dalam function jumlahkanList() tersebut.
    # kita harus menaruh list paramter tersebut di paling belakang.
    # contoh :
    # def jumlahkanList(NEW_PARAMETER,*list_angka) <- seperti itu.
    # dan list paramter hanya bisa di pakai satu kali, jika lebih dari satu
    # maka akan menyebabkan ERROR.

    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")


# dengan kita menambahkan tanda (*) otomatis nilai parameter list_angka tersebut menjadi LIST
# yang dimana kita bisa menambahkan data sebanyak yang kita mau.
# lalu di dalamnya kita membuat sebuah var total dengan nilai 0
# lalu tinggal kita buatkan saja perulangan yang dimana total = total + angka
# total = 0, dan angka adalah nama perulangan tersebut yang mengambil parameter list_angka
# lalu tinggal kita print(Total {list_angka} = {total})  <-- output :
# print(Total (DATA YANG DI INPUT) = {HASIL DARI DATA YANG SUDAH DI TAMBAHKAN})
# dikarenakan di perulangan tersebut kita sudah menambahkan data nya ke dalam perulangan


jumlahkanList(15, 15, 15, 15, 15, 15, 1242, 124, 125, 124, 125)  # output: 1830
