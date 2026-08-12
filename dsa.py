import os

print("DSA Manager")
print()
print("1. Add problem")
print("2. Push to GitHub")

choice = input("Enter choice: ")

if choice == "1":
    name = input("Problem name: ")
    topic = input("Topic: ")
    difficulty = input("Difficulty: ")
    language = input("Language: ")

    folder_name = name.replace(" ", "-")
    folder_path = os.path.join(topic, folder_name)

    if os.path.exists(folder_path):
        print("\nError: Problem already exists!")
        exit()

    os.makedirs(folder_path)

    if language.lower() == "c++":
        file_name = "solution.cpp"
    elif language.lower() == "python":
        file_name = "solution.py"
    elif language.lower() == "java":
        file_name = "solution.java"
    else:
        file_name = "solution.txt"

    file_path = os.path.join(folder_path, file_name)

    open(file_path, "w").close()

    print("\nProblem created successfully!")
    print("Solution:", file_path)

elif choice == "2":
    print("Push functionality coming soon...")

else:
    print("Invalid choice")
