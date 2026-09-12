# 🥐 Loafly Production Python

A production-ready Python order processing project created by refactoring Loafly's legacy order-processing script.

This project demonstrates how to transform a simple Python script into a clean, modular, configurable, and robust Python application using the Python standard library.

---

## 📌 Project Overview

Loafly is an online artisan bakery that processes customer orders.

The original legacy script had several problems:

- All logic was written in one Python file.
- Price cleaning was mixed with business logic.
- The discount percentage was hard-coded.
- There was no proper modular structure.
- There was no logging.
- Missing prices could stop the entire pipeline.
- There was no retry mechanism for failed saves.
- The API key was hard-coded in the source code.

This project refactors the legacy script step by step into a more production-ready Python framework.

---

## 🎯 Assignment Objectives

The project covers six main improvements:

1. Create reusable functions.
2. Create an `Order` class using OOP.
3. Organize the application into modules and packages.
4. Move application settings into a central configuration file.
5. Add logging and exception handling.
6. Add retry logic and secure environment-based API keys.

---

# 📂 Project Structure

```text
loafly-production-python/
│
├── .venv/                         # Python virtual environment
│
├── data/                          # Project data files
│
├── loafly/                        # Main Python package
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── starter/                       # Starter/reference files
│
├── .env                           # Local environment variables
├── .env.example                   # Example environment variables
├── .gitignore                     # Git ignore rules
│
├── gateway.py                     # Order saving service/gateway
├── legacy_orders.py               # Original legacy script
│
├── Q-1_Functions.py               # Question 1 - Functions
├── Q-2_OOP.py                     # Question 2 - Order class
├── Q-3_Modules_Packages.py        # Question 3 - Modules & Packages
├── Q-4_Config_driven_design.py    # Question 4 - Configuration
├── Q-5_Logging_and_Exception.py   # Question 5 - Logging & Exceptions
├── Q-6_Retry_and_secrets.py       # Question 6 - Retry & Secrets
│
├── raw_orders.csv                 # Raw order input data
├── loafly.log                     # Application log file
├── requirements.txt               # Project dependencies
├── run_pipeline.py                # Main pipeline runner
└── README.md                      # Project documentation

## Setup

Create a virtual environment:

```bash
python -m venv .venv


## Activate virtual environment
.venv\Scripts\activate
