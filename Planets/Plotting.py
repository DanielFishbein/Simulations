import matplotlib.pyplot as plt
import os
import sys



#Daniel Fishbein


#This file plots the data produced in Main.cpp 


print ("Sarting plotting")


#initializing lists
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



#defining variables
planet_count = -1  
total_steps = 1

#opening data file
this_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(this_folder, 'Data.txt')
with  open(data_file, "r") as df:


    print("Data File succesfuly opened with python")
    print("Extracting data")

    

    #stepping through each line of the data file
    for cnt, new_line in enumerate(df):
            
        #striping exess spaces and end of line charictors
        line = new_line.strip()

        #checking if its the first line or 2
        if cnt == (0 or 1):
            #getting variable for how many steps will be in this simulation
            total_steps = float(line)*5
            continue
        
        #print statement to see program progress
        if (cnt % 8760) == 0:                                                        
            progress = (cnt/total_steps)*100
            print(progress,"%")

        #checking for end of data section
        if line == "Next":
            planet_count = 0
            continue

        #redefining variables
        cordinate_count = 0
        base = ""
        exponent = ""
        number = ""
        e = False

        #stepping though each charictor in the line
        for char in line:
            
            #searching for exponents
            if char == "e":
                #if found base is set to number
                #number is reset
                #e is set to true
                base = number
                number = ""
                e = True
                continue
            
            #searching for end of cordnate
            if char == ",":
                #exponent is number
                exponent = number    
                
                #if no exponent was found 
                #base is set to number
                #and exponent is set to 0
                if e==False:
                    base = number
                    exponent = 0

                #converting base and exponent to floats
                base = float(base)
                exponent = float(exponent)

                #cordinate =base*10^exponent
                cordinate = base*(10**exponent)
                
                #adding the dorinate to the desired planet position list
                
                planet_plot_mat[planet_count][cordinate_count].append(cordinate)

                #redefinng variables
                base = ""
                exponent = ""
                number = ""
                e = False
                
                if cnt == 20:
                    sys.exit()
                #counting the cornate position up
                cordinate_count = cordinate_count + 1
                continue
            
            #addiing the charictor to the end of number
            number = number + char

        #counting the planet up
        planet_count = planet_count + 1
        print(planet_count)








#data_file.close()
print("Data File succesfuly closed with python")

print("Plotting")

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