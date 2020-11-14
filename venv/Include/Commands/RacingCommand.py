import time
from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand
from selenium.webdriver.common.keys import Keys


class RacingCommand(ICommand):
    def execute(self):
        count = int(input('Введи кол-во заездов и следи за напитками: '))
        chrome = WebDriver().chrome

        chrome.get('https://ok.greatraces.mobi/?0=2')

        i = 0
        for i in range(count):
            try:
                chrome.find_elements_by_class_name('rRace')[0].send_keys(Keys.ENTER)
                time.sleep(1)
            except Exception:
                chrome.get('https://ok.greatraces.mobi/?0=2')

        print('Откатал')
