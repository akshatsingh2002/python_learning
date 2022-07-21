try:
    print(5/0)
    print(5/'a')
except ZeroDivisionError:
    print("division by zero")
except TypeError:
    print("cannot divide by char")