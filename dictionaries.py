phones = {}
while True:
    command = input("Peek an option: new_contact, show_contacts")
    if command == "new_contact":
        full_name = input("Input full name: ")
        phone_num = input("Input phone number: ")
        phones[full_name] = phone_num
    elif command == "show_contacts":
        print(phones)
    command = input("Do you want to continue Y/N?")
    if command == "N":
        break
