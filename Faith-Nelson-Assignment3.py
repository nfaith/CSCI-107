# -----------------------------------------+
# Faith Nelson                             |  
# CSCI 107, Assignment 3                   |
# Last Updated: September 21, 2018         |  
# -----------------------------------------|
# This will create a lilypad with a        |
# pink lily flower that would give extra   |
# time for the player in the next froggy   |
# run.                                     | 
# -----------------------------------------+

import turtle


lilypad = turtle.Turtle()

lilypad.color("green")

lilypad.goto(0,0)
lilypad.shape("square")
lilypad.shapesize(8)
lilypad.stamp()

for courners in range(4):
    lilypad.penup()
    lilypad.shape("circle")
    lilypad.goto(0,0)
    lilypad.right(45)
    lilypad.forward(100)
    lilypad.shapesize(3)
    lilypad.stamp()
    lilypad.right(45)


lilypad.goto(15,15)
lilypad.pensize(20)
lilypad.color("pink")
lilypad.hideturtle()

numPetals = 4

for petals in range(numPetals):
    lilypad.pendown()
    lilypad.circle(10,280)
    lilypad.penup()
    lilypad.left(180)
    lilypad.forward(10)



lilypad.penup()
lilypad.color("yellow")
lilypad.shape("circle")
lilypad.goto(5,20)
lilypad.shapesize(1.5)
lilypad.stamp()
lilypad.penup()
    







