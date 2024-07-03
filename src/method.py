# Belajar Membuat Method / Function

nama = []

nama.append("Roy")
print("=============")
for data in nama:
    print(data)

nama.append("Han")
print("==============")
for data in nama:
    print(data)

# dengan Menggunakan Function
def print_nama():
    print("===============")
    for data in nama:
        print(data)


print_nama()
