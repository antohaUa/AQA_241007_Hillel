# https://peps.python.org/pep-0343/

fh = open('some.txt', 'w')
fh.write('Hello')
fh.close()

with open('some.txt', 'w') as fh:  # __enter__
    fh.write('Hello')
    # __exit__
    # --------->  fh.close()

a = 5



# print()
#
#
# __enter__ ()  runs when object created
#
# __exit__() runs when we exit or when exception raised

# custom context manager
class CustomContextManager:
    def __init__(self, x):
        self.x = x

    def __enter__(self):
        print('Enter Context Manager')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit Context manager')
        if exc_type is None:
            print(f'No errors and we print our value= {self.x * 2}')
        else:
            print('There were some errors')


with CustomContextManager(2) as my_cm:  # __enter__
    print('In the middle')
    # val = 1 / 0
    # __exit__
