how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)

files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)