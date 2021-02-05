import allure
import pytest
import yaml

with open("./pytest learning1/data.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)

@allure.feature("测试计算器")

class TestCalc2:
    @allure.story("测试加法")
    @pytest.mark.add
    def test_add(self, get_calc, get_datas):
        # 调用相加方法
        with allure.step("计算两个数的相加和"):
            result = get_calc.add(get_datas[0], get_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert result == get_datas[2]

    def test_div(self,get_calc,get_datas):
        #调用除法方法
        with allure.step("除法"):
            result = get_calc.div(get_datas[0], get_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert result == get_datas[2]

    def test_sub(self,get_calc,get_datas):
        #调用减法方法
        with allure.step("减法"):
            result = get_calc.sub(get_datas[0], get_datas[1])
         if isinstance (result, float):
            result = round (result, 2)
        # 断言
        assert result == get_datas[2]

    def test_mul(self,get_calc,get_datas):
        #调用乘法方法
        with allure.step("相乘"):
            result = get_calc.mul(get_datas[0], get_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert result == get_datas[2]