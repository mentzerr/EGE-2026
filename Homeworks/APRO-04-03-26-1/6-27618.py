from turtle import *

screensize(10000, 10000)
tracer(0)
m = 10

for i in range(2):
    fd(3 * m)
    lt(90)
    bk(10 * m)
    lt(90)
up()
bk(10 * m)
rt(90)
fd(8 * m)
lt(90)
down()
for j in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')


update()
exitonclick()
