a, b = 5, 10
print(hex(id(a)))

a, b = b, a
print(a)
print(b)


"""
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream
"""
import sys

data = ['Some', 'text', 'that', 'we', 'print']
print('a', 'b', sep='-', end='\n\n\nEND', file=sys.stderr)

print(1)
print('sdsfsd', 'sdfsadf')

# dir(var1)
