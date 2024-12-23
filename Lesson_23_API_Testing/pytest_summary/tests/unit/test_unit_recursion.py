import pytest
from code.lib_recursion import complex_list_sum

@pytest.mark.unit
class TestUnitRecursion:
    def test_sum1(self):
        l1 = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
        assert complex_list_sum(l1) == 72, 'Incorrect sum'

    def test_sum2(self):
        l1 = [5, 9, [1, 5]]
        assert complex_list_sum(l1) == 20, 'Incorrect sum'
