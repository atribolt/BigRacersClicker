from Include.Commands.ICommand import ICommand
from Include.WebDriver import WebDriver
from selenium.webdriver.common.keys import Keys


class ChangeCarCommand(ICommand):
    def execute(self):
        print('Ищу машины')
        chrome = WebDriver().chrome

        chrome.get('https://ok.greatraces.mobi/?0=c1')
        chrome.get('https://ok.greatraces.mobi/?0=g&8=1714115474f&3=c1')

        car_list = chrome.find_elements_by_class_name('rMyCar')
        print('Все машины этого бомжа:')
        for i in range(len(car_list)):
            name = car_list[i].find_element_by_class_name('rCarMark').text
            print(f'\t{i}: {name}')
        index = int(input('Введи номер машины: '))

        car = car_list[index].find_element_by_class_name("rCarMark")
        print(f'Выбрана машина: {car.text}')
        car_list[index].find_element_by_class_name('rChangeMyCar').send_keys(Keys.ENTER)
