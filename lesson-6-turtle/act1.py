import turtle

turtle.Screen().bgcolor("orange")

sc = turtle.Screen()
sc.setup(500, 500)

turtle.title("Welcome to Turtle")
pen = turtle.Turtle()

for i in range(4):
    pen.forward(100)
    pen.right(90)
    i=i+i
turtle.done()