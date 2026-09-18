def get_valid_input():
    while True:
        entry = input("Enter stock quantity (or 'quit' to finish): ")
        if entry == "quit":
            return "quit"
        is_negative = entry.startswith("-") and entry[1:].isdigit()
        if is_negative:
            print("Error: negative numbers are not allowed")
        elif not entry.isdigit():
            print("Error: please enter a valid number")
        else:
            return int(entry)
def calculate_tax(amount):
    tax = amount * 0.10
    return tax
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total
def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    
total_units = 0
failed_entries = 0

while True:
    entry = input("Enter stock quantity (or 'quit' to finish): ")
    if entry == "quit":
        break
    # more logic goes here
    is_negative = entry.startswith("-") and entry[1:].isdigit()

    if is_negative:
        print("Error: negative numbers are not allowed")
        failed_entries += 1
        continue
    elif not entry.isdigit():
        print("Error: please enter a valid number")
        failed_entries += 1
        continue

    quantity = int(entry)
    total_units += quantity
    if total_units > 500:
        print(f"ALERT: Inventory exceeds 500 units! Total is {total_units}. Stopping.")
        break
    else:
        print(f"Accepted {quantity} units. Running total: {total_units}")

print(f"Total Units Processed: {total_units}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")