from turtle import *

width(7) #line bold, ხაზის სისქე,
color("purple")

#building, შენობა
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

forward(80)


#door
begin_fill()
color("green")
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()

#roof
begin_fill()
color("pink")
right(180)
left(45)
forward(145)
left(90)
forward(145)
end_fill()

#window
begin_fill()
color("yellow")
penup()
goto(20,180) #გადასვლა
pendown()

left(45)
forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)
end_fill()

#window 2
begin_fill()
color("yellow")
penup()
goto(140,180)
pendown()


forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

end_fill()


exitonclick() #გამოსვლა დაკლიკებით+