#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_STR_LEN 256


int count(char string[MAX_STR_LEN], char c) {
    int result = 0;
    c = tolower(c);
    for (int i = 0; i < strlen(string); i++) {
        if (tolower(string[i]) == c) {
            result += 1;
        }
    }
    return result;
}

void countAll(char string[MAX_STR_LEN]) {
    for (int i = 0; i < strlen(string) - 1; i++) {
        printf("%c:%d", string[i], count(string, string[i]));

        if (i != strlen(string) - 2) {
            printf(", ");
        } else {
            putchar('\n');
        }
    }
}


int main() {

    char string[MAX_STR_LEN];
    
    fgets(string, sizeof(string), stdin);
    countAll(string);

    return 0;
}