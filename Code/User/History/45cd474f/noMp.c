#include <stdio.h>
#define INCHES_PER_POUND 166        //Macro definition of constant

int main(void)
{
    int length, width, height, volume, dweight;

    printf("Enter the length of the box: ");
    scanf("%d", &length);       //Using a pointer to store the value of integer into the variable "length"

    printf("Enter the width of the box: ");
    scanf("%d", &width);

    printf("Enter the height of the box: ");
    scanf("%d", &height);

    volume = height * length * width;
    dweight = (volume + INCHES_PER_POUND - 1) / INCHES_PER_POUND;       //Math trick to make "dweight" always be rounded up

    printf("Dimensions: %d x %d x %d\n", length, width, height);
    printf("Volume (cubic inches): %d\n", volume);
    printf("Dimensional Weight (pounds): %d\n", dweight);

    return 0;
}