import os,sys
sys.path.append("../Python_less/")
# import Lesson5
import pytest

print('this is master branch pyTEST')
print ('This branch is testing assignment from lesson 6')

from Lesson5 import MassiveP

def test_1_CanonicNum():
    assert CanonicNum(6) == 8
# def test_get_divisors(divisors_10):
#     assert dv.get_divisors(10) == divisors_10
132