"""
QUESTION 1 - FUNCTIONS

Goal:

Replace inline price cleaning with a reusable clean_price() function
and move the discount calculation into an apply_discount() function.

The functions should:
- Clean prices like '1,120' and convert them to a number.
- Apply the given discount percentage.
- Remove repeated logic and magic numbers from the main code.
"""


# Clean a price like '1,120' and convert it to a number.
def clean_price(text):
    return float(text.replace(",", "").strip())


# Apply the given discount percentage and return the final price.
def apply_discount(price, percent):
    discount = price * percent / 100
    return price - discount


# Test the functions.
print(clean_price("1,120"))
print(apply_discount(100, 18))