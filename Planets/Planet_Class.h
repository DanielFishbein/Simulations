#include <iostream>
#include <vector>

class Planet{
    public:
    double mass;
    std::vector<std::vector<double>> acceleration;
    std::vector<std::vector<double>> velocity;
    std::vector<std::vector<double>> position;
};