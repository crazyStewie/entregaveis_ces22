import turtle

square_side : int = 20
separation : int = 10

bob = turtle.Turtle()
bob.color('#fe6ab3', '#fe6ab3')

bob.pensize(4)
bob.screen.bgcolor('#90ee90')

for i in range(5):
    bob.pendown()
    for j in range(4):
        bob.forward(square_side)
        bob.left(90)
    bob.penup()
    bob.right(90)
    bob.forward(separation)
    bob.right(90)
    bob.forward(separation)
    bob.right(180)
    square_side += 20
turtle.done()




