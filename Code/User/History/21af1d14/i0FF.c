#include <stdio.h>

#define FREEZING_PT 32.0f
#define SCALE_FACTOR (5.0f / 9.0f)

int main(void)
{
    float ftemp, ctemp;

    printf("Enter the temperature in Fahrenheit: ");
    scanf("%f", &ftemp);        //Pressing "Enter" 

    ctemp = (ftemp - FREEZING_PT) * SCALE_FACTOR;       //Math for the conversion

    printf("Celsius equivalent: %.2f\n", ctemp);        //Please use %f for float values, not %d (Otherwise some anomalous behaviour may occur)

    return 0;
}