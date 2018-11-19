# Fibonacci numbers module


def fib(n):
    """returns Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    # this will be run when module is executed as main module in interpreter e.g. python fibo.py 2000
    # but no imported (print(__name__) in shell writes __main__)
    import sys
    if len(sys.argv) > 1:
        print(fib(int(sys.argv[1])))
