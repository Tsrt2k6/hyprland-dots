#include <stdio.h>

int main(void)
{
    int height = 8;
    int length = 12;
    int width = 10;
    int volume = height * length * width;
    int dweight = (volume + 165) / 166;

    printf("Dimensions: %d x %d x %d\n", length, width, height);
    printf("Volume (cubic inches): %d\n", volume);
    printf("Dimensional Weight (pounds): %d\n", dweight);

    return 0;
}