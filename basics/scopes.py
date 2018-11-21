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
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)  # current scope override global scope
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
