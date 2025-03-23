import sys
from model.phonebook_class import Phonebook
# menu_class.py

class Menu:

    def show_menu(self):
        item_menu = None
        _phonebook_is_opened = False
        while item_menu != 8:
            if not _phonebook_is_opened:
                self.menu_items = ('Открыть файл', 'Выйти')
                for i, item in enumerate(self.menu_items):
                    print(f'{i + 1}. {item}')
                item_menu = int(input('Выберите пункт меню: '))
                if item_menu == 1:
                    phonebook = Phonebook()
                    phonebook.open_phonebook()
                    _phonebook_is_opened = True
                elif item_menu == 2:
                    sys.exit()
            else:
                self.menu_items = (
                    'Сохранить файл', 'Добавить контакт', 'Показать все контакты', 'Найти контакт',
                    'Изменить контакт',
                    'Удалить контакт', 'Выйти')
                for i, item in enumerate(self.menu_items):
                    print(f'{i + 1}. {item}')
                item_menu = int(input('Выберите пункт меню: '))
                if item_menu == 1:
                    phonebook.save_phonebook()
                    _phonebook_is_opened = False
                elif item_menu == 2:
                    phonebook.add_contact()
                elif item_menu == 3:
                    phonebook.show_contacts()
                elif item_menu == 4:
                    phonebook.find_contact()
                elif item_menu == 5:
                    phonebook.change_contact()
                elif item_menu == 6:
                    phonebook.delete_contact()
                elif item_menu == 7:
                    sys.exit()