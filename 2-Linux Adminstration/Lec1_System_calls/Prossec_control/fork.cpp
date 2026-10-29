#include <iostream>
#include <unistd.h>    // fork(), getpid(), getppid()
#include <sys/types.h> // pid_t
#include <cstdio>      // perror()

int main() {

    // Display the current process ID before fork()
    std::cout << "Before fork: PID = "
              << getpid() << std::endl;

    // fork(): Creates a new child process
    // Returns:
    // -1 : Fork failed
    //  0 : Executing inside the child process
    // >0 : Executing inside the parent process
    //      (returns the child's PID)
    pid_t pid = fork();

    if (pid < 0) {

        // Handle fork() failure
        perror("fork");
        return 1;

    } else if (pid == 0) {

        // Child process
        // getpid(): Returns the current process ID
        // getppid(): Returns the parent process ID
        std::cout << "Hello from Child Process!"
                  << " PID = " << getpid()
                  << " PPID = " << getppid()
                  << std::endl;

    } else {

        // Parent process
        // pid contains the newly created child's PID
        std::cout << "Hello from Parent Process!"
                  << " PID = " << getpid()
                  << " Child PID = " << pid
                  << std::endl;
    }

    return 0;
}