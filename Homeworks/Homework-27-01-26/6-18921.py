from turtle import *

screensize(10000, 10000)
tracer(0)
m = 15

for i in range(13):
    fd(13*m)
    rt(90)
    fd(5*m)
up()
rt(90)
fd(7*m)
lt(90)
fd(10*m)
down()
for j in range(23):
    fd(8*m)
    lt(90)
    fd(11*m)
    lt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, 'blue')


exitonclick()
update()
