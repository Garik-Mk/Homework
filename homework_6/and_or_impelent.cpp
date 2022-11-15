#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include <cstring>

int main(int argc, char **argv)
{
    if (argc == 1){
        printf("%s\n", "No programs are specified.");
        return 1;
    }
    for (int i = 1; i < argc; ++i){
        pid_t pid = fork();
        if (pid < 0){
            return 2;
        }
        if (pid == 0){
            char* child_args[] = {argv[i], NULL};
            execvp(argv[i], child_args);
        }
        int status;
        wait(&status);
        if(status != 0){
            return 3;   
        }
    }
    return 0;
}