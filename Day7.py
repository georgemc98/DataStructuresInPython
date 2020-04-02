import turtle
#
# def draw_triangle(points, color, my_turtle):
#     my_turtle.fillcolor(color)
#
#     my_turtle.up()
#
#     my_turtle.goto(points[0][0], points[0][1])
#
#     my_turtle.down()
#
#     my_turtle.begin_fill()
#
#     my_turtle.goto(points[1][0], points[1][1])
#
#     my_turtle.goto(points[2][0], points[2][1])
#
#     my_turtle.goto(points[0][0], points[0][1])
#     my_turtle.end_fill()
#
# def get_mid(p1, p2):
#     return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
#
# def sierpinski(points, degree, my_turtle):
#     color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
#
#     draw_triangle(points, color_map[degree], my_turtle)
#
#     if degree > 0:
#         sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1, my_turtle)
#         sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree - 1, my_turtle)
#         sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree - 1, my_turtle)
#
# def triangleMain():
#         my_turtle = turtle.Turtle()
#
#         my_win = turtle.Screen()
#
#         my_points = [[0, 100], [-100, -50], [100, -50]]
#
#         sierpinski(my_points, 3, my_turtle)
#
#         my_win.exitonclick()
#
#
# triangleMain()

#
# def move_tower(height, from_pole, to_pole, with_pole):
#     if height >= 1:
#         move_tower(height - 1, from_pole, with_pole, to_pole)
#
#         move_disk(from_pole, to_pole)
#
#         move_tower(height - 1, with_pole, to_pole, from_pole)
#
#
# def move_disk(fp, tp):
#     print("moving disk from", fp, "to", tp)
#
#
# move_tower(6, "A", "B", "C")
#
#
# def search_from(maze, start_row, start_column):
#     maze.update_position(start_row, start_column)
#
#     # Check for base cases:
#
#     # 1. We have run into an obstacle, return false
#
#     if maze[start_row][start_column] == OBSTACLE:
#         return False
#
#     # 2. We have found a square that has already been explored
#
#     if maze[start_row][start_column] == TRIED:
#         return False
#
#         # 3. Success, an outside edge not occupied by an obstacle
#
#     if maze.is_exit(start_row, start_column):
#
#         maze.update_position(start_row, start_column, PART_OF_PATH)
#
#         return True
#
#         maze.update_position(start_row, start_column, TRIED)
#
#         # Otherwise, use logical short circuiting to try each direction in turn (if needed)
#
#     found = search_from(maze, start_row - 1, start_column) or \
#  \
#             search_from(maze, start_row + 1, start_column) or \
#  \
#             search_from(maze, start_row, start_column - 1) or \
#  \
#             search_from(maze, start_row, start_column + 1)
#
#     if found:
#
#         maze.update_position(start_row, start_column, PART_OF_PATH)
#
#     else:
#
#         maze.update_position(start_row, start_column, DEAD_END)
#
#     return found
#
# PART_OF_PATH = 'O'
#
# TRIED = '.'
#
# OBSTACLE = '+'
#
# DEAD_END = '-'
#
#
#
# class Maze:
#
#         def __init__(self, maze_file_name):
#
#                 rows_in_maze = 0
#
#                 columns_in_maze = 0
#
#                 self.maze_list = []
#
#
#
#                 with open(maze_file_name,'r') as maze_file:
#                     for line in maze_file:
#
#                         row_list = []
#
#                         col = 0
#
#                         for ch in line[: -1]:
#
#                             row_list.append(ch)
#
#                             if ch == 'S':
#
#                                 self.start_row = rows_in_maze
#
#                             self.start_col = col
#
#                         col = col + 1
#
#                         rows_in_maze = rows_in_maze + 1
#
#                         self.maze_list.append(row_list)
#
#                         columns_in_maze = len(row_list)
#
#                 self.rows_in_maze = rows_in_maze
#
#                 self.columns_in_maze = columns_in_maze
#
#                 self.x_translate = - columns_in_maze / 2
#
#                 self.y_translate = rows_in_maze / 2
#
#                 self.t = turtle.Turtle()
#
#                 self.t.shape('turtle')
#
#                 self.wn = turtle.Screen()
#
#                 self.wn.setworldcoordinates(- (columns_in_maze - 1) / 2 - .5, - (rows_in_maze - 1) / 2 - .5, \
#  \
#                                     (columns_in_maze - 1) / 2 + .5, (rows_in_maze - 1) / 2 + .5)
#
#         def draw_maze(self):
#
#             self.t.speed(10)
#
#             for y in range(self.rows_in_maze):
#
#                 for x in range(self.columns_in_maze):
#
#                     if self.maze_list[y][x] == OBSTACLE:
#                         self.draw_centered_box(x + self.x_translate, - y + self.y_translate, 'orange')
#
#                         self.t.color('black')
#
#                         self.t.fillcolor('blue')
#
#         def draw_centered_box(self, x, y, color):
#
#             self.t.up()
#
#             self.t.goto(x - .5, y - .5)
#
#             self.t.color('black', color)
#
#             self.t.setheading(90)
#
#             self.t.down()
#
#             self.t.begin_fill()
#
#             for i in range(4):
#                 self.t.forward(1)
#
#                 self.t.right(90)
#
#             self.t.end_fill()
#
#         def move_turtle(self, x, y):
#
#             self.t.up()
#
#             self.t.setheading(self.t.towards(x + self.x_translate, - y + self.y_translate))
#
#             self.t.goto(x + self.x_translate, - y + self.y_translate)
#
#         def drop_bread_crumb(self, color):
#             self.t.dot(10, color)
#
#         def update_position(self, row, col, val=None):
#
#             if val:
#                 self.maze_list[row][col] = val
#
#             self.move_turtle(col, row)
#
#             if val == PART_OF_PATH:
#
#                 color = 'green'
#
#             elif val == OBSTACLE:
#
#                 color = 'red'
#
#             elif val == TRIED:
#
#                 color = 'black'
#
#             elif val == DEAD_END:
#
#                 color = 'red'
#
#             else:
#
#                 color = None
#
#             if color:
#                 self.drop_bread_crumb(color)
#
#         def is_exit(self, row, col):
#
#             return (row == 0 or row == self.rows_in_maze - 1 or col == 0 or col == self.columns_in_maze - 1)
#
#         def __getitem__(self, idx):
#
#             return self.maze_list[idx]
#
#
# my_maze = Maze('maze2.txt')
#
# my_maze.draw_maze()
#
# my_maze.update_position(my_maze.start_row, my_maze.start_col)
#
#
#
# search_from(my_maze, my_maze.start_row, my_maze.start_col)

def ordered_sequential_search(a_list, item):
    pos = 0

    found = False

    stop = False

    while pos < len(a_list) and not found \
 \
            and not stop:

        if a_list[pos] == item:

            found = True

        else:
            if a_list[pos] > item:
                 stop = True
            else:
                                pos = pos+1
        return found


def binary_search(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search(a_list[:midpoint], item)
            else:
                return binary_search(a_list[midpoint + 1:], item)

# hash table is a collection of items stored in a way easy to ind them later
# each slot of hash table can hold one item
#

