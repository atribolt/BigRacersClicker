from Include.Commands.ICommand import ICommand


class IMenu:
    def print_menu(self):
        print('Пустое меню')


class ICommandFabric:
    def __init__(self, imenu):
        self.menu = imenu

    def build(self, command_types):
        return []
