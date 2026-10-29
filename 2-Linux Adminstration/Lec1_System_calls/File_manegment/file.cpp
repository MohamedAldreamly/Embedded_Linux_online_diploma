#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <cstring>
#include <sys/stat.h>


int main (){

    // File name to open or create
    const char* filename = "Embedded Linux"; 

    // open(): Opens a file and returns a File Descriptor (fd)
    // O_RDWR  : Open for reading and writing
    // O_CREAT : Create the file if it does not exist
    // O_TRUNC : Clear the file content if it already exists
    // S_IRUSR : Owner has read permission
    // S_IWUSR : Owner has write permission
    int fd = open(filename, O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);

    // -1 means the open() operation failed
    if (fd == -1){
        perror("open");
        return 1; 
    }

    // write(): Writes data to the file using its File Descriptor
    // strlen() returns the number of bytes to write
    // Returns the number of bytes written, or -1 on error
    ssize_t bytes_written = write(fd, "Hello Lunix", strlen("Hello Lunix")); 

    if (bytes_written == -1){
        perror("write");
        close(fd);
        return 1;  
    }

    // lseek(): Changes the current file offset (cursor position)
    // 0        : Offset value
    // SEEK_SET : Move relative to the beginning of the file
    // Here, we return to the beginning before reading
    if (lseek(fd, 0, SEEK_SET) ==-1) {
        perror("lseek");
        close(fd);
        return 1;
    }

    // Buffer to store data read from the file
    char buffer[128];

    // read(): Reads bytes from the file into the buffer
    // sizeof(buffer)-1 leaves space for the null terminator
    // Returns bytes read, 0 at EOF, or -1 on error
    ssize_t bytes_read = read(fd, buffer, sizeof(buffer)- 1); // Ensure space for null-terminator

    if (bytes_read ==-1){
        perror("read");
        close(fd);
        return 1;
    }

    // Add '\0' to mark the end of the C-style string
    buffer[bytes_read] = '\0'; // Null-terminate the buffer

    // Display the data read from the file
    std::cout << "Read from file: " << buffer << std::endl;

    // close(): Closes the File Descriptor and releases resources
    // Returns 0 on success or -1 on error
    if (close(fd) ==-1) {
        perror("close");
        return 1;
    }

    return 0;
}
