import turtle

t = turtle.Turtle()
turtle.title("For You")

screen = turtle.Screen()
screen.bgcolor("black")

#drawing heart
t.color("red")
t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)

t.end_fill()

#writing text
t.up()
t.setpos(-65, 150)
t.down()
t.color("Lightgreen")
t.write("ILY", font=("verdana", 20, "bold"))

t.ht()

turtle.mainloop()