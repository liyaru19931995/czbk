import allure

class TestJen:

    @allure.step(title='test01的步骤名称')
    def test_01(self):
        print('test01-----')
        assert True

    @allure.step(title='test02的步骤名称')
    def test_02(self):
        print('test02-----')
        assert False
