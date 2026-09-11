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