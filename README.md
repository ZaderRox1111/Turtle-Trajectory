# Turtle-Trajectory
Finding the trajectory of an object using the turtle library.


Kyle Elison kje237@nau.edu
Zach Derrick zcd22@nau.edu
# Understanding the Problem
The goal of this project is to launch a turtle and draw out its trajectory through
the built-in turtle library.
## Variables are given:
- Launch Velocity
- Launch Angle
- Acceleration due to gravity
- Time Step
- Launch Height
# Plan a Solution
Firstly, we are going to use a loop in order for the equation to work effectively.
These are the variables that we think we are going to need as of now.
## Variables:
- lVelocity = launch velocity
- xVelocity = X component of the launch velocity
- yVelocity = Y component of the launch velocity
- xPos = Position of x
- yPos = Position of y
- lAngle = lauch angle
- g = Acceleration due to gravity
- t = time
- dt = time step
- lHeight = launch height
- Based on the research we’ve done, these are the formulas we’ve come to.
## Formulas:
- yVelocity = lVelocity*sin(lAngle)
- xVelocity = lVelocity*cos(lAngle)
- yVelocity = yVelocity + (g * dt)
- t = t + dt
- xPos = xPos + (xVelocity * dt)
- yPos = yPos + (yVelocity * dt)
- We will create a function that plots the current x and y points that the turtle is
traveling in, and that function updates the time and velocity every iteration,
which is done by a loop in the main function.
# Implementation and testing
We first started out by importing the math and the turtle libraries so we could
draw and use the sin and cos functions. We then created all of our variables at
the beginning and outside any functions so they had scope over the entire
program, and then we created a turtle object.
We then defined the function Trajectory where the loop would take place that
calculates plots the points every iteration.
Our first few attempts had an error where the variables were being used before
they were referenced so we just moved all the variables into the trajectory
function so they’d be in the scope.
After adding the turtle.Screen().exitonclick(), we finally got the program to work
effectively, and then we changed the time step to make it more accurate. We then
we’re messing around with the values of various variables to see how it would
affect the launch.
# Reflect and refactor
Out solution works, however, there are a few things that we could have done
differently. We could have put the majority of the variables determining the
launch (e.g angle, height, launch velocity), into the argument of the function so
that the user could have multiple different launches with one execution of the
code. We could also further adapt that idea and make the user enter the
arguments when the code is running, and have that in a loop so they can keep
launching as much as they want during the program.
One of the problems that we came to was that the variables we defined at the
beginning, outside of any functions, weren’t able to be used within our Trajectory
function, but it would have been good practice to define those variables within
the Trajectory function anyway because it would have been good practice and
saved more namespace for a potentially much larger program.
Some additional time has passed and we’ve implemented the feature allowing
multiple different turtles to be created and launched within one execution of the
program
