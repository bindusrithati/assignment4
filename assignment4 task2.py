def file_operations():
    filename = "output.txt"
    
    # 1. Take user input and write it to the file
    user_input = input("Enter text to write to the file: ")
    with open(filename, "w") as file:
        file.write(user_input + "\n")
    print("Data successfully written to output.txt.\n")
    
    # 2. Append additional data to the same file
    append_input = input("Enter additional text to append: ")
    with open(filename, "a") as file:
        file.write(append_input + "\n")
    print("Data successfully appended.\n")
    
    # 3. Read and display final content of the file
    print(f"Final content of {filename}:")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())


# Run the function
file_operations()
