d1 = {}
print(type(d1))
d2 = dict()
d3 = {(1, 2, 3): None,
      frozenset((1,)): 56,
      'some_string': 45, 5.0: 2.8,
      True: False, (1, 2, 3): True,
      (1, 2, 3): 200
      }

# incorrect dict
# d3 = {[1, 2, 3]: None, frozenset((1,)): 56, 'some_string': 45, 5.0: 2.8, True: False}
print(d3)
d4 = {1: 1, 2: 2, 3: 3, 4: 4}
d4 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
d4 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}  # 8 elemnets by default then size change if filled 2/3
print(d4.__sizeof__())
#
# # dictionary changed size during iteration
# d_new = {'a': 1, 'b': 2}
# for itm in d_new:
#     d_new.pop(itm)

# how to avoid dictionary changed size during iteration - possible solutions
d_new = {'a': 1, 'b': 2}
for itm in list(d_new.keys()):
    d_new.pop(itm)
d_new = {'a': 1, 'b': 2}
for itm in d_new.values():
    print(type(itm))
    print(itm)
