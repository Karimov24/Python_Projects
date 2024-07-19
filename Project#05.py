def show_menu():
    print("1. View To-Do List\n2. Add Item\n3. Remove Item\n4. Save List\n5. Load List\n6. Exit")

def view_list(todo_list):
    for idx, item in enumerate(todo_list, 1):
        print(f"{idx}. {item}")

def add_item(todo_list):
    todo_list.append(input("Enter a new To-Do item: "))

def remove_item(todo_list):
    view_list(todo_list)
    idx = int(input("Enter the number of the item to remove: ")) - 1
    if 0 <= idx < len(todo_list):
        todo_list.pop(idx)

def save_list(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as file:
        file.write("\n".join(todo_list))

def load_list(filename="todo_list.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def main():
    todo_list = load_list()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_list(todo_list)
        elif choice == "2":
            add_item(todo_list)
        elif choice == "3":
            remove_item(todo_list)
        elif choice == "4":
            save_list(todo_list)
        elif choice == "5":
            todo_list = load_list()
        elif choice == "6":
            break

if __name__ == "__main__":
    main()
