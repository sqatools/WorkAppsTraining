"""
command to install pytest
"""
import pytest

@pytest.mark.abc
class TestHotelBooking():

    def test_HotelBooking_fun1(self):
        a = 20
        b = 30
        assert a + b == 50

    @pytest.mark.smoke
    def test_HotelBooking_fun2(self):
        num1 = 20
        num2 = 4
        assert num1*num2 == 80
        print(num1*40)

    @pytest.mark.smoke
    def test_HotelBooking_fun3(self):
        num1 = 50
        num2 = 5
        assert num1//num2 == 10

    @pytest.mark.regression
    def test_HotelBooking_fun4(self):
        num1 = 50
        num2 = 5
        assert num1 - num2 == 40
