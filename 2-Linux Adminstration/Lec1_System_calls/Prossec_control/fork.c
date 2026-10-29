#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t pid;
    // Create a new process using fork
    pid = fork();
    if (pid < 0) {
        // Error occurred
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
    // Child process
    printf("Hello from the Child process! (PID: %d)\n", getpid());
    // Simulate some work in the child process
    sleep(10);
    printf("Child process (PID: %d) exiting\n", getpid());
    exit(EXIT_SUCCESS);
    } else {
        // Parent process
        printf("Hello from the Parent process! (PID: %d), Child process (PID: %d)\n", getpid(), pid);
        // wait for the null process to complete
        // wait(NULL);
    }
    while(1);
    return 0;
}