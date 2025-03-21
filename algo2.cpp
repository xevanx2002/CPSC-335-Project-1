#include <iostream>
#include <vector>

void greedyHamAlg(std::vector<int>& cityDis, std::vector<int>& totFuel, int mpg) {
    int currentGas = 0;
    int startingCity = 0;
    
    for (int i = 0; i < cityDis.size(); i++) {
        
        // Calculate the current available gas on the trip to determine trip viability
        currentGas = currentGas + (totFuel[i] * mpg) - cityDis[i];

        if (currentGas < 0 || i != (cityDis.size() - 1)) {
            // Reset the trip but starting from the next city instead
            startingCity = i + 1;
            currentGas = 0;
        };
    };

    // If the total gas is below zero after calcs, there is no valid starting city 
    if (currentGas >= 0) {
        std::cout << "The preferred starting city for the sample provided is city " << startingCity << std::endl;
    }
    else {
        std::cout << "No valid starting city was found" << std::endl;
    }
}

int main() {
    int cityNum, mpg;
    bool exit = false;
    char choice;
    
    while(exit != true) {
        std::cout << "Welcome to the Greedy Approach to Hamiltonian Problem Algorithm!" << std::endl;
        std::cout << "Please enter the number of cities you wish to travel!" << std::endl;
        std::cin >> cityNum;

        std::cout << "Please enter the miles per gallon for the vehicle!" << std::endl;
        std::cin >> mpg;

        std::vector<int> cityDis(cityNum);
        std::vector<int> totFuel(cityNum);

        std::cout << "Please enter the following distances between cities and the fuel fuel available at each city!" << std::endl;
        for (int i = 0; i < cityNum; i++) {
            std::cout << "City Distance " << (i + 1) << ": ";
            std::cin >> cityDis[i];
            std::cout << std::endl;
            
            std::cout << "Fuel Available for City " << (i + 1) << ": ";
            std::cin >> totFuel[i];
            std::cout << std::endl;
        };

        greedyHamAlg(cityDis, totFuel, mpg);
        std::cout << "Would you like to go again? Y | N" << std::endl;
        std::cin >> choice;

        if (choice == 'Y' || choice == 'y') {
            exit = false;
        }
        else {
            exit = true;
        };
    };

    return 0;
}