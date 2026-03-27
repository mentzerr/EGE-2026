from turtle import *

screensize(10000, 10000)
tracer(0)
m = 10

for j in range(4):
    fd(36 * m)
    rt(90)
    fd(41 * m)
    rt(90)
up()
rt(90)
fd(20 * m)
lt(90)
fd(20 * m)
down()
for i in range(4):
    fd(25 * m)
    rt(90)
up()
fd(7 * m)
lt(90)
fd(7 * m)
rt(90)
down()
for k in range(7):
    fd(16 * m)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'blue')

exitonclick()
update()