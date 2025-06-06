import re
from model.contact_class import Contact
# phonebook_class.py

class Phonebook:


    filename = './phonebook.csv'

    def __init__(self):
        '''
        Конструктуктор класса. До открытия телефонной книги функцией open_phonebook объект данного класса -пустой.
        '''
        self.contacts = []

    def open_phonebook(self):
        '''
        Функция открытия телефонного справочника.
        Считываем строки файла. Если файл пустой, возвращаем пустой список.
        '''
        try:
            with open(self.filename, 'r', encoding='UTF-8', newline='') as file:
                reader = file.readlines()
                for line in reader:
                    self.contacts.append(line.strip().split(';'))
        except FileNotFoundError:
            self.contacts = []
        return self.contacts

    def save_phonebook(self):
        '''
        Сохраняем телефонный справочник и перезаписываем старые записи.
        '''
        if self.contacts:
            with open(self.filename, 'w', encoding='UTF-8', newline='') as file:
                for contact in self.contacts:
                    file.write(f'{contact[0]};{contact[1]};{contact[2]};{contact[3]}\n')
            return True
        else:
            return True

    def add_contact(self):
        '''
        Функция добавления строки с новым контактом. Контакт добавляется в конец списка.
        '''
        contact = Contact()
        id_contact = len(self.contacts)
        self.contacts.append(f'{id_contact+1};{contact.name};{contact.number};{contact.comment}'.split(';'))
        return self.contacts

    def show_contacts(self):
        '''
        Вывести всех пользователей
        '''
        if self.contacts:
            print(f'Список пользователей:\n ------------------')
            for contact in self.contacts:
                print(f'ID: {contact[0]}; Имя: {contact[1]}; Телефон: {contact[2]}; Комментарий: {contact[3]}\n ------------------')
        else:
            print(f'Телефонный справочник пока что пустой.')
        return True

    def find_contact(self, id = None):
        '''
        Найти интересующий нас контакт по ID или по значению в одном из полей контакта.
        '''
        if not id:
            #Запуск поиска по текстовым полям
            text = input('Введите текст для поиска: ')
            _is_finded = False
            for contact in self.contacts:
                if (re.search(text.lower(), contact[1].lower())) or (re.search(text.lower(), contact[2].lower())) or (re.search(text.lower(), contact[3].lower())):
                    print(
                        f'ID: {contact[0]}; Имя: {contact[1]}; Телефон: {contact[2]}; Комментарий: {contact[3]}\n ------------------')
                    _is_finded = True
            else:
                if _is_finded == True:
                    return True
                else:
                    print('Совпадений не найдено')
                    return False

        else:
            #Запуск поиска по ID. В случае, если ID найден - возвращается True
            for contact in self.contacts:
                if id == int(contact[0]):
                    print(
                        f'ID: {contact[0]}; Имя: {contact[1]}; Телефон: {contact[2]}; Комментарий: {contact[3]}\n ------------------')
                    return True
            else:
                print('Пользователя с таким ID не существует')
                return False

    def change_contact(self):
        '''
        Изменить один из контактов
        '''
        idx = 0
        while idx == 0:
            try:
                idx = int(input('Введите ID контакта, который Вы хотите изменить: '))
                if type(idx) is int:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f'ID может быть только числом')
        if self.find_contact(idx):
            new_name = input('Введите новое имя: ')
            new_number = input('Введите новый номер: ')
            new_comment = input('Введите новый комментарий: ')
            self.contacts[int(idx)-1][1] = new_name
            self.contacts[int(idx)-1][2] = new_number
            self.contacts[int(idx)-1][3] = new_comment
            return True
        else:
            print('Контакт не найден')
            return False

    def delete_contact(self):
        '''
        Удалить контакт по его ID
        '''
        idx = int(input('Введите ID контакта, который Вы хотите удалить: '))
        if self.find_contact(idx):
            new_contacts = []
            for i, contact in enumerate(self.contacts):
                if int(idx) == i+1:
                    continue
                else:
                    id_next = len(new_contacts)
                    new_contacts.append(f'{id_next+1};{contact[1]};{contact[2]};{contact[3]}'.split(';'))
            else:
                self.contacts = new_contacts
