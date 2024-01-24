from TREENETRA_AT_7_8.Pytest.SouceCode import login
import pytest

#Positive Senario for addition
@pytest.mark.parametrize('input_a,input_b,excepeted_result',[
    (2,3,5),(0,0,0),(-2,-3,-5),(-9,8,-1),(-8,9,1),(1,1,2)
])
def test_addition_positive(input_a,input_b,excepeted_result):
    result = login.addition(input_a,input_b)
    assert result == excepeted_result

#Negetive Senario for addition
@pytest.mark.xfail
@pytest.mark.parametrize('input_a,input_b,excepeted_result',[
    (2,3,7),(0,0,1),(-2,-3,5),(-9,8,111),(-8,9,1)
])
def test_addition_negetive(input_a,input_b,excepeted_result):
    result = login.addition(input_a,input_b)
    assert result == excepeted_result