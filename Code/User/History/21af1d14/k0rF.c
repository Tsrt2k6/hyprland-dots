#include <stdio.h>

int main(void)
{
    int ftemp, ctemp;

    printf("Enter the temperature in Fahrenheit: ");
    scanf("%d", &ftemp);

    ctemp =(ftemp - 32.0) * (5/9);

    print("Celsius equivalent: %d\n", ctemp);
}