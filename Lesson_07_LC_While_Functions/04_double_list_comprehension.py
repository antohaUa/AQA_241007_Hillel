# RARE!
# double for
phrase = ['Some', 'phrase']
# ['S', 'o'....]
l1 = []
for word in phrase:
    for character in word:
        l1.append(character)
print(l1)

l2 = [character for word in phrase for character in word]
print(l2)

list_of_lists = [[1, 2, 3], [4, 5, 6]]
flat_list = [number for internal_list in list_of_lists for number in internal_list]
print(flat_list)
