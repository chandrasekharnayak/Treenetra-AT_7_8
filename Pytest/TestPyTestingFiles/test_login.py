from TREENETRA_AT_7_8.Pytest.SouceCode import login
# def test_add():
#     assert login.addition(2,3) == 6

import pytest
#Positive Senario for addition

def test_addition_positive():
    attempt_1 = login.addition(2,3)
    assert attempt_1 == 5
    attempt_2 = login.addition(-2, -3)
    assert attempt_2 == -5
    attempt_3 = login.addition(0, 0)
    assert attempt_3 == 0
    attempt_4 = login.addition(-1, 1)
    assert attempt_4 == 0

#Positive Senario for multiplication
def test_multiplication_positive():
    attempt_1 = login.multiplication(2,3)
    assert attempt_1 == 6
    attempt_2 = login.multiplication(-2, -3)
    assert attempt_2 == 6
    attempt_3 = login.multiplication(0, 0)
    assert attempt_3 == 0
    attempt_4 = login.multiplication(-1, 1)
    assert attempt_4 == -1

#Negetive Senario for addition

@pytest.mark.xfail(reason='need to pass')
def test_addition_negetive():
    attempt_1 = login.addition(2,3)
    assert attempt_1 == -1
    attempt_2 = login.addition(-2, -3)
    assert attempt_2 == -5
    attempt_3 = login.addition(0, 0)
    assert attempt_3 == 0.0
    attempt_4 = login.addition(-1, 1)
    assert attempt_4 == 1

#Negetive Senario for addition
@pytest.mark.xfail(reason='need to pass')
def test_multiplication_negetive():
    attempt_1 = login.multiplication(2,3)
    assert attempt_1 == 5
    attempt_2 = login.multiplication(-2, -3)
    assert attempt_2 == -5
    attempt_3 = login.multiplication(0, 0)
    assert attempt_3 == 0.0
    attempt_4 = login.multiplication(-1, 1)
    assert attempt_4 == 11