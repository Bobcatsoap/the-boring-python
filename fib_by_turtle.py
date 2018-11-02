import turtle


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        myTurtle.circle(b * 2, 90)
        a, b = b, a + b
        n += 1
    return "done"


myTurtle = turtle.Turtle()
fib(15)
turtle.getscreen()._root.mainloop()
