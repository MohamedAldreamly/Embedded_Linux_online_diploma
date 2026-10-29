
def write_to_file(filename, content):

    # try: Executes code that might raise an exception.
    # If an IOError occurs, execution jumps to the except block.
    try:

        # open(): Opens the file in write mode ('w').
        # 'w': Creates the file if it does not exist.
        # 'w': Overwrites the file if it already exists.

        # with: A context manager that automatically closes
        # the file when the block finishes, even if an error occurs.

        # as f: Assigns the opened File Object to the variable 'f'.
        # 'f' is used to access file methods like:
        # write(), read(), seek(), tell(), and close().
        with open(filename, 'w') as f:

            # write(): Writes the content into the file.
            f.write(content)

            # Prints a success message after writing.
            print(f"Successfully wrote to {filename}")

        # The file is automatically closed here by 'with'.

    # except: Handles exceptions raised inside the try block.
    # IOError: Handles file I/O errors, such as permission errors.
    # If no IOError occurs, this block is skipped.
    except IOError:

        # Displays an error message if a file I/O operation fails.
        print(f"Error writing to {filename}")


# Example usage:

# The name of the file to create or open.
filename = "output.txt"

# The text data to write into the file.
# \n creates a new line.
content = "Hello, world!\nThis is a simple file write example."

# Calls the function and passes the filename and content.
write_to_file(filename, content)
