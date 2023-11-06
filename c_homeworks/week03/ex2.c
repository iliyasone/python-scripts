#include <math.h>
#include <stdio.h>

#define square(x) (x)*(x)

struct Point
{
    double x;
    double y;
};

double distance(struct Point p1, struct Point p2) {
    return sqrt(square(p1.x-p2.x) + square(p1.y-p2.y));
};


double area(struct Point p1, struct Point p2, struct Point p3) {
    return 0.5 * fabs(p1.x*p2.y - p2.x*p1.y + p2.x*p3.y - p3.x*p2.y + p3.x*p1.y - p1.x*p3.y);
}

int main() {
    struct Point A = {25.0, 6.0};
    struct Point B = {1.0, 2.2};
    struct Point C = {10.0, 6.0};

    printf("A - B: %lf", distance(A, B));
    printf("area: %lf", area(A, B, C));
}