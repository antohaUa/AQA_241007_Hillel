# from decimal import getcontext, Decimal
# getcontext().prec = 17
# print(*dir(float), sep='\n')
# print(help('float.as_integer_ratio'))
print((-0.125).as_integer_ratio())
print(1.1.as_integer_ratio())
print(2.2.as_integer_ratio())
print(2476979795053773 / 1125899906842624)
print(1125899906842624 * 2)
print(2476979795053773 * 2)
print((2476979795053773 * (2 + 1)) / 2251799813685248)

# use integers if possible
f1 = 23.104   # 23104
f2 = 25.109   # 25109
