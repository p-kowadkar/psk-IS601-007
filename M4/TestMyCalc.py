import pytest
from MyCalc import MyCalc

# psk 10/14/2023 Create an instance of the MyCalc class
calc = MyCalc()

# psk 10/14/2023 addition test cases
@pytest.mark.parametrize("num1, num2, z", [(5, 3, 8), (20, 10, 30), (-5, 2, -3), (17, -8, 9)])
def test_num_add_num(num1, num2, z):
    assert z == calc.add(num1, num2)

# psk 10/14/2023 ans-add-num test cases
@pytest.mark.parametrize("num1, num2, z", [("ans", 3, 12), ("ans", 500, 512), ("ans", -2, 510), ("ans", -500, 10)])
def test_ans_add_num(num1, num2, z):
    if num1 == "ans":
        result = calc.ans
    assert z == calc.add(result, num2)

# psk 10/14/2023 sub test cases
@pytest.mark.parametrize("num1, num2, z", [(10, 3, 7), (60, 30, 30), (-15, -5, -10), (23, -15, 38)])
def test_num_sub_num(num1, num2, z):
    assert z == calc.sub(num1, num2)

# Updated values for ans-sub-num test cases
@pytest.mark.parametrize("num1, num2, z", [("ans", 100, -62), ("ans", 10, -72), ("ans", -15, -57), ("ans", 25, -82)])
def test_ans_sub_num(num1, num2, z):
    if num1 == "ans":
        result = calc.ans
    assert z == calc.sub(result, num2)

# psk 10/14/2023 multiply test cases
@pytest.mark.parametrize("num1, num2, z", [(5, 5, 25), (8, 8, 64), (-7, 2, -14), (12, -6, -72)])
def test_num_mul_num(num1, num2, z):
    assert z == calc.multiply(num1, num2)

# psk 10/14/2023 ans-mul-num test cases
@pytest.mark.parametrize("num1, num2, z", [("ans", -5, 360), ("ans", 8, 2880), ("ans", 3, 8640), ("ans", 9, 77760)])
def test_ans_mul_num(num1, num2, z):
    if num1 == "ans":
        result = calc.ans
    assert z == calc.multiply(result, num2)

# psk 10/14/2023 division test cases
@pytest.mark.parametrize("num1, num2, z", [(10, 2, 5), (100, 10, 10), (-15, -3, 5), (24, -6, -4)])
def test_num_div_num(num1, num2, z):
    assert z == calc.divide(num1, num2)

# psk 10/14/2023 ans-div-num test cases
@pytest.mark.parametrize("num1, num2, z", [("ans", 2, -2.0), ("ans", 5, -0.4), ("ans", -10, 0.0), ("ans", -4, 0.0)])
def test_ans_div_num(num1, num2, z):
    if num1 == "ans":
        result = calc.ans
    assert z == calc.divide(result, num2)