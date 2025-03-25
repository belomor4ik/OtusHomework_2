# contact_class.py

class Contact:
    '''
    Это класс - контакт
    '''


    def __init__(self):
        '''
        Эта функция позволяет задать имя, номер телефона и комментарий нового контакта.
        Имя не может содержать какие-либо знаки, кроме букв.
        Номер телефона может состоять только из цифр.
        Комментарий может быть произвольным.
        '''
        self.name = False
        while not self.name:
            try:
                self.name = input('Введите имя: ')
                if not self.name.isalpha():
                    raise TypeError
                else:
                    break
            except TypeError:
                print('Имя может состоять только из букв.')
        self.number = False

        while not self.number:
            try:
                self.number = input('Введите номер: ')
                if not self.number.isnumeric():
                    raise TypeError
                else:
                    break
            except TypeError:
                print('Номер может состоять только из цифр.')
        self.comment = input('Введите комментарий: ')