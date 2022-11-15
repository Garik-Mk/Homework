#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    pid_t pid = fork();
    if(pid==0) {
        int sum = 0;
        for(int i = 0; i < argc; ++i){
            sum += atoi(argv[i]);
        }
        sum /= argc - 1;
        printf("Average: %d\n", sum);
        exit(0);
    }
    else {
        wait(&pid);
    }
    return 0;
}