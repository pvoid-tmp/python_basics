#include <math.h>
#include <stdio.h>

#define DELTA 1
#define STOP 30

void main()
{
	double sinus = 0.0;
	double epsilon = 0.0001;
	double angle;
	
	for (angle = 0.0; angle <= (STOP * M_PI/180 + epsilon); angle += DELTA * M_PI/180) { 
		printf("%.4f: %.4f\n", angle, sinus);
		sinus += (sqrt(1 - sinus*sinus)) * (DELTA * M_PI/180);
	}
}