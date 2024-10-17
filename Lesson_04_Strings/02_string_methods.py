# https://docs.python.org/3.9/library/stdtypes.html#string-methods


# translate
translation_table = str.maketrans('123?', 'abc!')
t1 = 'Everything fine 2ut ... repl13ement required?'
modified_text = t1.translate(translation_table)

print(t1)
print(modified_text)

# help
print(help('str.center'))

# if string can be used for variable naming
print('='*50)
variable_name = 's1x2'
print(variable_name.isidentifier())
v1 = '1s'
print(v1.isidentifier())

var10 = 'fdgsdfg'
print(f'Variable name is allowed: {var10.isidentifier()}')


