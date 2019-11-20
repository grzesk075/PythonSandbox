def scope_test():
    def do_local():
        spam = "local spam"  # only inside this function

    def do_nonlocal():
        nonlocal spam  # outer scope
        spam = "nonlocal spam"

    def do_global():
        global spam  # global scope
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)  # test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)  # nonlocal spam
    do_global()
    print("After global assignment:", spam)  # nonlocal spam

    # another use case
    numbers = [1, 2, 3]
    if True:
        numbers = [4, 5, 6]
        letters = ['a', 'b', 'c']  # This is visible in scope of whole function!

    print('Numbers: ', numbers)  # Numbers:  [4, 5, 6]
    print('Letters: ', letters)  # Letters:  ['a', 'b', 'c']


scope_test()
print("In global scope:", spam)  # global spam

if __name__ == '__main__':
    print("In main function scope:", spam)  # global spam
