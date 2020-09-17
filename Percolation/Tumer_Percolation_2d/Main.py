import random
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from Functions import pick_point
from Functions import check_near
from Functions import check_overlap

#size of matrix
matrix_size = 50

#creating the initial matrix
Growth_Matrix = []
for i in range(matrix_size+1):
    dumb = []
    for j in range(matrix_size+1):
        dumb.append(0)
    Growth_Matrix.append(dumb)

seed = int(matrix_size/2)
Growth_Matrix[seed][seed] = 1

#function that gets called to update each frame
def update(frame):
    
    #pick a new point in the matrix
    point = pick_point(matrix_size)
    
    #check if the point chosen is overlaping
    is_overlap = check_overlap(point[0], point[1], Growth_Matrix)

    #setting the point chosen to 1 
    Growth_Matrix[point[0]][point[1]] = 1

    #if overlap is true, save the state of the matrix and return
    if is_overlap == True:
        matrice.set_array(Growth_Matrix)
        return

    #check if near another point
    is_near = check_near(point[0], point[1], Growth_Matrix)

    #if overlap is true, save the state of the matrix and return
    if is_near ==True:
        matrice.set_array(Growth_Matrix)
        return
    else:
        #if not then save the state of the matrix
        matrice.set_array(Growth_Matrix)
        #set the point chosen back to 0
        Growth_Matrix[point[0]][point[1]] = 0
    
    
#creating plot
fig, ax = plt.subplots()
matrice = ax.matshow(Growth_Matrix)
plt.colorbar(matrice)

#function that animates the plot 
ani = animation.FuncAnimation(fig, update, frames=10, interval=100)
plt.show()