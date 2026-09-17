# Transform and clean orders.

import logging

from loafly.config import DISCOUNT_PERCENT
from loafly.models import Order


logger = logging.getLogger(__name__)


def clean_price(text):
    """Clean a price and convert it to a float."""
    return float(text.replace(",", "").strip())


def apply_discount(price, percent):
    """Apply the given discount percentage."""
    discount = price * percent / 100
    return price - discount


def transform_orders(raw_orders):
    """Clean prices and create Order objects."""
    orders = []

    for order_id, data in raw_orders.items():
        order = Order(order_id, data["customer"])

        for item_name, price in data["items"]:
            try:
                cleaned_price = clean_price(price)
                order.add_item(item_name, cleaned_price)

            except (ValueError, AttributeError):
                logger.warning(
                    "Skipping item '%s' in order %s: "
                    "missing or invalid price",
                    item_name,
                    order_id
                )

            finally:
                logger.info(
                    "Finished processing price for item '%s' "
                    "in order %s",
                    item_name,
                    order_id
                )

        discounted_total = apply_discount(
            order.total(),
            DISCOUNT_PERCENT
        )

        order.discounted_total = discounted_total
        orders.append(order)

        logger.info(
            "Order %s transformed successfully. Total: %.2f",
            order_id,
            discounted_total
        )

    return orders