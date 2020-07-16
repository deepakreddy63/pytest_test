import pytest
from account import Account, InsufficientBalance
from io import StringIO 
import sys

# parametrize --> to test number of parameters 
# xfail/skip --> to not count in the tests. xfail does testing, but doesn't include in report.

@pytest.mark.xfail
def test_account_init(account):
    assert account.name == "John Doe"
    assert account.balance == 900
    assert account.id == 1234

@pytest.mark.skip
def test_account_init1(account):
    assert account.name == "John Doe"
    assert account.balance == 1000
    assert account.id == 1234

@pytest.mark.parametrize("credit, output", [(200, 1200), (400, 1400), (800, 1900), (1980, 2980)])
def test_account_credit(account, credit, output):
    account.credit(credit)
    assert account.balance == output

def test_account_debit(account):
    
    with pytest.raises(InsufficientBalance):
        account.debit(1200)
    
    account.debit(600)
    assert account.balance == 400

def test_account_display(account):
    # Create the in-memory "file"
    temp_out = StringIO()
    # Replace default stdout (terminal) with our stream
    sys.stdout = temp_out
    account.display()
    assert temp_out.getvalue() == f"Account is under {account.name} with id {account.id} and current balance is {account.balance}\n"
    # the original output stream to the terminal.
    sys.stdout = sys.__stdout__