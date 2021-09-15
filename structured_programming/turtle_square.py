import turtle

def run():

    window = turtle.Screen()
    turtle1 = turtle.Turtle()

    for i in range(4):
        turtle1.forward(100)
        turtle1.right(90)

    window.mainloop()


if __name__ == '__main__':
    run()