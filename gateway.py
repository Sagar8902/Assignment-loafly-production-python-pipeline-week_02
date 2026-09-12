"""
gateway.py  -  Loafly's orders API client (provided, do not edit).

This stands in for a real third-party service you call to save an order.
Like any network call it is not reliable: it succeeds most of the time, but
sometimes raises ConnectionError because the service is busy. Your job in the
retry task is to call this safely, not to change it.
"""
import random


def save_to_orders_api(order_id, total):
    """Try to save one order to the (flaky) orders API.

    Succeeds about 70% of the time. The rest of the time it raises
    ConnectionError, as a real API would under load.
    """
    if random.random() < 0.7:
        return {"order_id": order_id, "status": "SAVED", "total": total}
    raise ConnectionError(f"orders API unavailable for order {order_id}")
