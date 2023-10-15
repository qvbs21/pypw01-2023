phones = {}
commands = [
    "new_contact", "show_contacts"
]
while True:
    command = input(f"Peek an option: {commands} ")
    while command not in command:
        print("Unknown command, try again")
        command = input(f"Peek an option: {commands} ")

    if command == "new_contact":
        full_name = input("Input full name: ")
        phone_num = input("Input phone number: ")
        phones[full_name] = phone_num
    elif command == "show_contacts":
        print(phones)
    command = input("Do you want to continue Y/N?")
    if command == "N":
        break
