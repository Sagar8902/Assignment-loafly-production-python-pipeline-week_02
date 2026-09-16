<<<<<<< HEAD
"""
QUESTION 4 - CONFIG-DRIVEN DESIGN

Goal:

Move all application settings into one config.py file so that
changing a setting changes the application behaviour without
editing the other modules.

Settings:
- CURRENCY         -> currency used for order totals
- DISCOUNT_PERCENT -> discount applied to orders
- INPUT_FILE       -> input CSV file path
- RETRY_COUNT      -> number of retry attempts


                 config.py
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   extract.py   transform.py   load.py
       │            │            │
   INPUT_FILE   DISCOUNT      CURRENCY
                PERCENT       RETRY_COUNT
=======
"""
QUESTION 4 - CONFIG-DRIVEN DESIGN

Goal:

Move all application settings into one config.py file so that
changing a setting changes the application behaviour without
editing the other modules.

Settings:
- CURRENCY         -> currency used for order totals
- DISCOUNT_PERCENT -> discount applied to orders
- INPUT_FILE       -> input CSV file path
- RETRY_COUNT      -> number of retry attempts


                 config.py
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   extract.py   transform.py   load.py
       │            │            │
   INPUT_FILE   DISCOUNT      CURRENCY
                PERCENT       RETRY_COUNT
>>>>>>> 5f67676 (Fix order loading retry and refresh pipeline log)
"""