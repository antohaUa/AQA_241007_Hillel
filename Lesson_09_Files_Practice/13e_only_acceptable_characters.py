# Given string  of characters
# Check that all characters are from ascii table
# starting from space character(32) and finishing ~ character(126)
# return true or false
s1 = '🦊 sdf45435324 🦆'  # -> False
s2 = 'Super String~'  # -> true
START_CH = ' '


# '0' < '4' < 'a'
# all()

def needed_characters(str1):
    return all([START_CH <= itm <= '~' for itm in str1])


print(needed_characters(s1))
print(needed_characters(s2))
