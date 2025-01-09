import re

# # #################################################################################
# # extract date from string
# s1 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
#
# # findall
# result = re.findall(r'\d{2}-\d{2}-\d{4}', s1)
# print(result)
# result = re.findall(r'(\d{2})-(\d{2})-(\d{4})', s1)  # only year
# print(result)
#
# # match  (?P<name>...)
# if result := re.match(r'^.*?(?P<date>\d{2}-\d{2}-(?P<year>\d{4}))', s1):
#     print(result.group(0))
#     print(result.group(1))
#     print(result.group(2))
#     print(result.group('date'))
#     print(result.group('year'))
# # # #################################################################################
#
# # first two letters from each word
# s2 = "The gentle wind whispers secrets divine"
#
# # findall
# print(re.findall(r'\b\w\w', s2))
#
# # search
# result = re.search(r'(?P<start>\b\w\w).', s2)
# print(result.group(0))
# print(result.group(1))
# print(result.group('start'))
#
# if result := re.search(r'(?P<start>\b\w\w).', s2):
#     print(result.group('start'))
#
# # ####################################################################################
# # split
# s3 = 'Target string,that has;several delimiters.End'
# # print(s3.split(','))
# result = re.split(r'[;,\s\.]', s3)
# print(result)
#
# # #####################################################################################
# s4 = "He was carefully disguised but captured quickly by police."
# for curr_match in re.finditer(r"\w+ly", s4):
#     print(f'found "{curr_match.group(0)}" at position {curr_match.start()}-{curr_match.end()}')
#
# # #####################################################################################
# values = ['A1', 'B2', 'C44', 'Y1000']
# s4 = 'Some text *A1_ with _C44& inside'
# for itm in values:
#     rg = r'[_-](?P<VAL>' + re.escape(itm) + r')[&*]'
#     if result := re.search(rg, s4):
#         print(result.group('VAL'))
#         break

# #####################################################################################
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Names and Surnames</title>
    <style>
        table {
            border-collapse: collapse;
            width: 300px;
        }

        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }

        th {
            background-color: #f2f2f2;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h2>Names and Surnames</h2>
    <table>
        <tr>
            <th>Name</th>
            <th>Surname</th>
        </tr>
        <tr>
            <td>John</td>
            <td>Doe</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>Smith</td>
        </tr>
        <tr>
            <td>Michael</td>
            <td>Johnson</td>
        </tr>
        <tr>
            <td>Sarah</td>
            <td>Williams</td>
        </tr>
        <tr>
            <td>Robert</td>
            <td>Brown</td>
        </tr>
    </table>
</body>
</html>
"""
import re

# write here solution with group
# r2 = re.compile(r'<td>([a-zA-Z]+)</td>', re.MULTILINE)
r2 = re.compile(r'(?<=<td>)[a-zA-Z]+(?=</td>)', re.MULTILINE)
result = r2.findall(html)
print(result)

names = result[::2]
surnames = result[1::2]
print(names)
print(surnames)
names_surnames = list(zip(names, surnames))
print(names_surnames)



