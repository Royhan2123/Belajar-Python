import turtle

screen = turtle.Screen()
screen.bgcolor("white")


t = turtle.Turtle()
t.shape("turtle")  
t.color("red")     
t.speed(1)         


t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()


t.penup()          
t.goto(-50, -200)  
t.pendown()        


t.color("black")   
t.write("Ini untukmu", align="center", font=("Arial", 24, "bold"))


turtle.done()