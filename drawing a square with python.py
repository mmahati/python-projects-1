import turtle

my_turtle = turtle.Turtle()
# my_turtle.speed(1)

def square(length, angle):
    for i in range(4):
        my_turtle.foward(length)
        my_turtle.right(angle)

square(100, 90)

