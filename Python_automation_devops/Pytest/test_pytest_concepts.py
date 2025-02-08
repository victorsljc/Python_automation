# pytest concepts
#     1. fixtures
#             @pytest.fixture
#     2.parametrization
#             @pytest.mark.parametrize('a,b,c',[(1,2,3),(2,3,5)])
#     3.assertions
#             assert condition, failed_message
#     4.testcase writing
#             create a file using test or test_ on start of the name

#     5.markers
            # Builtin markers
            # parametrize: Perform multiple calls to the same test function16.
            # skip: Always skip a test function23.
            # skipif: Skip a test function if a certain condition is met23.
            # xfail: Expect a test to fail1.
            # usefixtures: Use fixtures on a test function or class2.
            # filterwarnings: Filter certain warnings of a test function2.
            # Custom markers
            # # pytest.ini
            # [pytest]
            # markers =
            #     slow: marks tests as slow (deselect with '-m "not slow"')
            # #
            # Apply markers to whole class
            #     import pytest
            #
            #     @pytest.mark.webtest
            #     class TestClass:
            #         def test_startup(self):
            #             pass
            #
            #         def test_startup_and_more(self):
            # #             pass
            # Apply marker at module level
            # import pytest
            # pytestmark = pytest.mark.webtest
#     6. testcase execution modes
#         Pytest provides flexible test selection options:
#         Run tests by module: pytest test_mod.py
#         Run tests by directory: pytest testing/
#         Run tests by keyword: pytest -k "MyClass and not method"
#         Run tests by markers: pytest -m slow
import pytest
from pycparser.plyparser import parameterized


def test_sample():
    a=10
    b=10
    assert a+b==20,'failed'

def testsample():
    a=20
    b=40
    print(a+b)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  fixtures @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@pytest.fixture
def add():
    print('this is addition operation setup')
    yield
    print('this is addition operation teardown')


def test_sub(add):
    print('this is subtraction')


@pytest.fixture(params=[1,2,3])
def addition(request):
    return request.param

def test_addition_params(addition):
    print(addition+2)

# @@@@@@@@@@@@@@@@@@@@@  markers @@@@@@@@@@@@@@@@@@@'
# Builtin markers
# parametrize: Perform multiple calls to the same test function16.
# skip: Always skip a test function23.
# skipif: Skip a test function if a certain condition is met23.
# xfail: Expect a test to fail1.
# usefixtures: Use fixtures on a test function or class2.
# filterwarnings: Filter certain warnings of a test function2.
# Custom markers
# # pytest.ini
# [pytest]
# markers =
#     slow: marks tests as slow (deselect with '-m "not slow"')
# #
# Apply markers to whole class
#     import pytest
#
#     @pytest.mark.webtest
#     class TestClass:
#         def test_startup(self):
#             pass
#
#         def test_startup_and_more(self):
# #             pass
# Apply marker at module level
# import pytest
# pytestmark = pytest.mark.webtest


@pytest.mark.regression
def test_reg1():
    print('this is regression 1')
@pytest.mark.regression
def test_reg2():
    print('this is regression 2')

# @pytest.mark.sanity
def test_san1():
    print('this is regression 2')

@pytest.mark.skip(reason='this is incomplete')
def test_san2():
    print('this is regression 2')

# @pytest.mark.smoke
def test_smoke1():
    print('this is regression 2')

# @pytest.mark.smoke
def test_smoke2():
    print('this is regression 2')

@pytest.mark.parametrize("a,b,c",[(1,2,3),(2,3,5)])
def test_sum(a,b,c):
    assert a+b ==c , " it is not equal"
    print(f'the addion of {a} and {b} is {c}')

