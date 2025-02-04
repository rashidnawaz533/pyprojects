import json

def add_contact():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    contact = {"name": name, "age": age, "email": email}
    return contact

def display_contacts(people):
    for i, person in enumerate(people):
        print(i+1, person['name'], person['age'], person['email'])

def delete_contact(people):
    display_contacts(people)
    while True:
        number = input("Please Enter a number to delete")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("invalid Number, out of range")
            else:
                people.pop(number - 1)
                print('Person deleted')
                break
        except:
            print('invalid number')


def search_contact(people):
    search_name = input("Enter a name to search: ")
    result = []

    for person in people:
        name = person['name']
        if search_name == name:
            result.append(person)
    if not result:
        print('nothing Found')
    else:
        display_contacts(result)

print("Welcome to Contact Management System!")
with open("contacts.json", "r") as f:
    people = json.load(f)['contacts']

    while True:
        print("contact size list: ", len(people))
        choice = input("You can add, Delete, Search ar Quit 'q'").lower()
        if choice == 'add':
            person = add_contact()
            people.append(person)
            print("person added!")
        elif choice == 'delete':
            delete_contact(people)
        elif choice == "search":
            search_contact(people)
        elif choice == 'q' or 'quit':
            break
        else:
            print('Invalid command')

with open("contacts.json", 'w') as f:
    json.dump({"contacts": people}, f)
