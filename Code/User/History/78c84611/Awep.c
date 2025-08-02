#include <stdio.h>

int main(void)
{
    float loan, interest, mpay;

    printf("Enter the amount of loan: ");
    scanf("%f", &loan);

    printf("Enter the interest rate: ");
    scanf("%f", &interest);

    printf("Enter the monthly payment: ");
    scanf("%f", &mpay);

    printf("Balance remaining after first payment: %f", (loan - mpay) * (1 + interest/12));

    return 0;
}