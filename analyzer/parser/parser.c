#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 5000

FILE *open_file(const char *filename, char *style)
{
    FILE *file = fopen(filename, style);
    if (file == NULL)
    {
        perror("ERROR parsing");
        return NULL;
    }

    return file;
}

void close_file(FILE *file)
{
    fclose(file);
}

void substring(char *buffer, char *string, int start, int length)
{
    char substr[length + 1];
    strncpy(substr, string + start, length);
    substr[length] = '\0';
}

int parse_file(FILE *savefile, FILE *newfile)
{
    char buffer[BUFFER_SIZE];

    fprintf(newfile, "{\n");

    // Comb through every line
    while (fgets(buffer, BUFFER_SIZE, savefile) != NULL)
    {
        int splitter = 0;
        // Comb through every charater
        for (int i = 0; buffer[i] != '\n'; i++)
        {
            char value[i - splitter + 1];
            char key[i + 1];
            switch (buffer[i])
            {
            // Check for brackets
            case '{':
                // parse_file(savefile, newfile);
                fprintf(newfile, "{\n");

            case '}':
                // break;
                fprintf(newfile, "},\n");

            // Check for key-value pairs
            case '=':
                strncpy(key, buffer, i);
                key[i] = '\0';

                fprintf(newfile, key);
                fprintf(newfile, ": ");

                splitter = i;

            case '\n':
                strncpy(value, buffer + splitter + 1, i - splitter + 1);
                value[i - splitter + 1] = '\0';

                char i_num[20];
                sprintf(i_num, "%d", i);
                char split_num[20];
                sprintf(split_num, "%d", splitter);

                fprintf(newfile, value);
                fprintf(newfile, ",");
                fprintf(newfile, i_num);
                fprintf(newfile, " ");
                fprintf(newfile, split_num);
                fprintf(newfile, "\n");

            default:;
            }
        };
    };

    fprintf(newfile, "},");
    return 0;
}

int parse_by_name(const char *savefilename, const char *newfilename)
{
    FILE *savefile = open_file(savefilename, "r, ccs=ISO-8859-1");
    FILE *newfile = open_file(newfilename, "w");
    printf(savefilename);
    printf(newfilename);

    parse_file(savefile, newfile);

    close_file(savefile);
    close_file(newfile);
}
