#include <stdio.h>

int main(void)
{
    int length, width, height;

    printf("Enter the length of the box: ");
    scanf("%d", &length);

    printf("Enter the width of the box: ");
    scanf("%d", &width);

    printf("")

    int volume = height * length * width;
    int dweight = (volume + 165) / 166;

    printf("Dimensions: %d x %d x %d\n", length, width, height);
    printf("Volume (cubic inches): %d\n", volume);
    printf("Dimensional Weight (pounds): %d\n", dweight);

    return 0;
}