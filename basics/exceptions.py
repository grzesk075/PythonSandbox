class MyException(Exception):
    """My first training exception"""
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2


try:
    raise MyException('abc', 2)
    # 1/0
    # raise Exception('first', 'second')
    # pass
except MyException as e:
    print('MyException {0}, {1} was caught'.format(e.prop1, e.prop2))
except Exception as e:
    print('Exception {0} was caught'.format(type(e)))  # type() returns description of any object type
    print('Args of exception:', e.args)
    print('The whole __str__:', e)
    print('Rethrowing it ...')
    raise  # rethrow an exception
else:
    print('Exception was not thrown')
finally:
    print('Finally clean-up actions')  # with command are explained in files.py
