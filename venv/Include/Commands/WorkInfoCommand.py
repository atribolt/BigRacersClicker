from Include.static_methods import check_work_completed
from Include.WebDriver import WebDriver
from Include.Commands.ICommand import ICommand
from selenium.webdriver.common.keys import Keys


class WorkInfoCommand(ICommand):
    def execute(self):
        check_work_completed()