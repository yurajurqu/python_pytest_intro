import pytest

from checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('a',1)
    checkout.addItemPrice('b', 7)
    return checkout
def test_canCalculateTotal(checkout):
    checkout.addItem('a')
    assert checkout.calculateTotal() == 1
def test_getCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 8
    
def test_canAddDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    
# @pytest.mark.skip
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 5

def test_throwExceptionWhenAddingItemWithoutPrice(checkout):
    with pytest.raises(Exception):    
        checkout.addItem('z')