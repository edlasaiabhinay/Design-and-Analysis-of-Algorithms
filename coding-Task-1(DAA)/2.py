try:
    user_text = input("Enter a string to search in: ")
    pattern = "the"
    indices = []

    for i in range(len(user_text) - len(pattern) + 1):
        if user_text[i:i+len(pattern)] == pattern:
            indices.append(i)

    print(f"Pattern '{pattern}' found at indices: {indices}")
except Exception as e:
    print(f"Error: {e}")
