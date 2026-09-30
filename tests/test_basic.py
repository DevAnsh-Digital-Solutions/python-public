import pytest

from ci_fixture.add import add
from ci_fixture.cart import Cart
from ci_fixture.format_currency import format_currency
from ci_fixture.multiply import multiply


def test_add_adds_two_numbers():
    assert add(2, 2) == 4


def test_multiply_multiplies_two_numbers():
    assert multiply(3, 4) == 12


def test_format_currency_formats_a_positive_amount():
    assert format_currency(9.5) == "$9.50"
    assert format_currency(1234567.891) == "$1,234,567.89"


def test_cart_subtotal_and_total():
    cart = Cart()
    cart.add_item(10.0, 2)
    cart.add_item(5.0)
    assert cart.subtotal() == 25.0
    assert cart.total(discount_pct=20) == 20.0


def test_cart_rejects_bad_input():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_item(1.0, 0)
    with pytest.raises(ValueError):
        cart.total(discount_pct=101)
