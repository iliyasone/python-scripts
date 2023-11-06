#include <stdio.h>
#include <stdarg.h>

void* aggregate(void* base, size_t size, int n, void* initial_value, void* (*opr)(const void*, const void*)) {
    char *pos = (char*) base; //make base position 1 byte
    for (int i = 0; i < n; i++) {
        void* next = pos + i*size;
    initial_value = opr(initial_value, next); 
    }
}