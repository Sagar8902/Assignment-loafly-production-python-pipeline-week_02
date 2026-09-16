<<<<<<< HEAD
"""
QUESTION 3 - MODULES AND PACKAGES

Goal:
Split the Loafly script into a clean package where each module
has one responsibility.

Modules:
- config.py     -> application settings
- models.py     -> Order class
- extract.py    -> read and group raw orders
- transform.py  -> clean and transform orders
- load.py       -> save processed orders
- __init__.py   -> makes loafly a Python package

run_pipeline.py:
Orchestrates the pipeline in this order:

    Extract -> Transform -> Load

Acceptance Criteria:
- loafly package contains __init__.py
- Each module has one clear responsibility
- run_pipeline.py imports the required modules
- Pipeline runs in Extract -> Transform -> Load order
=======
"""
QUESTION 3 - MODULES AND PACKAGES

Goal:
Split the Loafly script into a clean package where each module
has one responsibility.

Modules:
- config.py     -> application settings
- models.py     -> Order class
- extract.py    -> read and group raw orders
- transform.py  -> clean and transform orders
- load.py       -> save processed orders
- __init__.py   -> makes loafly a Python package

run_pipeline.py:
Orchestrates the pipeline in this order:

    Extract -> Transform -> Load

Acceptance Criteria:
- loafly package contains __init__.py
- Each module has one clear responsibility
- run_pipeline.py imports the required modules
- Pipeline runs in Extract -> Transform -> Load order
>>>>>>> 5f67676 (Fix order loading retry and refresh pipeline log)
"""