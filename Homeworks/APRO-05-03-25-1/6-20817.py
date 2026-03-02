from turtle import *

screensize(10000, 10000)
tracer(0)
m = 10

for i in range(3):
    fd(27 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(6*m)
lt(90)
down()
for j in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
up()

for x in range(-80, 80):
    for y in range(-80, 80):
        goto(x * m, y * m)
        dot(3, 'red')


update()
exitonclick()