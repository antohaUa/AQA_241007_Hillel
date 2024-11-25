class Word:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if isinstance(other, Word):
            return Word(f'{self.text} {other.text}')
        raise TypeError("Unsupported operand type(s) for +")

    def __repr__(self):
        return self.text


# Usage
s1 = Word("Hello")
s2 = Word("World")
result = s1 + s2
print(repr(result))


#####################################################################

class HexAdder:
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError("HexAdder only accepts integer values")
        self.value = value

    def __add__(self, other):
        if isinstance(other, HexAdder):
            # Perform addition as if the values were hexadecimal
            hex_sum = int(hex(self.value)[2:], 16) + int(hex(other.value)[2:], 16)
            return HexAdder(int(str(hex_sum), 16))
        elif isinstance(other, int):
            # Treat `other` as a decimal integer but process as hexadecimal
            hex_sum = int(hex(self.value)[2:], 16) + int(hex(other)[2:], 16)
            return HexAdder(int(str(hex_sum), 16))
        raise TypeError("Unsupported operand type(s) for +")

    def __repr__(self):
        return f"HexAdder({self.value})"


# Usage
h1 = HexAdder(0xF)
h2 = HexAdder(0x1)

# Adding as if they were hexadecimal numbers
add_result = h1 + h2
print(add_result)

# Adding with a decimal integer
rprint(repr(result))
print(result2)
