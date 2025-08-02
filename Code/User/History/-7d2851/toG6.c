#include <stdio.h>

int main(void)
{
    int x;

    printf("Enter the value for x: ");
    scanf("%d", &x);

    printf("The value of 3x^5 + 2x^4 - 5x^3 - x^2 + 7x - 6 is: %d\n", ((((3*x+2)*x+5)*x-1)*x+7)*x+6 );

    return 0;
}