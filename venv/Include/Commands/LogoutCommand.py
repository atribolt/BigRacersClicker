import time
from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand
from selenium.webdriver.common.keys import Keys


class LogoutCommand(ICommand):
    def execute(self):
        print('Выход из одноклассников...')
        chrome = WebDriver().chrome
        chrome.get('https://m.ok.ru/cdk/st.cmd/main/st.fflo/on/st.uir/554878226782/_prevCmd/userMain/tkn/4170?_aid=leftMenuClick')
        chrome.find_element_by_class_name('base-button_target').send_keys(Keys.ENTER)
        time.sleep(1)
        chrome.find_element_by_name('button_logoff').send_keys(Keys.ENTER)
