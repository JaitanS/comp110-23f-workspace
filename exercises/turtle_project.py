"""Pink house in the forest. Above and Beyond: Tree heights are randomized for each tree and Tree function is broken down (triangle function)."""
__author__ = "730675117"
import random
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None: 
    """Entrypoint to scene."""
    tim: Turtle = Turtle()
    tree(tim, -500.0, 0.0)
    tree(tim, -400.0, 0.0)
    tree(tim, -300, 0.0)
    tree(tim, 500.0, 0.0)
    tree(tim, 400.0, 0.0)
    tree(tim, 300.0, 0.0)
    house(tim, 100.0, 0.0)
    door(tim, 7.5, 0.0)
    done()


def triangle(tim: Turtle, x: float, y: float) -> None:
    """Draws Triangles."""
    tim.penup()
    tim.goto(x, y) 
    tim.setheading(0.0)
    tim.pendown()
    i: int = 0
    while i < 3: 
        tim.left(120)
        tim.forward(70)
        i += 1
    return


def tree(tim: Turtle, x: float, y: float) -> None:
    """Draws trees."""
    tim.penup()
    tim.goto(x, y) 
    tim.setheading(0.0)
    tim.pendown()
    tim.color(55, 30, 25)
    tim.begin_fill()
    i: int = 0
    tree_height: int = random.randint(100, 200)
    while i < 2: 
        tim.left(90)
        tim.forward(tree_height)
        tim.left(90)
        tim.forward(20)
        i += 1
    tim.end_fill()
    tim.penup()
    tim.goto(x, y) 
    tim.setheading(0.0)
    tim.pendown()
    tim.color(26, 62, 11)
    tim.begin_fill()
    triangle(tim, (x + 25), (y + tree_height))
    tim.end_fill()
    tim.penup()
    tim.goto(x, y) 
    tim.setheading(0.0)
    tim.pendown()
    tim.begin_fill()
    triangle(tim, (x + 25), (y + tree_height + 30))
    tim.end_fill()
    return 


def door(tim: Turtle, x: float, y: float) -> None:
    """Draws a door for house."""
    tim.penup()
    tim.goto(x, y) 
    tim.setheading(0.0)
    tim.pendown()
    tim.color(95, 70, 57)
    tim.begin_fill()
    i: int = 0
    while i < 2: 
        tim.left(90)
        tim.forward(30)
        tim.left(90)
        tim.forward(15)
        i += 1
    tim.end_fill()
    return


def house(tim: Turtle, x: float, y: float) -> None: 
    """Draws the house."""
    tim.penup()
    tim.goto(x, y) 
    tim.setheading(0.0)
    tim.pendown()
    tim.color(169, 95, 156)
    tim.begin_fill()
    i: int = 0
    while i < 2:
        tim.left(90)
        tim.forward(100)
        tim.left(90)
        tim.forward(200)
        i += 1
    tim.end_fill()
    tim.penup()
    tim.goto(x, (y + 100)) 
    tim.setheading(0.0)
    tim.pendown()
    tim.color(168, 123, 99)
    tim.begin_fill()  
    tim.left(135)
    tim.forward(141.421)
    tim.left(90)
    tim.forward(141.421)
    tim.left(135)
    tim.forward(200)
    tim.end_fill()
    return


if __name__ == "__main__":
    main()
