# def f1(name):
#     print(name)
#
# f1('Alan')
# # print(name)



def say():
    greeting = 'Hello'               # |
    print(hex(id(greeting)))         # |
                                     # |    --> Closure

    def display():                   # |
        print(hex(id(greeting)))     # |
        print(greeting)              # |

    return display


if __name__ == '__main__':
    fn = say()
    # print(fn.__closure__)
    fn()

# # https://www.pythontutorial.net/advanced-python/python-closures/
