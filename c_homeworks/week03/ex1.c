#include <stdio.h>

int const_tri(int *p, int n) {
    if (n == 0 || n == 1) {
        return n;
    } else if (n == 2) {
        return 1;
    }
    p[0] = 1;
    p[1] = 1;
    p[2] = 2;
    int temp;

    n -= 3;
    while (n > 0) {
        temp = p[0] + p[1] + p[2];
        p[0] = p[1];
        p[1] = p[2];
        p[2] = temp;
        n--;
    }
    

    return p[2];

}


int main() {
    const int x = 1;
    int *q = &x;
    int *p = malloc(sizeof(int)*3);
    
    *p = x;
    p[1] = x;   // equivalent to *(p+1) = x
    *(p+2) = 2*x;

    printf("%p %p %p\n", p, p+1, p+2);

    if (((long)(p+1) - (long)(p)) == sizeof(int) && ((long)(p+2) - (long)(p+1)) == sizeof(int)) {
        printf("Cells are contiguous\n");
    } else {
        printf("cells are NOT contiguous (weird)\n");
    }

    printf("%d", const_tri(p, 36)); // 1132436852

    free(p);
    return 0;
}