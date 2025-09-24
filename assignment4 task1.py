def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("Reading file content:")
            line_number = 1
            for line in file:
                print(f"line{line_number}:{line.strip()}")
                line_number += 1
    except FileNotFoundError:
        print(f"error:the file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Call the function with sample.txt
read_file("sample.txt")
