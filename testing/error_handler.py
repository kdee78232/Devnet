def cars(**kwargs):
    for key, value in kwargs.items():
        print("hello", value)

cars(kwarg1="john",kwarg2='sue')
