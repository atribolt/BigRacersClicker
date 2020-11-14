from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand


class StartGameCommand(ICommand):
    def execute(self):
        print('Запускаю игру...')
        chrome = WebDriver().chrome
        chrome.get('https://m.ok.ru/app/greatraces?refplace=52')
