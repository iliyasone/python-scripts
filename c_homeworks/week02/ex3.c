#include <stdio.h>

#define MAX_STR_LEN 256


int convert(int x, int s, int t) {
    char result[MAX_STR_LEN];

    int true_value = 0;
    int place_value = 1;
    while (x > 0) {
        int last_digit = x % 10;

        if (last_digit >= s) {
            return -1;
        }

        true_value += last_digit * place_value;
        place_value *= s;

        x = x / 10; // remove last digit
    }

    int len_result = 0;

    while (true_value > 0) {
        int last_digit = true_value % t;
        true_value /= t;
        result[len_result] = '0' + last_digit;
        len_result++;
    }

    for (int i = 0; i < len_result / 2; i++ ) {
        char tmp = result[i];
        result[i] = result[len_result-i-1];
        result[len_result-i-1] = tmp;
    }


    result[len_result] = '\0';


    int result_n;
    sscanf(result, "%d", &result_n);
    return result_n;
}

int main() {
    int x, s, t;
    scanf("%d", &x);
    scanf("%d", &s);
    scanf("%d", &t);

    int result = convert(x, s, t);
    if (result == -1 || s > 10 || t > 10 || s < 2 || t < 2) {
        printf("cannot convert!");
    }
    else {
        printf("%d", result);
    }
    
    return 0;
}