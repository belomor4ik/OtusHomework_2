import sys
from model.phonebook_class import Phonebook
# menu_class.py

class Menu:


    def show_menu(self):
        item_menu = None
        _phonebook_is_opened = False
        while item_menu != 8:
            if not _phonebook_is_opened:
                #Пока телефонный справочник не открыт, пользователь может только открыть его или выйти из программы.
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
                #Когда пользователь открыл справочник, он может с ним работать.
                self.menu_items = (
                    'Сохранить файл', 'Добавить контакт', 'Показать все контакты', 'Найти контакт',
                    'Изменить контакт',
                    'Удалить контакт', 'Выйти')
                for i, item in enumerate(self.menu_items):
                    print(f'{i + 1}. {item}')
                item_menu = int(input('Выберите пункт меню: '))
                if item_menu == 1:
                    #Сохранить изменения
                    phonebook.save_phonebook()
                    _phonebook_is_opened = False
                elif item_menu == 2:
                    #Добавить контакт
                    phonebook.add_contact()
                elif item_menu == 3:
                    #Показать контакты
                    phonebook.show_contacts()
                elif item_menu == 4:
                    #Найти контакты
                    phonebook.find_contact()
                elif item_menu == 5:
                    #Изменить контакт
                    phonebook.change_contact()
                elif item_menu == 6:
                    #Удалить контакт
                    phonebook.delete_contact()
                elif item_menu == 7:
                    sys.exit()