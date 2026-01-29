import pytest
from math_utils import MathUtils

@pytest.fixture
def math_utils():
    return MathUtils

def test_add(math_utils):
    assert math_utils.add(3, 5) == 8
    assert math_utils.add(-2, 2) == 0
    assert math_utils.add(0, 0) == 0

def test_subtract(math_utils):
    assert math_utils.subtract(10, 5) == 5
    assert math_utils.subtract(5, 10) == -5
    assert math_utils.subtract(0, 0) == 0

def test_multiply(math_utils):
    assert math_utils.multiply(3, 4) == 12
    assert math_utils.multiply(-2, 5) == -10
    assert math_utils.multiply(0, 10) == 0

def test_divide(math_utils):
    assert math_utils.divide(10, 2) == 5
    assert math_utils.divide(5, 2) == 2.5
    assert math_utils.divide(10, 0) == -1.0
