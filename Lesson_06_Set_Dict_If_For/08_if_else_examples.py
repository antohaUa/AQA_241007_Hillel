# # -------------------------------------------------------------------------------------
# s1 = '12312312sd'
#
# # assert len(s1) == 10, 'No correct'
#
# # the same assert in if-else
# if len(s1) == 10:
#     pass
# else:
#     print(f'Not correct {len(s1)}')
#
# # the same assert as ternar if
# print('Assertion passed') if len(s1) == 10 else print(f'Not correct {len(s1)}')
#
# # -------------------------------------------------------------------------------------
i1 = 7
i2 = 5
#
input_val = 49

# % 7 - foo , %5 - baz  %7 and %5 foobaz
if input_val % i1 == 0 and input_val % i2 == 0:
    print('foobaz')
elif input_val % i1 == 0:
    print('foo')
elif input_val % i2 == 0:
    print('baz')
else:
    print('Nothing')
# -------------------------------------------------------------------------------------
