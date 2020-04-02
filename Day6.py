import turtle

def list_sum(num_list):
    if len(num_list) == 1:

        return num_list[0]

    else:

        return num_list[0] + list_sum(num_list[1:])


print(list_sum([1, 3, 5, 7, 9]))


def to_str(n, base):
    convert_string = "0123456789ABCDEF"

    if n < base:

        return convert_string[n]

    else:

        return to_str(n // base, base) + convert_string[n % base]

# turtle is standard python module that shows graphic rep

# my_turtle = turtle.Turtle()
#
# my_win = turtle.Screen()



# def draw_spiral(my_turtle, line_len):
#
#         if line_len > 0:
#
#                 my_turtle.forward(line_len)
#
#                 my_turtle.right(90)
#
#                 draw_spiral(my_turtle, line_len - 5)
#
# draw_spiral(my_turtle, 100)

# my_win.exitonclick()

# fractal has same basic shape no matter magnification
# coastline, snowflake, trees and shrubs are real life example
# main idea of fractal tree - has same shape and characteristiscs as whole tree

# tree is a trunk with a smaller tree going of to right and other smaller ree going to left

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 10, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()

main()

# sierpinski triangle is another fractal
# start with dividing triangle in four, ignore the middle and do the same with the rest

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)

    my_turtle.up()

    my_turtle.goto(points[0][0], points[0][1])

    my_turtle.down()

    my_turtle.begin_fill()

    my_turtle.goto(points[1][0], points[1][1])

    my_turtle.goto(points[2][0], points[2][1])

    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, my_turtle):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']

    draw_triangle(points, color_map[degree], my_turtle)

    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1, my_turtle)
        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree - 1, my_turtle)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree - 1, my_turtle)

def triangleMain():
        my_turtle = turtle.Turtle()

        my_win = turtle.Screen()

        my_points = [[-100, -50], [0, 100], [100, -50]]

        sierpinski(my_points, 3, my_turtle)

        my_win.exitonclick()


triangleMain()
