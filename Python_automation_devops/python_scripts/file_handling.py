'''
    File handling Common Modes
        "r": Read (default mode).
        "w": Write (creates a new file or overwrites an existing file).
        "a": Append (adds data to the end of the file).
        "b": Binary mode (e.g., "rb" or "wb").
        "+": Read and write (e.g., "r+" or "w+").
    Best Practices
        Use with Statements:
            Always use with to ensure files are properly closed.
        Handle Exceptions:
            Use try-except blocks to handle file-related errors (e.g., file not found, permission issues).
        Avoid Loading Large Files into Memory:
            Process large files line by line or in chunks.
        Use pathlib for Path Manipulation:
            pathlib provides a cleaner and more intuitive way to handle file paths.
        Validate File Existence:
            Check if a file exists before performing operations on it.

'''
def test_open_and_close_file():
    # Open a file in read mode
    file = open("example.txt", "r")
    content = file.read()  # Read the file content
    file.close()  # Close the file

def test_open_file_using_with():
    with open("example.txt", "r") as file:
        content = file.read()
    # File is automatically closed here

def test_read_file_like_whole_line_and_alllines():
    with open("example.txt", "r") as file:
        # Read the entire file
        content = file.read()
        # print(content)

        # Read one line at a time
        # file.seek(0)  # Reset file pointer to the beginning
        # line = file.readline()
        # while line:
        #     print(line.strip())  # Remove newline characters
        #     line = file.readline()

        # Read all lines into a list
        file.seek(0)  # Reset file pointer to the beginning
        lines = file.readlines()
        print(lines)


def test_write_file():
    # Write to a file (overwrites existing content)
    with open("output.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a new line.")

    # Append to a file
    with open("output.txt", "a") as file:
        file.write("\nThis is appended text.")


def test_check_file_exists():
    import os
    if os.path.exists("example.txt"):
        print("File exists")

def test_delete_file():
    import os
    os.remove("example.txt")

def test_rename_file():
    import os
    os.rename("old.txt", "new.txt")

def test_copy_file():
    import shutil
    shutil.copy("source.txt", "destination.txt")

def test_move_file():
    import shutil
    shutil.move("source.txt", "destination.txt")

# working with directories

def test_create_directory():
    import os
    os.mkdir("new_directory")

def test_list_files_in_directory():
    import os
    files = os.listdir(".")
    print(files)

def test_delete_dir():
    import os
    os.rmdir("empty_directory")

# working with pathlib

def test_working_with_file_path():
    from pathlib import Path
    # Create a Path object
    file_path = Path("example.txt")

    # Read a file
    content = file_path.read_text()
    print(content)

    # Write to a file
    file_path.write_text("New content")

