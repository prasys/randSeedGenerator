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
#include <unistd.h>

using namespace std;

unsigned long seedValue;
int prob;
double number;
double generateNoOfTrials = 0;
ofstream myfile;
string filename;
int inputSize = 0; // how big we want our random generator to be
int noOfLoops = 0; // how many number of loops that we need to do


/*
 --------------------------------------------------------------------
 mix -- mix 3 32-bit values reversibly.
 Code taken from http://www.concentric.net/~Ttwang/tech/inthash.htm
 For every delta with one or two bits set, and the deltas of all three
 high bits or all three low bits, whether the original value of a,b,c
 is almost all zero or is uniformly distributed,
 * If mix() is run forward or backward, at least 32 bits in a,b,c
 have at least 1/4 probability of changing.
 * If mix() is run forward, every bit of c will change between 1/3 and
 2/3 of the time.  (Well, 22/100 and 78/100 for some 2-bit deltas.)
 mix() was built out of 36 single-cycle latency instructions in a
 structure that could supported 2x parallelism, like so:
 a -= b;
 a -= c; x = (c>>13);
 b -= c; a ^= x;
 b -= a; x = (a<<8);
 c -= a; b ^= x;
 c -= b; x = (b>>13);
 ...
 Unfortunately, superscalar Pentiums and Sparcs can't take advantage
 of that parallelism.  They've also turned some of those single-cycle
 latency instructions into multi-cycle latency instructions.  Still,
 this is the fastest good hash I could find.  There were about 2^^68
 to choose from.  I only looked at a billion or so.
 --------------------------------------------------------------------
 */

unsigned long mix(unsigned long a, unsigned long b, unsigned long c)
{
    a=a-b;  a=a-c;  a=a^(c >> 13);
    b=b-c;  b=b-a;  b=b^(a << 8);
    c=c-a;  c=c-b;  c=c^(b >> 13);
    a=a-b;  a=a-c;  a=a^(c >> 12);
    b=b-c;  b=b-a;  b=b^(a << 16);
    c=c-a;  c=c-b;  c=c^(b >> 5);
    a=a-b;  a=a-c;  a=a^(c >> 3);
    b=b-c;  b=b-a;  b=b^(a << 10);
    c=c-a;  c=c-b;  c=c^(b >> 15);
    return c;
}

void initRandomGenerator() {
    //seedValue = time(0);
    seedValue = mix(clock(),getpid(),time(0));
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
    //initRandomGenerator();
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
            myfile << prob << endl;
        }
        myfile.close();
       // delay(1000);

    }
    //cout << number << endl;
    
    //cout << (getSeedValue(timer)) << endl; // get the current time that is avaliable
   // cout << "Hello, World!\n" << endl;
    return 0;
}
