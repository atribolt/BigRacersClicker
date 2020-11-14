class Argument:
    def __init__(self, key, value=''):
        self.key = key
        self.value = value

    def to_string(self):
        result = self.key
        if self.value != '':
            result = f'{result}={self.value}'
        return result
