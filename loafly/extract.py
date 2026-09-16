<<<<<<< HEAD
# Extract orders from the input CSV.

import csv
import logging

from loafly.config import INPUT_FILE


logger = logging.getLogger(__name__)


def extract_orders():
    """Read and group orders from the input CSV."""
    logger.info("Starting order extraction from %s", INPUT_FILE)

    rows = []

    try:
        with open(INPUT_FILE, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                rows.append(row)

    except FileNotFoundError:
        logger.error("Input file not found: %s", INPUT_FILE)
        raise

    orders = {}

    for row in rows:
        order_id = row["order_id"]

        if order_id not in orders:
            orders[order_id] = {
                "customer": row["customer"],
                "items": []
            }

        orders[order_id]["items"].append(
            (row["item_name"], row["item_price"])
        )

    logger.info("Successfully extracted %s orders", len(orders))

    return orders
=======
# Extract orders from the input CSV.

import csv
import logging

from loafly.config import INPUT_FILE


logger = logging.getLogger(__name__)


def extract_orders():
    """Read and group orders from the input CSV."""
    logger.info("Starting order extraction from %s", INPUT_FILE)

    rows = []

    try:
        with open(INPUT_FILE, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                rows.append(row)

    except FileNotFoundError:
        logger.error("Input file not found: %s", INPUT_FILE)
        raise

    orders = {}

    for row in rows:
        order_id = row["order_id"]

        if order_id not in orders:
            orders[order_id] = {
                "customer": row["customer"],
                "items": []
            }

        orders[order_id]["items"].append(
            (row["item_name"], row["item_price"])
        )

    logger.info("Successfully extracted %s orders", len(orders))

    return orders
>>>>>>> 5f67676 (Fix order loading retry and refresh pipeline log)
