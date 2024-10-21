# Importing python's built-in logging module
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
_log = logging.getLogger(__name__)

# Initializing variables to be used in boolean operations
x = bool(1123123)
y = bool(0)
# _log.info(y)
# _log.info(x)

a = True
b = False
_log.info('Comparison operations:')
_log.info('-' * 20)
_log.info(f'a is equal to b: {a == b}')  # Equal by value to
_log.info(f'a is not equal to b: {a != b}')  # Not equal by value to
_log.info(f'a in memory equals to b memory object: {a is b}')  # Equal and point to the same memory object
_log.info(f'a in memory not equals to b memory object: {a is not b}')  # Equal and not point to the same memory object

# |Operator |Description |
# |--------|-------------|
# |AND      |Returns true only if both operands are true|
# |OR       |Returns true if at least one of the operands is true|
# |NOT      |Returns the opposite of the operand (true becomes false, and false becomes true)|
# |XOR      |Exclusive OR - Returns true only if one operand is true and the other is false|
# |NAND     |Not AND - Returns true only if at least one operand is false|
# |NOR      |Not OR - Returns true only if both operands are false|
# |XNOR     |Exclusive NOR - Returns true only if both operands are true or both operands are false|

# AND
# 1100
# 0101
# ----
# 0100

# OR
# 1101
# 0101
# ----
# 1101

# OR
# 1
# 0
# -
# 1


# Performing boolean operations using variables a and b
c = a and b  # Logical AND
d = a or b  # Logical OR
e = not a  # Logical NOT
f = a ^ b  # Logical XOR

# Displaying the results of boolean operations using the logger object
_log.info('Logical operations:')
_log.info('-' * 20)
_log.info(f'Logical AND of {a} and {b} is {c}')
_log.info(f'Logical OR of {a} and {b} is {d}')
_log.info(f'Logical NOT of {a} is {e}')
_log.info(f'Logical XOR of {a} and {b} is {f}')

check1 = all((1 == 1, 1, None is None, 5 * 3 == 15))
_log.info(check1)
check2 = any((False, True is None, 6 * 7 != 42, 0, 12))
_log.info(check2)

#   True         False   -> True
if 5 * 3 == 15 or False:
    _log.info('if #1 passed')
#   True         True   -> True
if 5 * 3 == 15 and True:
    _log.info('if #2 passed')
