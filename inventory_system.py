import json
import logging
from datetime import datetime
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid types: item must be str, qty must be int")
        return

    if qty < 0:
        logging.warning("Negative quantity not allowed for %s", item)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item, qty):
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
            logging.info("Removed %d of %s", qty, item)
        else:
            logging.warning("Tried to remove non-existent item: %s", item)
    except KeyError as e:
        logging.error("KeyError while removing %s: %s", item, e)
    except TypeError as e:
        logging.error("Invalid quantity type for %s: %s", item, e)


def get_qty(item):
    return stock_data.get(item, 0)


def load_data(filename="inventory.json"):
    global stock_data
    try:
        with open(filename, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
            logging.info("Loaded inventory from %s", filename)
    except FileNotFoundError:
        logging.warning("File not found: %s", filename)
        stock_data = {}
    except json.JSONDecodeError as e:
        logging.error("Invalid JSON format: %s", e)


def save_data(filename="inventory.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
            logging.info("Saved inventory to %s", filename)
    except OSError as e:
        logging.error("Failed to save data: %s", e)


def print_data():
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 1)
    remove_item("apple", 3)
    remove_item("grape", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    logging.info("Program executed successfully.")
if __name__ == "__main__":
    main()
