def somedecorator(func):
    def wrapper(*args, **kwargs):
        print("%%%%%")
        result = func(*args, **kwargs)
        print("**********")
        return result

    return wrapper

# def deco(func):
#     def wrapper():
#         print('*' * 10)
#         func()
#         print('*' * 10)
#     return wrapper