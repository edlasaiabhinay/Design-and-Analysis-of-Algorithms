def read_file_content(): #to read and display file content
    try:
        filename = input("Enter file name with extension: ")
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print("Error:", e)
read_file_content()
