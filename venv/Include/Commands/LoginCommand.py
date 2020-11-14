from getpass import getpass
from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand
from selenium.webdriver.common.keys import Keys


class LoginCommand(ICommand):
    def __init__(self, login='', password=''):
        self.login = login
        self.password = password

    def execute(self):
        if self.login == '' or self.password == '':
            self.login = input('Введи логин: ')
            self.password = getpass('Введи пароль: ')

        print(f'Вход в одноклассники: {self.login}, "пароль нипокажу"')
        chrome = WebDriver().chrome
        chrome.get('https://m.ok.ru')
        chrome.find_element_by_name('fr.login').send_keys(self.login)
        chrome.find_element_by_name('fr.password').send_keys(self.password)
        chrome.find_element_by_class_name('base-button_target').send_keys(Keys.ENTER)
