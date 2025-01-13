class UserAccount:
    def __init__(self, login, mail, password):
        self.login=login
        self.__password=hash(password)
        self.mail=mail
    def set_password(self, new_password):
        self.__password=hash(new_password)
        return f'Ваш пароль изменён на {self.__password}'
    def check_password(self, my_password):
        return hash(my_password)==self.__password

check=UserAccount('Den', 'my_mail', 'password345')
print(check.set_password('12345678'))
print(check.check_password('12345678'))
print(check.check_password('gfhjkam'))