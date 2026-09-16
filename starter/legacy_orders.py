"""
legacy_orders.py  -  Loafly's "it ran fine on my laptop" script.

This is the BEFORE. It works for the happy rows, but look at the problems:
  - the price cleaning is copy-pasted inline
  - the discount is a magic number typed into the logic
  - the API key is sitting right here in the code
  - it uses print(), has no error handling, and no retry
  - everything lives in one file

It also crashes the first time it meets an order with a missing price,
which is exactly the kind of 2am breakage this session is about.

Run:  python legacy_orders.py
"""
import csv

# read today's raw orders
rows = []
with open("raw_orders.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append(row)

# group the item rows into orders
orders = {}
for row in rows:
    oid = row["order_id"]
    if oid not in orders:
        orders[oid] = {"customer": row["customer"], "items": []}
    orders[oid]["items"].append((row["item_name"], row["item_price"]))

# process every order
for oid, o in orders.items():
    total = 0
    for name, price in o["items"]:
        total = total + float(price.replace(",", ""))   # cleaning, copy-pasted inline
    total = total - total * 10 / 100                     # discount, magic number
    api_key = "loafly-prod-key-9f3a21"                   # secret, sitting in the code (!)
    print("saving order", oid, "for", o["customer"], "total", total)   # no logging, no retry
