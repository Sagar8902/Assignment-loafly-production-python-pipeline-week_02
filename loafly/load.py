<<<<<<< HEAD
# Load orders with retry.

import logging
import time

import gateway

from loafly.config import (
    CURRENCY,
    RETRY_COUNT,
    RETRY_WAIT_SECONDS
)


logger = logging.getLogger(__name__)


def load_orders(orders, api_key):
    """Save orders to the API with retry."""
    for order in orders:
        logger.info(
            "Saving order %s for %s, total %s %.2f",
            order.order_id,
            order.customer,
            CURRENCY,
            order.discounted_total
        )

        for attempt in range(1, RETRY_COUNT + 1):
            try:
                gateway.save_to_orders_api(order, api_key)

                logger.info(
                    "Order %s saved successfully on attempt %s",
                    order.order_id,
                    attempt
                )

                break

            except Exception as error:
                logger.warning(
                    "Attempt %s/%s failed for order %s: %s",
                    attempt,
                    RETRY_COUNT,
                    order.order_id,
                    error
                )

                if attempt < RETRY_COUNT:
                    logger.info(
                        "Waiting %s second before retrying order %s",
                        RETRY_WAIT_SECONDS,
                        order.order_id
                    )

                    time.sleep(RETRY_WAIT_SECONDS)

                else:
                    logger.error(
                        "Failed to save order %s after %s attempts",
                        order.order_id,
                        RETRY_COUNT
=======
# Load orders with retry.

import logging
import time

import gateway

from loafly.config import (
    CURRENCY,
    RETRY_COUNT,
    RETRY_WAIT_SECONDS
)


logger = logging.getLogger(__name__)


def load_orders(orders, api_key):
    """Save orders to the API with retry."""

    for order in orders:
        logger.info(
            "Saving order %s for %s, total %s %.2f",
            order.order_id,
            order.customer,
            CURRENCY,
            order.discounted_total
        )

        for attempt in range(1, RETRY_COUNT + 1):
            try:
                gateway.save_to_orders_api(
                    order.order_id,
                    order.discounted_total
                )

                logger.info(
                    "Order %s saved successfully on attempt %s",
                    order.order_id,
                    attempt
                )

                break

            except ConnectionError as error:
                logger.warning(
                    "Attempt %s/%s failed for order %s: %s",
                    attempt,
                    RETRY_COUNT,
                    order.order_id,
                    error
                )

                if attempt < RETRY_COUNT:
                    logger.info(
                        "Waiting %s second before retrying order %s",
                        RETRY_WAIT_SECONDS,
                        order.order_id
                    )

                    time.sleep(RETRY_WAIT_SECONDS)

                else:
                    logger.error(
                        "Failed to save order %s after %s attempts",
                        order.order_id,
                        RETRY_COUNT
>>>>>>> 5f67676 (Fix order loading retry and refresh pipeline log)
                    )