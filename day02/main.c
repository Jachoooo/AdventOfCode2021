#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "input.txt"

//Advent of code 2021
//Day 02 
int main(int argc, char* argv[])
{
    printf("Advent of Code 2021\n\nDay 02\n");
    printf("+----------------------------+\n");
    FILE* file = fopen(FILENAME, "r"); /* should check the result */
    char line[256];
    int dep = 0;
    int hor = 0;

    while (fgets(line, sizeof(line), file)) {
        if( !strncmp(line,"up",2)){
            dep-=line[3]-48;
        }
        if( !strncmp(line,"do",2)){
            dep+=line[5]-48;
        }
        if( !strncmp(line,"fo",2)){
            hor+=line[8]-48;
        }
    }
    fclose(file);
    printf("\r|                            |\r");   
    printf("| Part1 = %d\n",hor*dep);
    
    //Part 2
    dep = 0;
    hor = 0;
    int aim = 0;
    file = fopen(FILENAME, "r"); /* should check the result */

    while (fgets(line, sizeof(line), file)) {
        if( !strncmp(line,"up",2)){
            aim-=line[3]-48;    
        }
        if( !strncmp(line,"do",2)){
            aim+=line[5]-48;
        }
        if( !strncmp(line,"fo",2)){
            hor+=line[8]-48;
            dep+=(line[8]-48)*aim;
        }
    }
    fclose(file);  
    printf("\r|                            |\r"); 
    printf("| Part2 = %d\n",hor*dep);
    printf("+----------------------------+\n\n");

    return 0;
}