"""
command to install pytest
"""
import pytest

@pytest.mark.smoke
def test_login_fun1(smoke_setup):
    a = 20
    b = 30
    assert a + b == 50

@pytest.mark.smoke
def test_login_fun2(smoke_setup):
    num1 = 20
    num2 = 4
    assert num1*num2 == 90
    print(num1*40)

@pytest.mark.regression
def test_login_fun3(regression_setup):
    num1 = 50
    num2 = 5
    assert num1//num2 == 10

@pytest.mark.regression
def test_login_fun4(regression_setup):
    num1 = 50
    num2 = 5
    assert num1 - num2 == 40


@pytest.mark.regression
def test_login_fun5(regression_setup):
    num1 = 50
    num2 = 5
    assert num1 - num2 == 40