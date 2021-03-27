import pytest


@pytest.fixture
def some_constant():
    return 5

def test_someconst(some_constant):
    assert some_constant == 5