import tkinter as tk
import turtle

def draw_heart():
    t = turtle.Turtle()
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
    t.setpos(-100, 150)
    t.down()
    t.color("Lightgreen")
    t.write("I <3 YOU LIA", font=("Verdana", 20, "bold"))

    t.ht()

def create_heart():
    draw_heart()

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

button1 = tk.Button(text='Click Me', command=create_heart, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
