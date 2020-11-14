from Include.WebDriver import WebDriver
from Include.Commands.StartGameCommand import StartGameCommand

def check_work_completed():
    chrome = WebDriver().chrome
    state = False
#    StartGameCommand().execute()

    chrome.get('https://ok.greatraces.mobi/?0=w0w')
    try:
        price = chrome.find_element_by_class_name('rEndQuest')
        if price.text == 'Забрать':
            state = True
            print('Работа завершена')
        else:
            state = False
            print(f'Осталось работать: {chrome.find_element_by_id("time").text}')
    except Exception:
        state = False
        print('Не стоит на работе')

    return state
