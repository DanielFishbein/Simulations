import random
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from Functions import pick_point
from Functions import check_near
from Functions import check_overlap
from Functions import check_corner
from Functions import check_edge
from Functions import take_step


matrix_size = 20


x = 0
y = 1
#Creating the initial matrix and conditions
Growth_Matrix = []
for i in range(matrix_size+1):
    dumb = []
    for j in range(matrix_size+1):
        dumb.append(0)
    Growth_Matrix.append(dumb)

seed = int(matrix_size/2)
Growth_Matrix[seed][seed] = 1


#Global variables that must be used to tell if the program is working on a new point or the same point
is_new_point = True
old_point = [0,0]

#The function that is called for animating
def update(frame):

    #Global variables that must be used to tell if the program is working on a new point or the same point
    global is_new_point
    global old_point

    #Checks the state of the global boolean
    #and either picks a new point or continues with the old point 
    if is_new_point == True:
        point = pick_point(matrix_size)
        old_point = point
    if is_new_point == False:
        point = old_point

    #Checks if the picked point is overlapping another point
    is_overlap = check_overlap(point[x], point[y], Growth_Matrix)
    
    #Marks the point being looked at on the matrix
    Growth_Matrix[point[x]][point[y]] = 1
    
    #if there is overlap the state of the matrix is saved and the function ends
    if is_overlap == True:
        is_new_point = True
        return

    #changing the state of the global variable 
    is_new_point = False

    #Calling a function to check if the point in question is in a corner
    is_corner = check_corner(point[x],point[y], matrix_size)
    if is_corner[0] == True:

        #if true than the pont in question is reset to 0
        Growth_Matrix[point[x]][point[y]] = 0
        
        #gathering and renameing the new point determined
        old_point[x], old_point[y] = is_corner[1][x], is_corner[1][y]
        
        #saving the state of the matrix
        matrice.set_array(Growth_Matrix)

        
        return

    #Calling a function to check if the point in question is in a edge
    is_edge = check_edge(point[x],point[y], matrix_size)
    if is_edge[0] == True:

        #if true than the pont in question is reset to 0
        Growth_Matrix[point[x]][point[y]] = 0

        #gathering and renameing the new point determined
        old_point[x], old_point[y] = is_edge[1][x], is_edge[1][y]

        #saving the state of the matrix
        matrice.set_array(Growth_Matrix)

        
        return

    #Calling a function to check if the point in question is adjacent to another point
    is_near = check_near(point[x], point[y], Growth_Matrix)
    if is_near ==True:

        #resetting the global variable 
        is_new_point = True

        #saving the state of the matrix
        matrice.set_array(Growth_Matrix)
        return

    #Calling a function to take a step in a random direction
    old_point = take_step(point[x],point[y])
    
    #saving the state of the matrix
    matrice.set_array(Growth_Matrix)

    #setting the old point to 0
    Growth_Matrix[point[x]][point[y]] = 0
    return
    
#creating figure for plots
fig, ax = plt.subplots()
matrice = ax.matshow(Growth_Matrix)
plt.colorbar(matrice)

#function that animates the program by repeataly calling "update"
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)
plt.show()