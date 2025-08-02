#include <stdio.h>

int main(void)
{
    float radius, volume;

    printf("What is the radius of the sphere?: ");
    scanf("%f", &radius);

    volume = (4.0f / 3.0f) * 3.14f * radius * radius * radius;

    printf("The volume of the sphere is: %.2f\n", volume);

    return 0;
}