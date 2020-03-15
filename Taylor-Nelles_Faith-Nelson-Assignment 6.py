# -----------------------------------------+
# Taylor Nelles and Faith Nelson           |
# CSCI 107, Assignment 6                   |
# Last Updated: October 19, 2018           |
# -----------------------------------------|
# Create a Roman-style tile mosaic with a  |
# user-supplied number of rows and columns.|
# -----------------------------------------+

import turtle
import random

# -----------------------------------------+
# create_turtle                            |
# -----------------------------------------+
# This function has no parameters.         |
# -----------------------------------------+
# Create and return a hidden turtle with   |
# shape "turtle" and speed 0.              |
# -----------------------------------------+

def create_turtle():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.shape("turtle")
    return turtle
# -----------------------------------------+
# draw_square                              |
# -----------------------------------------+
# rectangle: the name of the turtle        |
# x: upper left corner x-coordinate        |
# y: upper left corner y-coordinate        |
# width: width of rectangle                |
# height: height of rectangle              |
# -----------------------------------------+
# Draw a rectangle with a random fill      |
# color and black border.  A turtle should |
# be stamped in the middle, pointing right.|
# -----------------------------------------+

def draw_square(rectangle, x, y, width, height):
    rectangle.penup()
    rectangle.goto(x,y)
    rectangle.pendown()
    R = random.random()
    G = random.random()
    B = random.random()
    rectangle.pencolor("black")
    rectangle.fillcolor(R, G, B)
    rectangle.begin_fill()
    for side in range(2):
        rectangle.forward(width)
        rectangle.left(90)
        rectangle.forward(height)
        rectangle.left(90) 
    rectangle.penup()
    rectangle.goto(x + width/2, y + height/2)
    rectangle.stamp()
    rectangle.end_fill()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# This function has no parameters.         |
# -----------------------------------------+
# This function should create a turtle,    |
# prompt the user for the number of row    |
# columns and then draw the mosaic.  Call  |
# the other two functions as appropriate.  |
# -----------------------------------------+

def main():
    mosaic = create_turtle()
    y = window.window_height()
    x = window.window_width()
    rows = int(input("Enter the number of rows for the mosaic:"))
    columns = int(input("Enter the number of columns for the mosaic:"))
    rectangle_width = x/columns
    rectangle_height = y/rows
    for i in range(columns):
        for j in range(rows):
            draw_square(mosaic, -x/2 + i*(rectangle_width), -y/2 + j*(rectangle_height), rectangle_width, rectangle_height)

# -----------------------------------------+

window = turtle.Screen()
window.title("Mosaic")
main()
window.exitonclick()
