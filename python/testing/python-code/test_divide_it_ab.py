from division_func import divide_it
from division_func import DIVISION_RESULTS
from nose.tools import assert_raises


def test_divide_it_ab():
    try:
        divide_it('a','b')
        assert False
    except TypeError:
        assert True



#    assert_raises(TypeError, divide_it, 'a', 'b')