import pytest
import yaml

from myenv.python_code1.calc import Calculator

with open("./pytest learning1/data.yaml") as f:
    data = yaml.safe_load(f)['add']
    add_data = data['data']
    print(add_data)
    add_id = data['add_id']
    print(add_id)
    div_data = data['data']
    print(div_data)
    div_id = data ['div_id']
    print (div_id)

class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b，expect",add_data,add_id)
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",div_data,div_id)
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect

