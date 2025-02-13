import turtle
import sys


window = turtle.Screen()
window.title=("Aproximacion a los videojuegos")
window.bgcolor("#68a0ed")
window.setup(500,500)

class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")
        self.color("darkgreen")

    def adelante(self):
        self.forward(10)

    def atras(self):
        self.backward(10)

    def izquierda(self):
        self.left(15)
    
    def derecha(self):
        self.right(15)
    

    

kame = Tortuga()

window.onkey(kame.adelante, "w")
window.onkey(kame.atras, "d")
window.onkey(kame.izquierda, "s")
window.onkey(kame.derecha, "a")
window.onkey(sys.exit, "e")

window.listen()

turtle.mainloop()