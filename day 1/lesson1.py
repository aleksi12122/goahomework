from turtle import *

#step 1: draw a rectangle

width(3)

speed(7)

color("black")

forward(200)
right(90)

forward(250)
right(90)

forward(200)
right(90)

forward(250)
right(90)

#step 2: draw the door

penup()
goto(75,-250)
pendown()

width(4)

color("brown")

begin_fill()
left(90)
forward(100)

right(90)
forward(50)

right(90)
forward(100)
end_fill()


#step 3: make the roof

penup()
goto(200,0)
pendown()

width(5)

color("red")

begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#step 4:draw the windows

width(3)

color("yellow")

penup()
goto(175,-100)
pendown()
left(210)
forward(80)

left(90)
forward(50)

left(90)
forward(80)

left(90)
forward(50)

penup()
goto(75,-100)
pendown()

left(90)
forward(80)

left(90)
forward(50)

left(90)
forward (80)

left(90)
forward(50)


penup()
goto(150,-100)
pendown()

left(90)
forward(80)

penup()
goto(175,-60)
pendown()

left(90)
forward(50)

penup()
goto(50,-100)
pendown()

right(90)
forward(80)


penup()
goto(25,-60)
pendown()


right(90)
forward(50)

#step 5: make the doorknob

color("black")

begin_fill()


penup()
goto(125,-175)
pendown()

left(180)
forward(15)

left(90)
forward(15)

left(90)
forward(15)

left(90)
forward(15)

end_fill()


exitonclick()


