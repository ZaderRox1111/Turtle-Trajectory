import turtle
from math import sin, cos, pi, radians

def main():
    #turtles
    ezekiel = turtle.Turtle()

    turtle.Screen().delay(0)
    turtle.setworldcoordinates(-100, -300, 600, 300)

    trajectory(ezekiel, 50, 60, 'red')

    turtle.exitonclick()


def trajectory(turtle, launchVel, launchAngle, color):
    launchAngle = radians(launchAngle)
    G = 9.81
    totalTimeSteps = 20

    turtle.color(color)

    for t in range(0, totalTimeSteps):
        x = launchVel * t * cos(launchAngle)
        y = launchVel * t * sin(launchAngle) - 0.5 * G * t**2
        turtle.goto(x, y)


main()
