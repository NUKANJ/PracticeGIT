import pytest

def mul(num1,num2):
    return num1*num2

def add(num1,num2):
    return num1+num2

@pytest.fixture
def init():
    print('Test method execution started')
    yield
    print('Test method execution ended')

def test_m1(init):
    actuals = mul(10,30)
    assert actuals == 300

def test_m2(init):
    actuals = add(10,30)
    assert actuals == 40
