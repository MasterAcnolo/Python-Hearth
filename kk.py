import turtle

def draw_heart():
    window = turtle.Screen()
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.color("red")
    pen.pensize(3)
    pen.speed(1)

    pen.begin_fill()

    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)

    pen.end_fill()

    pen.hideturtle()

def write_message():
    pen = turtle.Turtle()
    pen.color("black")
    pen.penup()
    pen.goto(-60, 40)
    pen.pendown()
    pen.write("INSERT TEXT HERE", font=("Arial", 18, "bold"))
    pen.hideturtle()


draw_heart()


write_message()


turtle.done()
