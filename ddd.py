import turtle
import random
turtle.speed(0)

for r in range(10):
    x = random.randint(-300,300)
    y = random.randint(-300, 300)
    r = random.randint(1,100)
    turtle.penup()
    turtle.goto(x, y-r)
    turtle.pendown()
    turtle.circle(r)
    print(f"좌표({x},{y}) / 반지름({r})")
turtle.done()