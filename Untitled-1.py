import turtle

# t = turtle.Turtle()
# t.clear()
#turtle.resetscreen()

#for i in range(4):
#   t.forward(100)
#   t.left(90)
# turtle.mainloop() 

t = turtle.Turtle()
def square(t, d, is_reset):

    for i in range(4):
        t.forward(d)
        t.left(90)
    
    if is_reset == True:
        reset()

def reset():
    turtle.resetscreen()

for i in range(1, 10):
    square(t, i * 5, False)




turtle.mainloop()

