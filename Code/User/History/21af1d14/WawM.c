#include <stdio.h>
#define FREEZING_PT 32.0f
#define SCALE_FACTOR (5.0f / 9.0f)

int main(void)
{
    int ftemp, ctemp;

    printf("Enter the temperature in Fahrenheit: ");
    scanf("%d", &ftemp);

    ctemp = (ftemp - FREEZING_PT) * SCALE_FACTOR;

    print("Celsius equivalent: %d\n", ctemp);

    return 0;
}