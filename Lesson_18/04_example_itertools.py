from itertools import chain


def chain2(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


print(*list(chain2('EDF', 'CBA')), sep='\n')
print('*' * 20)
print(*list(chain('ABC', 'EDF')), sep='\n')
