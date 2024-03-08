from collections import UserDict

#Базовий клас для полів запису
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)




#Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    pass



#Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
class Phone(Field):
    def __init__(self, value: str):
        if not all([len(value) == 10, value.isdigit()]):
            raise ValueError("The phone number must consist of 10 digits")
        self.value = value



#Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

#Додавання телефонів.Видалення телефонів.Редагування телефонів.Пошук телефону.
            
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == old_phone:
                self.phones[i] = Phone(new_phone)
        
    def remove_phone(self, del_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == del_phone:
                phone = self.phones[i]
                self.phones.remove(phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    



#Клас для зберігання та управління записами.
class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, value):
        return(self.data.get(value))

    def delete(self, name):
        del self.data[name]

#Додавання записів. Пошук записів за іменем. Видалення записів за іменем.

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")


print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
