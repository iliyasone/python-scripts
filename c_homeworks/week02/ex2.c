#include <stdio.h>

#define MAX_STRING_LENGTH 256

int main() {

    char string[MAX_STRING_LENGTH];
    int dot = -1;
    
    fgets(string, sizeof(string), stdin);


    for (int i = 0; i < MAX_STRING_LENGTH; i++) {
        if (string[i] == '.') {
            dot = i-1;
        }
    }


    if (dot == -1) {
        dot = strlen(string) - 2;
    }


    putchar('"');
    for (int i = dot; i >= 0; i--) {
        putchar(string[i]);
    }
    putchar('"');
    putchar('\n');


    return 0;
}