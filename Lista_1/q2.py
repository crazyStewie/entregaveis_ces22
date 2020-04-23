import turtle

def draw_poly(t : turtle.Turtle, n : int, sz : int):
    for _ in range(n):
        t.forward(sz)
        t.left(360/n)

square_side : int = 20
separation : int = 10

bob = turtle.Turtle()
bob.color('#fe6ab3', '#fe6ab3')

bob.pensize(4)
bob.screen.bgcolor('#90ee90')

draw_poly(bob, 8, 50)

turtle.done()




