class Flex(object):
    def __init__(self, name):
        self.name = name

    def add_param(self, name, value):
        object.__setattr__(self, name, value)  # object.__delattr__ to delete

if __name__ == '__main__':
    f = Flex('example')
    f.add_param('num', 8)
    print(f.num)
