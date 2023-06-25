from decimal import Decimal
from typing import NamedTuple, Optional, Callable

from fuctions_implementation_strategy import Customer, LineItem, Order

Promotion = Callable[['Order'], Decimal]

promos: list[Promotion] = []


def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo


def best_promo(order: Order) -> Decimal:
    return max((promo(order) for promo in promos))


@promotion
def fidelity(order: Order) -> Decimal:
    rate = Decimal('0.075')
    if order.customer.fidelity >= 1000:
        return order.total() * rate
    return Decimal('0')


@promotion
def promo(order: Order) -> Decimal:
    discount = Decimal('0')
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal(0.20)
    return discount


@promotion
def promo(order: Order) -> Decimal:
    rate = Decimal('0.07')
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * rate
    return Decimal('0')


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, Decimal('.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5))]

# print(Order(joe, cart, fidelity_promo))
# print(Order(ann, cart, fidelity_promo))
#
banana_cart = [LineItem('banana', 30, Decimal('.5')),
               LineItem('apple', 10, Decimal('1.5'))]
# print('------')
# print(Order(joe, banana_cart, bulk_item_promo))
#
long_cart = [LineItem(str(item_code), 1, Decimal(1))
             for item_code in range(10)]
#
# print(Order(joe, long_cart, large_order_promo))


print(Order(ann, long_cart, best_promo))
print(Order(joe, long_cart, best_promo))
