from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand
from selenium.webdriver.common.keys import Keys


class WorkLessCommand(ICommand):
    def execute(self):
        print('Снимаю с работы')
        chrome = WebDriver().chrome
        chrome.get('https://ok.greatraces.mobi/?0=w0w')
        try:
            chrome.find_element_by_class_name('rEndQuest').send_keys(Keys.ENTER)
            print('Снят с работы')
        except Exception:
            print('Не стоит на работе')
