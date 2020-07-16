# pytest_test
To understand and test pytest with CI

## Installation
### To create virtual environment 
python3 -m venv pytest-env  
source pytest-env/bin/activate
### Install pytest using pip
pip install pytest  
pip install coverage

## Tested following pytest features
- pytest will run all files starting with test\_*.py or ending with *\_test.py.
- pytest requires functions to test to start with test*
- We can use pytest.mark.name to group all test functions with a name marker
- use pytest.fixture decorator for a function to use it as a fixture to avoid code duplication.
All fixture functions can be defined with in same file or **conftest.py** for common access 
- Parametrize to run test against multiple set of inputs
- xfail/skip is to not count in the tests. xfail does testing, but doesn't include in report.
- To stop testing after n num of failures. e.g: pytest --maxfail = 1
- _coverage run -m pytest arg1 arg2_ to run python coverage on testing files. _coverage report -m_ to view report.


### Files
├── account.py  
├── conftest.py  
├── README.md  
├── test_basic.py --> To test basic pytest features like fixture, subset of tests using markers, substrings  
└── test_intermediate.py --> To test parametrize, xfail/skip on class methods  

