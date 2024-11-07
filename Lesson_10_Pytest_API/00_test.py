a = 10

if a > 10:
    print('Great A')
else:
    print('Error')

assert a > 10, 'Error here'

# python -O <file>   # assertion will be skipped
# try:
#     assert a > 10, 'Error here'
# except AssertionError as assert_err:
#     print(assert_err)
