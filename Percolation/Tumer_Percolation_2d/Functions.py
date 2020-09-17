import random

#picks a point from inside the matrix
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

#checks if the point given is already set to 1
def check_overlap(x,y, Matrix):
    if Matrix[x][y] == 1:
        return True