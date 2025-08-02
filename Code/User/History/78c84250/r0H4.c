#include <stdio.h>

int main(void)
{
    int amount, n20, n10, n5, n1;

    printf("Enter a dollar amount: ");
    scanf("%d", &amount);

    n20 = amount / 20;
    amount -= n20 * 20;

    n10 = amount / 10;
    amount -= n10 * 10;

    n5 = amount / 5;
    amount -= n5 * 5;

    n1 = amount / 1;
    amount -= n1;

    printf
}