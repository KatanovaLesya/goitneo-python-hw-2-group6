#додаєм обробку помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
  
@input_error
def add_contact(args, contacts):
  name, phone = args 
  contacts[name] = phone
  return "Contact added."

@input_error
def change_contact(args, contacts):
  name = args[0]
  new_phone = args[1]
  contacts[name] = new_phone
  return "Contact changed."

@input_error
def user_phone(args, contacts):
  name = args[0]
  phone = contacts[name]
  return (phone)

def all_contacts(contacts):
    list = contacts
    return (list)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(user_phone(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
