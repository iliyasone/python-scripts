#include <stdio.h>

#define MAX_STR_LEN 256

#define SWAP(a, b) { a = a + b; b = a - b; a = a - b; }

int tribonacci(int n) {
    int before_before_previous = 0;
    int before_previous = 1;
    int previous = 1;
    
    if (n == 0 || n == 1) {
        return n;
    } else if (n == 2) {
        return 1;
    }

    for (int i = 3; i <= n; i ++) {
        int new = previous + before_previous + before_before_previous;

        before_before_previous = before_previous;
        before_previous = previous;
        previous = new;
    }

    return previous;

}


int main() {
    printf("%d\n", tribonacci(4));
    printf("%d\n", tribonacci(36));
    return 0;
}