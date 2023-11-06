#include <stdio.h>
#include <limits.h>
#include <float.h>



#define print_with_size(number) printf("%ld %ld\n", sizeof(number), number)
#define print_with_size_float(number) printf("%ld %f\n", sizeof(number), number)

int main() {
    int integer_max = INT_MAX;
    unsigned short int ushort_max = USHRT_MAX;
    signed long int long_max = LONG_MAX;
    float float_max = FLT_MAX;
    double double_max = DBL_MAX;

    print_with_size(integer_max);
    print_with_size(ushort_max);
    print_with_size(long_max);
    print_with_size_float(float_max);
    print_with_size_float(double_max);

    return 0;
}