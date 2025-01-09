# open input.txt file and find all small english letters that match such conditions:

# target small letter round exactly with three capital english letters on the left and on the right
# Match examples:
# sdTRYaUVKn  -> matches "a" because 'TRY' on the left ( 3 capital letters ) and 'UVK' on the right ( 3 capital letters)
# NTRSjARTb   -> no match ( not exactly 3 capital letters on the left ('NTRS' = 4 letters) )
# zDFGbOPNq   -> matches "b"
# Print Output as : "Result: "string of found letters">

# Note:
#  - Result will be human readable string up to 10-15 characters
#  - Some usefull regexp constructions
# [A-Z]  - match any capital letter
# [^A-Z] - match any character except capital letter
# [a-z]  - match small letter
# do not forget about possible PRE and POST regexp searches

import re


def letters_search(filename):
    with open(filename, 'r') as input_fh:
        data = input_fh.read()

    pattern = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
    target_matches = re.findall(pattern=pattern, string=data)
    return target_matches


if __name__ == '__main__':
    print(letters_search('input.txt'))
