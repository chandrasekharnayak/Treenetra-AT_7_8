# marker is pytest method for run the test case based to customer requirement
#skip,skipif,xfail, passed,parameterized, custom
# pytest file -v -s
#pytest file_name -m custom_mark_name -v -s
import sys

import pytest

@pytest.mark.skip(reason='i do not want to run the test for now')
def test_1():
    pass

@pytest.mark.skip
def test_2():
    pass

@pytest.mark.skipif(sys.version_info<(3,16),reason='Required python 3.16')
def test_3():
    pass

@pytest.mark.xfail(reason = 'this test is excepted to fail')
def test_4():
    pass

@pytest.mark.passed(reason= 'Forcing this test to be marked as passed')
def test_5():
    pass

@pytest.mark.smoke
@pytest.mark.regression
def test_6():
    pass
@pytest.mark.smoke
@pytest.mark.regression
def test_7():
    pass
@pytest.mark.regression
def test_8():
    pass
@pytest.mark.regression
def test_9():
    pass
@pytest.mark.regression
def test_10():
    pass

def test_11():
    pass

