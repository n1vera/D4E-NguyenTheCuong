from turtle import *
speed(-1)
for x in range(1000):
    if x %2 == 0:
        a = 'green'
    elif x %2 != 0:
        a = 'red'
    else:
        a = 'blue'
    fillcolor(a)
    begin_fill()
    circle(200)
    left(56*2)
    end_fill()
mainloop()
