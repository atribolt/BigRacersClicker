from Include.ICommandFabric import ICommandFabric, IMenu

from Include.Commands.LoginCommand import LoginCommand
from Include.Commands.WorkRepeateCommand import WorkRepeateCommand
from Include.Commands.StartWorkCommand import StartWorkCommand
from Include.Commands.WorkLessCommand import WorkLessCommand
from Include.Commands.ChangeCarCommand import ChangeCarCommand
from Include.Commands.RacingCommand import RacingCommand
from Include.Commands.WorkLessOnlyPriceCommand import WorkLessOnlyPriceCommand
from Include.Commands.LoginKnownUsersCommand import LoginKnownUsersCommand
from Include.Commands.WorkInfoCommand import WorkInfoCommand


class Menu(IMenu):
    def __init__(self):
        self.menu = dict()
        self.menu['0'] = ('Выполнить вход в одноклассники', LoginCommand())
        self.menu['1'] = ('Переставить на работу на 4 часа', WorkRepeateCommand())
        self.menu['2'] = ('Поставить на работу на 4 часа', StartWorkCommand())
        self.menu['3'] = ('Снять с работы принудительно', WorkLessCommand())
        self.menu['4'] = ('Выбрать машину', ChangeCarCommand())
        self.menu['5'] = ('Кататься', RacingCommand())
        self.menu['6'] = ('Снять с работы если завершена', WorkLessOnlyPriceCommand())
        self.menu['7'] = ('Войти с записанных аккаунтов', LoginKnownUsersCommand())
        self.menu['8'] = ('Проверить состояние работы', WorkInfoCommand())


    def print_menu(self):
        for i in self.menu:
            print(f'{i}: {self.menu[i][0]}')


class BigRacingFabric(ICommandFabric):
    def build(self, commands):
        menu = self.menu.menu
        result = {}
        commands = commands.replace(' ', '').split(',')
        print(commands)

        for i in commands:
            result[i] = menu[i]
        return result
