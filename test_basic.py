import pytest
import math

# To introduce pytest, fixture, markers
# usage::
# pytest -v -->for verbose
# pytest -q -->for concise 
# pytest -k less -->tests only function with "less" string in them
# pytest -m math -v -->To run test functions with custom name marker
def test_equality():
    a = 10
    assert a == 10

def test_greater_than_equal():
    a = 12
    assert a >= 15    

def test_wrong_input_type():
    ''' To test wrong input type error'''
    a = "test"
    with pytest.raises(TypeError):
        assert a < 15   

@pytest.fixture
def input():
    "fixture to input value for test functions"
    return 25


def test_less_than(input):
    assert input < 30

@pytest.mark.math
def test_sqrt(input):
    assert math.sqrt(input) == 5