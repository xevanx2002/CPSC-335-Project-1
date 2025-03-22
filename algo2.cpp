// Ekaterina Miakotina and Evan Wenzel

#include <iostream>
#include <vector>

void greedyHamAlg(std::vector<int>& cityDis, std::vector<int>& totFuel, int mpg) {
    int currentGas = 0;
    int startingCity = 0;
    
    // Loop through the vector of cities to determine the best starting city within the circle
    for (int i = 0; i < cityDis.size(); i++) {
        // Calculate the current available gas on the trip to determine trip viability
        currentGas = currentGas + (totFuel[i] * mpg) - cityDis[i];

        // Checks the available gas after calculating travel for a negative number to see if the trip is possible
        // Resets the trip while iterating through the possible starting cities
        if (currentGas < 0 && i != (cityDis.size() - 1)) {
            // Reset the trip but starting from the next city instead
            startingCity = i + 1;
            currentGas = 0;
        };
    };

    std::cout << "The best starting city index is " << startingCity << std::endl;
}

int main() {
    int cityNum, mpg;
    bool exit = false;
    char choice;
    
    // Loop that iterates through the enitre program as long as the user want to
    while(exit != true) {
        std::cout << "Welcome to the Greedy Approach to Hamiltonian Problem Algorithm!" << std::endl;

        // Askes the user for the desired number of cities to calulate through
        std::cout << "Please enter the number of cities you wish to travel!" << std::endl;
        std::cin >> cityNum;
        // Asks the user for the miles per gallon the vehicle uses
        std::cout << "Please enter the miles per gallon for the vehicle!" << std::endl;
        std::cin >> mpg;

        // CityDis is the distances between each city within an array while totFuel is the fuel available in each city
        std::vector<int> cityDis(cityNum);
        std::vector<int> totFuel(cityNum);

        std::cout << "Please enter the following distances between cities and the fuel fuel available at each city!" << std::endl;
        for (int i = 0; i < cityNum; i++) {
            // Each iteration is for the distance between the starting city and the next
            std::cout << "City Distance " << i << ": ";
            std::cin >> cityDis[i];
            std::cout << std::endl;
            // Each iteration is for the total fuel available in each city 
            std::cout << "Fuel Available for City " << i << ": ";
            std::cin >> totFuel[i];
            std::cout << std::endl;
        };

        // Run the algorithm with the inputed information provided
        greedyHamAlg(cityDis, totFuel, mpg);
        // Ask the user if they want to run the algorithm again with different inputs
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