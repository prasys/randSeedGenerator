//
//  methods.cpp
//  randGenerator
//
//  Created by Pradeesh Parameswaran on 12/11/19.
//  Copyright © 2019 Pradeesh Parameswaran. All rights reserved.
//

#include "methods.hpp"
//#include <time.h>
//time_t timer;

struct {
    
   time_t getSeedValue(time_t &timerValue) {
        return time(&timerValue);
    }
