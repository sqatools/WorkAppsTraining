"""
command to install pytest
pip install pytest-html : command to install
"""
import pytest
env = 'PROD'
import datetime
import logging

log_filename = "./logs/" + datetime.datetime.now().strftime("workapps-web-selenium-%Y-%m-%d-%H-%M-%S")
logging.basicConfig(
    filename=f"{log_filename}.log",
    format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)",
    level=logging.INFO
)
logger = logging.getLogger(__name__)




@pytest.mark.usefixtures("notscop_setup")
class TestLogin:

    @pytest.mark.smoke
    #@pytest.mark.usefixtures("smoke_setup")
    #@pytest.mark.skip
    @pytest.mark.parametrize('a, b, c', ([20, 30, 50], [40, 50, 100], [60, 70, 130]))
    def test_login_fun1(self, a, b, c):
        logger.info(f"a : {a}, b:{b}, c: {c}")
        assert a + b == c

    @pytest.mark.smoke
   # @pytest.mark.usefixtures("smoke_setup")
    def test_login_fun2(self):
        num1 = 20
        num2 = 4
        assert num1*num2 == 90
        print(num1*40)

    @pytest.mark.regression
    @pytest.mark.skipif(env == 'Test', reason="Can not test in test environment" )
   # @pytest.mark.usefixtures("smoke_setup")
    def test_login_fun3(self):
        num1 = 50
        num2 = 5
        assert num1//num2 == 10

    @pytest.mark.regression
   # @pytest.mark.usefixtures("smoke_setup")
    @pytest.mark.xfail
    def test_login_fun4(self):
        num1 = 50
        num2 = 5
        assert num1 - num2 == 45


    @pytest.mark.regression
    #@pytest.mark.usefixtures("smoke_setup")
    def test_login_fun5(self):
        num1 = 50
        num2 = 5
        assert num1 - num2 == 40