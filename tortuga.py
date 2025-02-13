import turtle

#personalizacion de la ventana
window = turtle.Screen()
window.title("Prueba con turtle")
window.bgcolor("#68a0ed")
window.setup(500, 500)
window.setworldcoordinates(0,500, 500, 0)

#personalizacion de la pluma 
kame = turtle.Turtle()
kame.shape("turtle")
kame.color("darkgreen")
kame.pensize(2)
kame.speed(10)


#instrucciones de la pluma
for i in range(0, 10):
    kame.penup()
    kame.goto(i*25, i*25)
    kame.pendown()
    kame.circle(i*25)

#kame.speed(2)
#kame.penup()
#kame.goto(200, 200)
#kame.pendown()
#kame.goto(350, 200)
#kame.goto(350, 350)
#kame.goto(200, 350)
#kame.goto(200, 200)

#ame.circle(50)
#kame.circle(75)
#kame.circle(100)

print(kame.pos())

turtle.mainloop()