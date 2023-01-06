import pytest

@pytest.fixture(scope='function')
def smoke_setup():
    print("\n Smoke Initial Setup  done")
    yield
    print("\n Smoke setup cleanup  done")

@pytest.fixture(scope='session')
def regression_setup():
    print("\n Regression Initial Setup  done")
    yield
    print("\n Regression cleanup  done")

@pytest.fixture(scope='class')
def class_setup():
    print("\b class setup done")
    yield
    print("\n class setup cleanup done")


@pytest.fixture
def notscop_setup():
    print("\b no scope setup done")
    yield
    print("\n no scope setup cleanup done")