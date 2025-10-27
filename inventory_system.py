"""
Inventory Management System.
Uses a global dictionary to track stock data.
"""
import json
from datetime import datetime
# Removed unused 'logging' import


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Adds a quantity of an item to the stock_data.
    Fixes: Mutable default argument, uses f-strings, and adds input validation.
    """
    if logs is None:
        logs = []

    if not item:
        return

    if not isinstance(qty, int):
        return

    stock_data[item] = stock_data.get(item, 0) + qty

    logs.append(
        f"{datetime.now()}: Added {qty} of {item}"
    )


def remove_item(item, qty):
    """
    Removes a quantity of an item from the stock_data.
    Fixes: Overly broad exception.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Returns the quantity of an item, defaulting to 0 if not found."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Loads stock data from a JSON file."""
    # Pylint W0603: Using the global statement (required to modify global dict)
    global stock_data
    try:
        with open(file, "r", encoding='utf-8') as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        pass


def save_data(file="inventory.json"):
    """Saves stock data to a JSON file."""
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(stock_data))


def print_data():
    """Prints a report of all items and their quantities."""
    print("Items Report")
    for i, qty in stock_data.items():
        print(i, "->", qty)


def check_low_items(threshold=5):
    """
    Checks and returns a list of items below the specified stock threshold.
    """
    result = []
    for i, qty in stock_data.items():
        if qty < threshold:
            result.append(i)
    return result


def main():
    """Main execution block demonstrating usage."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # Removed dangerous eval() function


main()
# <-- ENSURE there is one single blank line after the main() call.