import turtle

# Membuat layar turtle
screen = turtle.Screen()
screen.bgcolor("white")

# Membuat turtle
t = turtle.Turtle()
t.shape("turtle")  # Bentuk turtle bisa diubah sesuai keinginan
t.color("red")     # Warna turtle diatur menjadi merah
t.speed(1)         # Kecepatan turtle (1 adalah lambat, bisa disesuaikan)

# Menggambar love shape
t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

# Posisi turtle untuk menulis kata-kata di bawah love shape
t.penup()          # Mengangkat pena turtle
t.goto(-50, -200)  # Posisi turtle
t.pendown()        # Menurunkan pena turtle

# Menulis kata-kata
t.color("black")   # Warna tulisan hitam
t.write("Ini untukmu", align="center", font=("Arial", 24, "bold"))

# Menahan jendela sampai ditutup pengguna
turtle.done()