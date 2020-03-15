import turtle

# -----------------------------------------+
# Faith Nelson & Taylor Nelles             |
# CSCI 107, Assignment 5                   |
# Last Updated: October 12, 2018           |
# -----------------------------------------|
# Create an object that you would find in  |
# minecraft. We decided to make a horse.   |
# -----------------------------------------+


window = turtle.Screen()
window.title("Horse")

horse = turtle.Turtle()
horse.hideturtle()
horse.color("brown")
horse.speed(0)

mane = turtle.Turtle()
mane.hideturtle()
mane.speed(0)
mane.color("sandybrown")

def setup_turtle(turtle,x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def draw_square(square, center_x, center_y, square_color):
    setup_turtle(square,center_x, center_y)
    square.fillcolor(square_color)
    square.begin_fill()
    for side in range(4):
        square.forward(20)
        square.right(90)
    square.end_fill()

def line(turtle, turtle_color, start_x, start_y, end_x, end_y):
    setup_turtle(turtle, start_x, start_y)
    turtle.fillcolor(turtle_color)
    turtle.begin_fill()
    turtle.goto(end_x, end_y)
    turtle.end_fill()

def draw_triangle(triangle, x, y, x_direction, y_direction, triangle_color):
    setup_turtle(triangle, x, y)
    triangle.fillcolor(triangle_color)
    triangle.begin_fill()
    triangle.goto(x,y + (y_direction * 20))
    triangle.goto(x+ (x_direction * 20), y + (y_direction * 20))
    triangle.goto(x,y)
    triangle.end_fill()


## Draws Horse head
draw_square(horse, -100, 100, "chocolate")
draw_square(horse, -120, 80, "turquoise") 
draw_square(horse, -140, 60, "chocolate")
for x in range(40, 180, 20):
    draw_square(horse, -x, 40, "chocolate")

draw_square(horse, -40, -40, "chocolate")

for x in range(60, 140, 20):
    draw_square(horse, -x, 60, "chocolate")
for x in range(80, 120, 20):
    draw_square(horse, -x, 80, "chocolate")

for x in range(20, 120, 20):
    draw_square(horse, -x, 20, "chocolate")

for x in range(40, 100, 20):
    draw_square(horse, -x, 0, "chocolate")

for x in range(40, 80, 20):
    draw_square(horse, -x, -20, "chocolate")

draw_triangle(horse,-120, 80, -1,-1,"chocolate")
draw_triangle(horse,-140, 60,-1,-1,"chocolate")

draw_triangle(horse, -80,-20,-1,1,"chocolate")
draw_triangle(horse, -60,-40,-1,1,"chocolate")
draw_triangle(horse, -40,-60,-1,1,"chocolate")
draw_triangle(horse, -20,-80,-1,1,"chocolate")


## Draws horse mane
for x in range(60,100, 20):
    draw_square(mane, -x, 100, "moccasin")

for x in range(40,80,20):
    draw_square(mane, -x, 80, "moccasin")

for x in range(20,60,20):
    draw_square(mane, -x, 60, "moccasin")

for x in range(0,40,20):
    draw_square(mane, -x, 40, "moccasin")

draw_square(mane, 0, 20, "moccasin")

draw_triangle(mane, -40, 100,1, -1, "moccasin")
draw_triangle(mane, -20, 80, 1, -1, "moccasin")
draw_triangle(mane, 0, 60, 1, -1, "moccasin")

# Horse tail

for x in range(180, 220, 20):
    draw_square(mane, x, 0, "moccasin")
##draw_square(mane, 180, 0, "moccasin")
##draw_square(mane, 200, 0, "moccasin")

for x in range(200, 240, 20):
    draw_square(mane, x, -20, "moccasin")

##draw_square(mane,220 , -20, "moccasin")
##draw_square(mane,200, -20, "moccasin" )

for x in range(200, 240, 20):
    draw_square(mane, x, -40, "moccasin")

##draw_square(mane,200, -40, "moccasin")
##draw_square(mane,220, -40, "moccasin")

for x in range(220, 260, 20):
    draw_square(mane, x, -60, "moccasin")

##draw_square(mane,220, -60, "moccasin")
##draw_square(mane,240, -60, "moccasin")

for x in range(240, 280, 20):
    draw_square(mane, x, -80, "moccasin")

##draw_square(mane, 240, -80, "moccasin")
##draw_square(mane,260 , -80, "moccasin")

for x in range(260, 280, 20):
    draw_square(mane, x, -100, "moccasin")

##draw_square(mane,260 , -100, "moccasin")
##draw_square(mane, 280, -100, "moccasin")

draw_triangle(mane, 200, -40,-1,1, "moccasin")
draw_triangle(mane, 220, -80,-1,1, "moccasin")
draw_triangle(mane, 240, -100,-1,1, "moccasin")
draw_triangle(mane, 260, -120,-1,1, "moccasin")

## Draws horse body

for y in range( 0, 100, 20 ):
    for x in range(-20, 180, 20):
        draw_square(horse, x, -y, "chocolate")

## Draws the legs
for y in range(100, 200, 20):
    for x in range(-20, 20, 20):
        draw_square(horse, x, -y, "chocolate")
    for x in range(140, 180, 20):
        draw_square(horse, x, -y, "chocolate")
    

## Draws the hooves
hoof = turtle.Turtle()
hoof.hideturtle()
hoof.speed(0)
hoof.color("black")
     
for x in range(-20,20,20):
        draw_square(hoof, x, -200, "dimgray")
for x in range(140,180,20):
        draw_square(hoof, x, -200, "dimgray")
        
        

    



