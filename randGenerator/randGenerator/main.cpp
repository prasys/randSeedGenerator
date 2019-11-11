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
using namespace std;

long seedValue;
int prob;
double number;
double generateNoOfTrials = 0;

void initRandomGenerator() {
    seedValue = time(0);
    srand(seedValue);
    
}



int main(int argc, const char * argv[]) {
    initRandomGenerator();
//double number=(double)rand()/((double)RAND_MAX+1);
    cout << seedValue << endl;
    
    for (int i=0; i < 10;i++) {
        number=(double)rand()/((double)RAND_MAX+1);
        if (number > 0.5) {
            prob = 1;
        }
        else {
            prob = 0;
        }
        cout << prob << endl;
    }
    //cout << number << endl;
    
    //cout << (getSeedValue(timer)) << endl; // get the current time that is avaliable
    cout << "Hello, World!\n" << endl;
    return 0;
}
