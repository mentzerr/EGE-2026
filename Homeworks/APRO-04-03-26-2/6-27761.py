from turtle import *


screensize(10000, 10000)
tracer(0)
m = 10

for i in range(2):
    fd(1 * m)
    lt(270)
    fd(16 * m)
    rt(90)
up()
bk(4 * m)
rt(90)
fd(10 * m)
lt(90)
down()
for j in range(2):
    fd(17 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
exitonclick()