from turtle import *

screensize(10000, 1000)
tracer(0)
m = 10

for i in range(4):
    fd(10 * m)
    rt(270)
up()
fd(3 * m)
rt(270)
fd(5 * m)
rt(90)
down()
for j in range(2):
    fd(10 * m)
    rt(270)
    fd(12 * m)
    rt(270)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y * m)
        dot(3, 'blue')


update()
exitonclick()