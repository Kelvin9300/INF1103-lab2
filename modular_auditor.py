def get_valid_input():
    fail_count = 0
    while True:
        entry = input("Enter stock quantity (or 'quit' to finish): ")
        if entry == "quit":
            return fail_count, "quit"
        is_negative = entry.startswith("-") and entry[1:].isdigit()
        if is_negative:
            print("Error: negative numbers are not allowed")
            fail_count += 1
        elif not entry.isdigit():
            print("Error: please enter a valid number")
            fail_count += 1
        else:
            return fail_count, int(entry)
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
    fails, entry = get_valid_input()
    failed_entries += fails
    if entry == "quit":
        break
    total_units = process_delivery(total_units, entry)
    tax = calculate_tax(entry)
    if total_units > 500:
        print(f"ALERT: Inventory exceeds 500 units! Total is {total_units}. Stopping.")
        break
    else:
        print(f"Accepted {entry} units. Tax: {tax:.2f}. Running total: {total_units}")

generate_report(total_units, failed_entries)