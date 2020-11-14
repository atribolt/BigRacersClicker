from Include.static_methods import check_work_completed
from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand
from Include.Commands.WorkLessCommand import WorkLessCommand


class WorkLessOnlyPriceCommand(ICommand):
    def execute(self):
        chrome = WebDriver().chrome
        chrome.get('https://ok.greatraces.mobi/?0=w0w')

        is_complete = check_work_completed()
        if is_complete:
            WorkLessCommand().execute()
            print('Деньги за работу получены')
