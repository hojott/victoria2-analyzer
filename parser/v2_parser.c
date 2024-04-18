#include <stdio.h>

int BUFFER_SIZE = 100;

FILE *open_savefile(const char *filename)
{
    FILE *file = fopen(filename, "r, ccs=ISO-8859-1");
    if (file == NULL)
    {
        perror("Couldn't open file!");
        return NULL;
    }

    return file;
}

FILE *open_newfile(const char *filename)
{
    FILE *file = fopen(filename, "w");

    return file;
}

void close_file(FILE *file)
{
    fclose(file);
}

/*typedef char (*ReadlinePtr)();
ReadlinePtr generate_readline(const FILE *file)
{
    char readline()
    {
        char buffer[BUFFER_SIZE];
        return fgets(buffer, sizeof(buffer), file);
    };

    return readline;
}

typedef void (*WritelinePtr)(char);
WritelinePtr generate_writeline(const FILE *file)
{
    void writeline(char *towrite)
    {
        fprintf(file, towrite);
    }

    return readline;
}*/

int parse_file(FILE *savefile, FILE *newfile)
{
    char buffer[BUFFER_SIZE];

    while (fgets(buffer, BUFFER_SIZE, savefile) != NULL)
    {
        printf("%s", buffer);
    }
}

int parse(const char *savefilename, const char *newfilename)
{
    FILE *savefile = open_savefile(savefilename);
    FILE *newfile = open_newfile(newfilename);

    parse_file(savefile, newfile);

    close_file(savefile);
    close_file(newfile);
}

int main()
{
    parse("China1934_09_25.v2", "China1934_09_25.json");
    return 0;
}
