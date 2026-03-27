from turtle import *

screensize(10000, 10000)
tracer(0)
m = 10

for i in range(2):
    fd(10 * m)
    rt(90)
    fd(20 * m)
    rt(90)
up()
bk(4 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for j in range(4):
    fd(8 * m)
    lt(90)
    fd(12 * m)
    lt(90)
up()
fd(10 * m)
down()
for k in range(4):
    fd(12 * m)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
exitonclick()