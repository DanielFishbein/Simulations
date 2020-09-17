#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
#include "Planet_Class.h"

using namespace std;
    

//Daniel Fishbein

//This program models a soler system of a given number of years and plots using python



int main(){




std::cout << "Data File succesfuly opened with C++" << endl;


int years = 50;                  //number of years that program will simulate (must be an intiger)
double total_steps = 8760*years;

double G = 6.67408e-11;         //gravitational constant
int t = 3600;                   //deltat (second)

int x = 0;
int y = 1;
int z = 2;
int number_of_planets = 4;

//initial conditions                                                                                        
double planet_init_acc[4][3] = {{0,0,0}, {0,0,0}, {0,0,0}, {0,0,0}};
double planet_init_vel[4][3] = {{0,30000,0}, {0,0,0}, {0,13100,10000}, {10000,13100,0}};
double planet_init_pos[4][3] = {{149600000000,0,0}, {0,0,0}, {778600000000,0,0}, {0,778600000000,0}};
double planet_mass[4] = {5.972e24, 1.989e30, 1.898e27, 2.164e27};

//Initializing vectors
vector<double> acceleration_cord;
vector<double> velocity_cord;
vector<double> position_cord;
vector<Planet> planet_vector;


std::cout << "Starting Math" << endl;


//filling the planet objects with initial conditions
for (int i=0; i < number_of_planets; i++){
    Planet new_planet;
    for(int j=0; j < 3; j++){

        //converting arrays into vectors
        acceleration_cord.push_back(planet_init_acc[i][j]);
        velocity_cord.push_back(planet_init_vel[i][j]);
        position_cord.push_back(planet_init_pos[i][j]);
    }

    //placing vecotrs in the class
    new_planet.acceleration.push_back(acceleration_cord);
    new_planet.velocity.push_back(velocity_cord);
    new_planet.position.push_back(position_cord);
    
    //clearing vectors
    acceleration_cord.clear();
    velocity_cord.clear();
    position_cord.clear();
    
    //placing mass in the class
    new_planet.mass = planet_mass[i];

    //adding the new planet object to a vector of planets
    planet_vector.push_back(new_planet); 
}

//opening data storage file
ofstream data_file;
data_file.open ("Data.txt");

//writing down some numbers in the data file that get used later
data_file << number_of_planets << endl;
data_file << total_steps << endl;

//running simulation
for(int step=1; step <= total_steps; step++){
    
    //update every "year" of simulation time
    if (step % 8760 == 0){
        float progress = (step/total_steps)*100;
        std::cout << progress << "%" << endl;
    }
    //current planet being looked at                                                        
    for(int plan_curr=0; plan_curr < number_of_planets; plan_curr++){
        
        //redefining variables that get resued 
        double post_total_accel_x = 0;
        double post_total_accel_y = 0;
        double post_total_accel_z = 0;

        //other planet being looked at
        for(int plan_other=0; plan_other < number_of_planets; plan_other++){

            //if current planet and other planet are the same move on
            if(plan_other == plan_curr){
                continue;
            }                                        
            
            //r = r2 - r1
            double r_x = planet_vector[plan_other].position[step-1][x] - planet_vector[plan_curr].position[step-1][x];
            double r_y = planet_vector[plan_other].position[step-1][y] - planet_vector[plan_curr].position[step-1][y];
            double r_z = planet_vector[plan_other].position[step-1][z] - planet_vector[plan_curr].position[step-1][z];

            //r_magnitude = (r_x^2 + r_y^2 + r_z^2)^0.5
            double r_mag = pow(pow(r_x,2) + pow(r_y,2) + pow(r_z,2), 0.5);

            //a = G*m*r/(r_magnitude^3)
            double planet_accel_x = G*planet_vector[plan_other].mass*r_x/(pow(r_mag, 3));
            double planet_accel_y = G*planet_vector[plan_other].mass*r_y/(pow(r_mag, 3));
            double planet_accel_z = G*planet_vector[plan_other].mass*r_z/(pow(r_mag, 3));

            //summing accel from all the other planets influences on the current planet
            post_total_accel_x = post_total_accel_x + planet_accel_x;
            post_total_accel_y = post_total_accel_y + planet_accel_y;
            post_total_accel_z = post_total_accel_z + planet_accel_z;

        }
        //acceleration
        acceleration_cord.push_back(post_total_accel_x);
        acceleration_cord.push_back(post_total_accel_y);
        acceleration_cord.push_back(post_total_accel_z);
        
        planet_vector[plan_curr].acceleration.push_back(acceleration_cord);

        //velocity
        //v(i) = a*t + v(i-1)
        double planet_velocity_x = post_total_accel_x*t + planet_vector[plan_curr].velocity[step-1][x];
        double planet_velocity_y = post_total_accel_y*t + planet_vector[plan_curr].velocity[step-1][y];
        double planet_velocity_z = post_total_accel_z*t + planet_vector[plan_curr].velocity[step-1][z];

        velocity_cord.push_back(planet_velocity_x);
        velocity_cord.push_back(planet_velocity_y);
        velocity_cord.push_back(planet_velocity_z);

        planet_vector[plan_curr].velocity.push_back(velocity_cord);

        //position
        //p(i) = v*t + p(i-1)
        double planet_position_x = planet_vector[plan_curr].velocity[step][x]*t + planet_vector[plan_curr].position[step-1][x];
        double planet_position_y = planet_vector[plan_curr].velocity[step][y]*t + planet_vector[plan_curr].position[step-1][y];
        double planet_position_z = planet_vector[plan_curr].velocity[step][z]*t + planet_vector[plan_curr].position[step-1][z];

        position_cord.push_back(planet_position_x);
        position_cord.push_back(planet_position_y);
        position_cord.push_back(planet_position_z);

        planet_vector[plan_curr].position.push_back(position_cord);

        //clearing vectors
        acceleration_cord.clear();
        velocity_cord.clear();
        position_cord.clear();
        
        //writing data in a file
        data_file << planet_position_x << "," << planet_position_y << "," << planet_position_z << "," << endl;
    }
    //writing data in a file
    data_file << "Next"<< endl;

}
std::cout << "Math Complete" << endl;


//closing data file
data_file.close();


std::cout << "Data File succesfuly closed with C++" << endl;


//exicuting python file for plotting
string filename = "Plotting.py";
string command = "python ";
command += filename;
system(command.c_str());


std::cout << "Complete" << endl;


return 0;
}


