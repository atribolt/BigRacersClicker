from selenium import webdriver
from Include.Argument import Argument


options = None
chrome = None


class WebDriver:
    def __init__(self):
        self.options = options
        self.chrome = chrome

    def init(self, args, port):
        self.options = webdriver.ChromeOptions()

        for key in args:
            self.options.add_argument(Argument(key, args[key]).to_string())
        self.chrome = webdriver.Chrome(port=port, options=self.options)

        global options, chrome
        options = self.options
        chrome = self.chrome
