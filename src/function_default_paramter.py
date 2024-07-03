# Belajar Default Argument value

# disini kita langsung memasukkan data nya ke dalam parameter yang di buat
def say_hello(first_name = "John", last_name = "Doe"):
    print("Hello " + first_name + " " + last_name)


# sehingga ketika kitat memanggil function nya, kita tidak mengisi data lagi.
say_hello()