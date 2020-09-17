import random

#Function that picks a cordinate inside the given parameters
def pick_point(matrix_size):
    A = random.randint(1,matrix_size-1)
    B = random.randint(1,matrix_size-1)
    return [A,B]

#Function that checks lateraly and horizonaly if there is a point that is near by
def check_near(x, y, Matrix):
    if Matrix[x+1][y] == 1:
        return True
    elif Matrix[x-1][y] == 1:
        return True
    elif Matrix[x][y+1] == 1:
        return True
    elif Matrix[x][y-1] == 1:
        return True
    elif Matrix[x+1][y-1] == 1:
        return True
    elif Matrix[x-1][y-1] == 1:
        return True
    elif Matrix[x-1][y+1] == 1:
        return True
    elif Matrix[x+1][y+1] == 1:
        return True
    else:
        return False

#Function that checks if the point picked is already taken 
def check_overlap(x, y, Matrix):
    if Matrix[x][y] == 1:
        return True

#Function that checks if the given cordinate is at a corner and moves that point in an appropriate direction 
def check_corner(x, y, matrix_size):
    if (x == 0 and y == 0):
        return True, [x+1, y+1]
    elif ((x == matrix_size) and (y == 0)):
        return True, [x-1, y+1]
    elif ((x == 0) and (y == matrix_size)):
        return True, [x+1, y-1]
    elif ((x == matrix_size) and (y == matrix_size)):
        return True, [x-1, y-1]   
    else:
        return False, [x,y]

#Function that checks if the given cordinate is at an edge and moves that point in an appropriate direction 
def check_edge(x, y, matrix_size):
    if x == 0:
        return True, [x+1, y]
    elif x == matrix_size:
        return True, [x-1, y]
    elif y == 0:
        return True, [x, y+1]
    elif y == matrix_size:
        return True, [x, y-1]
    else:
        return False, [x,y]

#Function that roles a randome number between 0 and 1 gives a corisponding movement 
def take_step(x, y):
    number = random.random()
    if number < 0.125:
        return [x+1,y]
    elif number < 0.25:
        return [x+1,y+1]
    elif number < 0.375:
        return [x+1,y-1]
    elif number < 0.50:
        return [x-1,y]
    elif number < 0.625:
        return [x-1,y+1]    
    elif number < 0.75:
        return [x,y+1]
    elif number < 0.875:
        return [x-1,y-1]
    elif number <= 1:
        return [x,y-1]
