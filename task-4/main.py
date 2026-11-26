import re

def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
    except ValueError:
        return ("",)

    cmd = cmd.strip().lower()
    return cmd, *args

def normalize_number(phone_number: str):
    number_cleaned = re.sub(r"\D", "", phone_number)
    if number_cleaned.startswith("0"):
        number_cleaned = f"+38{number_cleaned}" # Assuming the entered number is a UA number.
    else:
        number_cleaned = f"+{number_cleaned}"
    return number_cleaned
    
def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add NAME NUMBER"
    else:
        name, phone_number = args
        number_cleaned = normalize_number(phone_number)
        if len(number_cleaned) < 5 or len(number_cleaned) > 15:
            return "Not a valid phone number."
        if name == "":
            return "Please enter a valid name."
        else: 
            if name in contacts:
                print("Contact already exists. Updating instead.")
            contacts[name] = number_cleaned
            return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change NAME NUMBER"
    else:
        name, phone_number = args
        if name not in contacts:
            return f"{name} doesn't exist. Please create a contact with the name '{name}' first."
        else:
            number_cleaned = normalize_number(phone_number)
            if len(number_cleaned) < 5 or len(number_cleaned) > 15:
                return "Not a valid phone number."
            else:
                if name == "":
                    return "Please enter a valid name."
                else:
                    contacts[name] = number_cleaned
                    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone NAME"
    else:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f"{name} doesn't exist. Please create a contact with the name '{name}' first."

def show_all(contacts):
    if contacts == {}: 
        return "You don't have any contacts."
    else: 
        for name, number in contacts.items():
            return f"{name}: {number}"

def main():
    print("Welcome to the assistant bot!")
    contacts = {}


    commands = """
add NAME NUMBER - adds a contact.
change NAME NUMBER - updates a contact's phone number.
phone NAME - prints the contact's phone number.
all - shows all of your contacts.
hello/hi - prints 'Hello, how can I help?'
exit/close - exits out of the program.
? - shows the text you're reading right now.
"""

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ("hello", "hi"):
            print("Hello, how can I help?\n")
        elif command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "?":
            print(commands)
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__== "__main__":
    main()
    
    
    
    
    
