#include <stdio.h>

#define FREEZING_PT 32.0
#define SCALE_FACTOR (5.0 / 9.0)

int main(void)
{
    float ftemp, ctemp;

    printf("Enter the temperature in Fahrenheit: ");
    scanf("%f", &ftemp);

    ctemp = (ftemp - FREEZING_PT) * SCALE_FACTOR;

    printf("Celsius equivalent: %f\n", ctemp);

    return 0;
}