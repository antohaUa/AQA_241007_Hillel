# https://docs.python.org/3.8/library/re.html#re.A

# 1. `re.IGNORECASE` (or `re.I`): Ignore case when matching.
# 2. `re.MULTILINE` (or `re.M`): Enable multi-line mode, where `^` and `$` match the beginning and end of each line, not just the whole string.
# 3. `re.DOTALL` (or `re.S`): Dot (`.`) matches any character, including a newline.
# 4. `re.VERBOSE` (or `re.X`): Allow verbose regular expressions, where whitespace and comments are ignored and can be used for better readability.

text = """In fields of gold, the sun does shine,
As birds on high, their songs intertwine.
The gentle wind whispers secrets DIVINE,
Nature's beauty, a sight so fine,
A timeless symphony, forever mine."""

import re

regex1 = re.compile('^.*divine.+$', re.MULTILINE | re.I)
#regex1 = re.compile('^.*divine.+$', re.I)
print(regex1.findall(text))

# # # debug
# # regexp2 = re.search(r'Natire', text, flags=re.DEBUG | re.M)
#
#
# verbose
regex1 = re.compile(r"""\d+  # the integral part
                        \.    # the decimal point
                        \d*  # some fractional digits""", re.VERBOSE)
#
# regex2 = re.compile(r"\d+\.\d*")
