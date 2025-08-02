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

    loan = (loan * (1 + interest/1200) - mpay);
    printf("\nBalance remaining after first payment: $%.2f\n", loan);

    loan = (loan * (1 + interest/1200) - mpay);
    printf("Balance remaining after second payment: $%.2f\n", loan);

    loan = (loan * (1 + interest/1200) - mpay);
    printf("Balance remaining after third payment: $%.2f\n", loan);

    return 0;
}