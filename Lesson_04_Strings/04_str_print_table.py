people = {
    "Alice": 25.101,
    "Bob": 30.217,
    "Charlie": 35.789,
    "Danielle": 140.584
}
summary = 'table printing completed'
sep_num = 25
s1 = 'Name'
print("-" * sep_num)
print(f"| {'Name':<10} | {'Something':>8} |")
print("-" * sep_num)

for name, something in people.items():
    print(f"| {name:^10}|  {something:^9.2f} |")
print("-" * sep_num)
print(f'{summary=}')
