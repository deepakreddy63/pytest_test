import pytest
from account import Account

@pytest.fixture
def account():
    a = Account(1000, "John Doe", 1234)
    return a