from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand
from selenium.webdriver.common.keys import Keys


class StartWorkCommand(ICommand):
    def execute(self):
        chrome = WebDriver().chrome
        chrome.get('https://ok.greatraces.mobi')
        chrome.get('https://ok.greatraces.mobi/?0=w0w')

        work = [c for c in chrome.find_elements_by_class_name('rOptionLink') if c.text == 'Работа']
        work[0].send_keys(Keys.ENTER)

        print('Ищу работу на 4 часа...')
        chrome.get('https://ok.greatraces.mobi/?0=w4work.taxi_gr5_uber&3=w0c')
        try:
            for body in chrome.find_elements_by_tag_name('tbody'):
                if body.find_element_by_class_name('rTuneHeader').text == '4 час':
                    body.find_element_by_class_name('rSellMyCar').send_keys(Keys.ENTER)
                    break
            print('Работает 4 часа')
        except Exception:
            print('Возможно модель машины не подходит')
