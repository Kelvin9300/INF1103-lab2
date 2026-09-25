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
        
def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            total = int(lines[0].strip())
            history_line = lines[1].strip()
            if history_line == "":
                history = []
            else:
                history = [int(x) for x in history_line.split(",")]
            return total, history
    except FileNotFoundError:
        return 0, []
    
def calculate_tax(amount):
    tax = amount * 0.10
    return tax
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total
def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
def save_inventory(total_units, history):
    with open("inventory.txt", "w") as file:
        file.write(f"{total_units}\n")
        history_strings = [str(x) for x in history]
        file.write(",".join(history_strings))
    
total_units, history = load_inventory()
failed_entries = 0

while True:
    fails, entry = get_valid_input()
    failed_entries += fails
    if entry == "quit":
        save_inventory(total_units, history)
        break
    
    total_units = process_delivery(total_units, entry)
    history.append(entry)
    tax = calculate_tax(entry)
    if total_units > 500:
        print(f"ALERT: Inventory exceeds 500 units! Total is {total_units}. Stopping.")
        save_inventory(total_units, history)
        break

    else:
        print(f"Accepted {entry} units. Tax: {tax:.2f}. Running total: {total_units}")

generate_report(total_units, failed_entries)