from ipynotifyer import notifyOnComplete as nf
from nose.tools import assert_equal, assert_raises


def notifyOnComplete_test1():

    @nf()
    def division(a, b):
        """returns some text"""
        return a / b

    assert_equal(division(1, 1), 1)

    assert_raises(Exception, division, 1, 0)

    @nf(timer=True)
    def division2(a, b):
        """returns some text"""
        return a / b

    assert_equal(division2(10, 5), 2)
