import Calculator as Calculator
import pytest

@pytest.fixture(scope='module')
def get_calc():
    print('开始结算')
    calc = Calculator()
    return calc
    yield
    print ('计算结束')