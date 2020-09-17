import numpy as np
import matplotlib.pyplot as plt

import Planet_Class

#Daniel Fishbein





years = 5              #number of years that program will simulate (must be an intiger)

G = 6.67408e-11         #gravitational constant
t = 3600                #deltat (second)

x = 0
y = 1
z = 2


#initial conditions                                                                                        
planet_init_pos = [np.array([149600000000,0,0]), np.array([0,0,0]), np.array([778600000000,0,0]),np.array([0,778600000000,0])]
planet_init_vel = [np.array([0,30000,0]), np.array([0,0,0]), np.array([0,13100,10000]),np.array([10000,13100,0])]
planet_init_acc = [np.array([0,0,0]), np.array([0,0,0]), np.array([0,0,0]),np.array([0,0,0])]


planet_mass = [5.972e24, 1.989e30, 1.898e27, 2.164e27]
planet_mat = []

#Initializing relevent variables and Matricies

for i in range(0,len(planet_mass)):
    position = [planet_init_pos[i]]
    velocity = [planet_init_vel[i]]
    acceleration = [planet_init_acc[i]]
    mass = planet_mass[i]

    planet = Planet_Class.Planet(mass, position, velocity, acceleration) 
    planet_mat.append(planet)


xplot_planet_1 = []
yplot_planet_1 = []
zplot_planet_1 = []

xplot_planet_2 = []
yplot_planet_2 = []
zplot_planet_2 = []

xplot_planet_3 = []
yplot_planet_3 = []
zplot_planet_3 = []

xplot_planet_4 = []
yplot_planet_4 = []
zplot_planet_4 = []

planet_plot_mat = [[xplot_planet_1,yplot_planet_1,zplot_planet_1],
                   [xplot_planet_2,yplot_planet_2,zplot_planet_2],
                   [xplot_planet_3,yplot_planet_3,zplot_planet_3],
                   [xplot_planet_4,yplot_planet_4,zplot_planet_4]]





num_planet = int(len(planet_mass))                                              #number of planets that will be used
total_steps = 8760*years                                                        #total steps the program will step through

for step in range(1,total_steps):                                               #for loop of steps for the program to run through
    if step % 8760 == 0:                                                        #print statement to see program progress
        progress = (step/total_steps)*100
        print(progress,"%")

    for plan_curr in range(0,num_planet):                                       #for loop for current plannet being calcualted
        post_total_accel = 0                                                    #resetting acceleration value for next planet

        for plan_other in range(0,num_planet):                                  #for loop for the plannet that is acting on the current planet
            if plan_other == plan_curr:                                         #if current planet and other planet are the same than skip
                continue

            r_vector = planet_mat[plan_other].position[step-1] - planet_mat[plan_curr].position[step-1]#r_vector = other_planet_position - current_planet_position
            r_mag = np.linalg.norm(r_vector)                                    #function to find the length of the r_vector

            planet_accel = G*planet_mat[plan_other].mass*r_vector/(r_mag*r_mag*r_mag)#a = G*m2*r_vecotor/(r_mag^3)
            post_total_accel = post_total_accel + planet_accel                  #adding the acceleration cause by other planet to the total acceleration on the current planet


        planet_mat[plan_curr].acceleration.append(post_total_accel)
        planet_mat[plan_curr].velocity.append(post_total_accel*t + planet_mat[plan_curr].velocity[step-1])#v(i) = a*t + v(i-1)
        planet_mat[plan_curr].position.append(planet_mat[plan_curr].velocity[step]*t + planet_mat[plan_curr].position[step-1])#p(i) = v*t + p(i-1)
        
        if step%500 == 0:
            #recodring plotting data
            planet_plot_mat[plan_curr][x].append(planet_mat[plan_curr].position[step][x])        #adding current planet x positon to list x positions for current planet from x value of p(i)
            planet_plot_mat[plan_curr][y].append(planet_mat[plan_curr].position[step][y])        #adding current planet y positon to list y positions for current planet from y value of p(i))
            planet_plot_mat[plan_curr][z].append(planet_mat[plan_curr].position[step][z])        #adding current planet z positon to list z positions for current planet from z value of p(i))

       

#final plotting
fig = plt.figure()                                                              #required syntax for printing an image
ax = fig.add_subplot(111, projection='3d')                                      #setting position of ghaph
ax.scatter(xplot_planet_1,yplot_planet_1,zplot_planet_1)                        #plotting path of planet 1
ax.scatter(xplot_planet_2,yplot_planet_2,zplot_planet_2)                        #plotting path of planet 2
ax.scatter(xplot_planet_3,yplot_planet_3,zplot_planet_3)                        #plotting path of planet 3
ax.scatter(xplot_planet_4,yplot_planet_4,zplot_planet_4)                        #plotting path of planet 4
plt.legend(("Planet 1" , "Planet 2", "Planet 3", "Planet 4"))                   #legend
plt.title("4 body system")                                                      #title
plt.xlabel('XLabel')                                                            #x-axis label
plt.ylabel('YLabel')                                                            #y-axis label    
plt.show()                                                                      #print graphs