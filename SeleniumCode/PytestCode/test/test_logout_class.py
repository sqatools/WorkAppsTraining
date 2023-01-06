"""
command to install pytest
"""
import pytest

@pytest.mark.usefixtures("notscop_setup")
class TestLogout:

    @pytest.mark.smoke
    @pytest.mark.parametrize('a, b, c', ([20, 30, 50]))
    def test_login_fun1(self, a, b, c):
        assert a + b == c

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_login_fun2(self):
        num1 = 20
        num2 = 4
        assert num1*num2 == 90
        print(num1*40)

    @pytest.mark.regression
    def test_login_fun3(self):
        num1 = 50
        num2 = 5
        assert num1//num2 == 10
