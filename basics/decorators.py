from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            print('Function will not run')
        else:
            print('before')
            f(*args, **kwargs)
            print('after')

    return decorated


@decorator_name
def func():
    print('Function is running')


can_run = True
func()

can_run = False
func()

# Python decorators implement Aspect Oriented Programming paradigm.
# Pragmatic use case of decorators is @timeit.
