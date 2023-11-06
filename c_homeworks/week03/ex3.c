#include <string.h>
#include <stdio.h>

#define MAX_PATH 2048
#define MAX_NAME 64
#define MAX_DATA 1024
#define MAX_CONTENTS 32

typedef struct Directory Directory;

typedef struct {
    int id;
    char name[MAX_NAME];
    unsigned char size;
    char content[MAX_DATA];
    Directory * directory;
} File;

struct Directory
{
    char name[MAX_NAME];
    char path[MAX_PATH];

    unsigned char nd;
    unsigned char nf;

    File* files[MAX_CONTENTS];
    Directory * sub_dirs[MAX_CONTENTS];
};


void overwrite_to_file(File *file, const char * str) {
    if (file && str)
        strcpy(file->content, str);   
}

void append_to_file(File *file, const char * str) {
    if (file && str)
        strcat(file->content, str);
}

void printp_file(File *file) {
    if (file && file->directory)
        printf("%s/%s", file->directory->path, file->name);
} 

void add_file(File *file, Directory *dir) {
    if (file && dir) {
        dir->files[dir->nf++] = file;
        file->directory = dir;
    }
}

// Prints the name of the File file
void show_file(File *file) {
    printf("%s ", file->name);
}


void show_dir(Directory *dir) {
    printf("\nDIRECTORY\n");
    printf(" path: %s\n", dir->path);
    printf(" files:\n");
    printf(" [ ");
    for (int i = 0; i < dir->nf; i++) {
        show_file(dir->files[i]);
    }
    printf("]\n");
    printf(" directories:\n");
    printf(" { ");
    for (int i = 0; i < dir->nd; i++) {
        show_dir(dir->sub_dirs[i]);
    }
    printf("}\n");
}

// Adds the subdirectory dir1 to the directory dir2
void add_dir(Directory *dir1, Directory *dir2) {
    if (dir1 && dir2) {
        dir2->sub_dirs[dir2->nd] = dir1;
        dir2->nd++;
        char temp_path[MAX_PATH];
        if (strcmp(dir2->path, "/")) {
            strcpy(temp_path, dir2->path);
            strcat(temp_path, "/");
            strcat(temp_path, dir1->name);
            strcpy(dir1->path, temp_path);
        } else {
            strcpy(temp_path, "/");
            strcat(temp_path, dir1->name);
            strcpy(dir1->path, temp_path);
        }
    }
}

int main() {
    Directory root = {"root", "/", 0, 0};
    Directory home = {"home", "home", 0, 0};
    Directory bin = {"bin", "bin", 0, 0};

    add_dir(&home, &root);
    add_dir(&bin, &root);

    File bash = {0, "bash"};
    add_file(&bash, &bin);

    File ex3_1 = {1, "ex3_1.c", 0, "int printf(const char * format, ...);"};
    File ex3_2 = {2, "ex3_2.c", 0, "//This is a comment in C language"};

    add_file(&ex3_1, &home);
    add_file(&ex3_2, &home);

    overwrite_to_file(&bash, "Bourne Again Shell!!");
    append_to_file(&ex3_1, "int main(){printf(\"Hello World!\")}");

    // printp_file(&bash);
    // printp_file(&home);
    // printp_file(&bin);

    show_dir(&root);
}
