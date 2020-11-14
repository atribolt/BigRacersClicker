from Include.WebDriver import WebDriver
from Include.BigRacingFabric import BigRacingFabric, Menu

if __name__ == '__main__':
    WebDriver().init({
        'user-data-dir': './Google/',
        'incognito': '',
        'disable-extensions': '',
        'disable-flash-3d': '',
        'disable-gpu': '',
        'disable-logging': '',
        'disable': 'all'
    }, 9090)
    menu = Menu()
    fabric = BigRacingFabric(menu)

    while True:
        print(fabric.menu.print_menu())
        index = input('Введи номер пункта (или пунктов через запятую): ')

        commands = fabric.build(index)
        for key in commands:
            print(f'Выполняю "{commands[key][0]}"')
            commands[key][1].execute()
        print('\n')
