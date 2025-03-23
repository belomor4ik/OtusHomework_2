# contact_class.py

class Contact:

    def __init__(self):
        while True:
            try:
                self.name = input('Введите имя: ')
                if not self.name.isalpha():
                    raise TypeError
                else:
                    break
            except TypeError:
                print('Имя может состоять только из букв.')

        while True:
            try:
                self.number = input('Введите номер: ')
                if not self.number.isnumeric():
                    raise TypeError
                else:
                    break
            except TypeError:
                print('Номер может состоять только из цифр.')
        self.comment = input('Введите комментарий: ')