import json
from pathlib import Path

path = Path("phones.json")

if path.exists():
    f = open("phones.json", "r")
    phones = json.load(f)
    f.close()

else:
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
    answer = input("Do you want to continue Y/N?")
    while answer.lower() not in ["y", "n"]:
        print("Choose Y or N only")
        answer = input("Do you want to continue Y/N?")

    if answer.lower() == "n":
        f = open("phones.json", "w")
        json.dump(phones, f)
        f.close
        break
