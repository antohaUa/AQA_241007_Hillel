# https://docs.python.org/3.8/library/re.html
"""
1. `.` (Dot): Matches any character except a newline.

2. `^` (Caret): Matches the start of a string.

3. `$` (Dollar): Matches the end of a string.

4. `*` (Asterisk): Matches zero or more occurrences of the preceding character or group.

5. `+` (Plus): Matches one or more occurrences of the preceding character or group.

6. `?` (Question Mark): Matches zero or one occurrence of the preceding character or group.

7. `{}` (Curly Braces): Matches a specified number of occurrences of the preceding character or group. For example, `{3}` matches exactly three occurrences.

8. `[]` (Square Brackets): Defines a character class and matches any single character within the brackets. For example, `[aeiou]` matches any vowel.

9. `()` (Parentheses): Creates a capturing group or a non-capturing group. A capturing group is used to extract a portion of the matched string.

10. `|` (Pipe): Acts as an OR operator and matches either the expression before or after the pipe.

11. `\` (Backslash): Escapes a special character, or indicates a special sequence.

12. `\b` (Word Boundary): Matches a word boundary, such as a space, comma, or beginning/end of a string.

13. `\d` (Digit): Matches any decimal digit. Equivalent to `[0-9]`.

14. `\D` (Non-Digit): Matches any character that is not a decimal digit. Equivalent to `[^0-9]`.

15. `\w` (Word): Matches any alphanumeric character and underscore. Equivalent to `[a-zA-Z0-9_]`.

16. `\W` (Non-Word): Matches any character that is not alphanumeric or underscore. Equivalent to `[^a-zA-Z0-9_]`.

17. `\s` (Whitespace): Matches any whitespace character, including space, tab, or newline.

18. `\S` (Non-Whitespace): Matches any character that is not a whitespace character.

19. `(?i)` (Ignore Case): Matches characters regardless of case.

20. `(?s)` (Single Line): Makes the dot (`.`) match all characters including newline.

"""
import re

# s1 = 'Target, day could 01 be 05 or of May'
# print(f"Or result={bool(re.search(r'May|June', s1))}")
# print('? result')
# print(bool(re.search(r'0?\d{1}', s1)))
# print('*?, +?, ?? result')
# print(re.findall(r'.*?\d{2}', s1))
# print(re.findall(r'^.+?\b', s1))  # first word
# print(re.findall(r'\w+$', s1))  # last word
#
# s2 = 'IPs: 192.168.1.100(new) and 192.168.2.255(old)'
# # we know that (?=<pattern>)
# print(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?=\(new\))', s2))
#
# s3 = 'IPs: new:192.168.1.100 and old:192.168.2.255'
# # we know that (?<=<pattern>)
# print(re.findall(r'(?<=old:)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s3))

# character sets
s4 = 'Simple digits are 123. Other digits not so simple ) 789 defghijklmnop'
print(re.findall(r'[6-9]{3}', s4))
print(re.findall(r'[m-p]{4}', s4))
