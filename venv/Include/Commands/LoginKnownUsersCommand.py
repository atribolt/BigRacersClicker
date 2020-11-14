import io
import json
import os
from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand
from Include.Commands.LoginCommand import LoginCommand


class LoginKnownUsersCommand(ICommand):
    def __init__(self):
        path = './users.json'
        data = ''
        try:
            file = open(path, 'r')
            data = ' '.join(file.readlines())
            file.close()
            self.users = json.loads(data)
        except Exception:
            print(data)
            self.users = None

    def execute(self):
        if self.users is None:
            print(f'Проверь файл {os.getcwd()}/users.json. В нем нет аккаунтов')
            return

        print('Нашел эти аккаунты:')
        for i in self.users:
            print(f'\t{i}: {self.users[i]["login"]}')

        index = input('Введи номер нужного для входа: ')
        login    = self.users[index]["login"]
        password = self.users[index]["password"]

        LoginCommand(login, password).execute()
