"""
command to install pytest
"""
import pytest

#@pytest.fixture(scope='function')
@pytest.fixture(scope='session')
def setup():
    print("Initial Setup Completed")
    yield
    print("Setup Cleanup Completed")

@pytest.mark.smoke
def test_addition(setup):
    a = 20
    b = 30
    print("Addition :", a+b)
    assert a + b == 50

@pytest.mark.smoke
def test_multiplication(setup):
    num1 = 20
    num2 = 4
    assert num1*num2 == 90
    print(num1*40)

@pytest.mark.smoke
def test_division(setup):
    num1 = 50
    num2 = 5
    print("Division :", num1//num2)
    assert num1//num2 == 10

@pytest.mark.regression
@pytest.mark.smoke
def test_subtraction(setup):
    num1 = 50
    num2 = 5
    assert num1 - num2 == 45

"""
%Y = Year 2023
%y = Year 23
%m = month 01
%M = Minute 58
%d = day 5
%D = 01/05/23
%h = Month Jan
%H = Hour
import datetime
datetime.datetime.now().strftime('%Y_%h_%d')
"""