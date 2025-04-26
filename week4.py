# Reading and writing files in Python
try:
    # Open the input file in read mode
    with open('input_file.txt', 'r') as input_file:
        # Read the contents of the file
        content = input_file.readlines()

    # Modify the content (example: convert all text to uppercase)
    modified_content = [line.upper() for line in content]

    # Write the modified content to a new file
    with open('output_file.txt', 'w') as output_file:
        output_file.writelines(modified_content)

    print("File has been successfully modified and saved as 'output_file.txt'.")

except FileNotFoundError:
    print("The input file was not found. Please check the file name or path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Handling file errors in Python
filename = input("Enter the filename: ")

try:
    # Attempt to open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist. Please check the filename.")
except PermissionError:
    print(f"Error: You don't have permission to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
