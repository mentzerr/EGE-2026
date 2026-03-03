from turtle import *

screensize(10000, 10000)
tracer(0)
m = 10

for i in range(5):
    fd(42 * m)
    rt(270)
    fd(55 * m)
    lt(90)
up()
fd(17 * m)
rt(90)
fd(12 * m)
lt(90)
down()
for j in range(14):
    fd(14 * m)
    lt(90)
    fd(200 * m)
    lt(90)
up()

for x in range(11, 26):
    for y in range(0, 56):
        goto(x * m, y * m)
        dot(3, 'red')


update()
exitonclick()
