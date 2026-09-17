# Run the Extract -> Transform -> Load pipeline.

import logging
import os

from dotenv import load_dotenv

from loafly.config import LOG_FILE
from loafly.extract import extract_orders
from loafly.transform import transform_orders
from loafly.load import load_orders


# Load environment variables from .env
load_dotenv()


# Configure logging for the whole application.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Loafly pipeline started")

    # Read the API key from the environment.
    api_key = os.getenv("LOAFLY_API_KEY")

    if not api_key:
        logger.error("LOAFLY_API_KEY is not set")
        raise RuntimeError("LOAFLY_API_KEY is required")

    try:
        # 1. EXTRACT
        raw_orders = extract_orders()

        # 2. TRANSFORM
        orders = transform_orders(raw_orders)

        # 3. LOAD
        load_orders(orders, api_key)

        logger.info("Loafly pipeline completed successfully")

    except Exception:
        logger.error(
            "Loafly pipeline failed",
            exc_info=True
        )
        raise


if __name__ == "__main__":
    main()