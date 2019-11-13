//
//  main.cpp
//  randGenerator
//
//  Created by Pradeesh Parameswaran on 12/11/19.
//  Copyright © 2019 Pradeesh Parameswaran. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fstream>

using namespace std;

long seedValue;
int prob;
double number;
double generateNoOfTrials = 0;
ofstream myfile;
string filename;
int inputSize = 0; // how big we want our random generator to be
int noOfLoops = 0; // how many number of loops that we need to do
void initRandomGenerator() {
    seedValue = time(0);
    srand(seedValue);
    
}

// a delay function just delays for the random number generator
void delay(int number_of_seconds)
{
    // Converting time into milli_seconds
    int milli_seconds = 1000 * number_of_seconds;
    
    // Stroing start time
    clock_t start_time = clock();
    
    // looping till required time is not acheived
    while (clock() < start_time + milli_seconds)
    ;
}


int main(int argc, const char * argv[]) {
// initRandomGenerator();
//double number=(double)rand()/((double)RAND_MAX+1);
    
    if (argc > 2) {
        inputSize = atoi(argv[1]);
        noOfLoops = atoi(argv[2]);
        cout << inputSize << endl;
        cout << noOfLoops << endl;
    }
    
    for (int i = 0; i < noOfLoops; ++i) {
        initRandomGenerator();
        filename = (to_string(seedValue) + ".txt");
        cout << filename << endl;
        myfile.open(filename);
        for (int j=0; j<inputSize;j++) {
            number=(double)rand()/((double)RAND_MAX+1);
            if (number >0.5) {
                prob = 1;
            }
            else {
                prob = 0;
            }
          // cout << prob << endl;
            myfile << prob;
        }
        myfile.close();
        delay(1000);

    }
    //cout << number << endl;
    
    //cout << (getSeedValue(timer)) << endl; // get the current time that is avaliable
   // cout << "Hello, World!\n" << endl;
    return 0;
}
