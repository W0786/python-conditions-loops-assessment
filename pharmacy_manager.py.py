# ============================================
# Pharmacy Inventory and Daily Sales Manager
# Topic: Loop Structures (for loop, range(),
#        conditions inside loops, counters, accumulators)
# ============================================

print("=== Pharmacy Inventory and Sales Manager ===")
print()

# --------------------------------------------
# STEP 1: Ask how many medicines to process
# --------------------------------------------

# The loop keeps asking until the user enters a whole number greater than 0
while True:
    try:
        total_medicines = int(input("How many different medicines do you want to process? "))
        if total_medicines <= 0:
            print("Error: Please enter at least 1 medicine. Try again.")
        else:
            break
    except ValueError:
        # This runs if the user types letters or a decimal number
        print("Error: Please enter a whole number only. Try again.")

# --------------------------------------------
# STEP 2: Create the accumulator and counters
# --------------------------------------------

total_revenue = 0       # ACCUMULATOR: adds up the money from every successful sale
restock_count = 0       # COUNTER: how many medicines need restocking
successful_sales = 0    # COUNTER: how many sales were completed
rejected_sales = 0      # COUNTER: how many sales failed (not enough stock)

# --------------------------------------------
# STEP 3: Process each medicine using a for loop
# --------------------------------------------

# range(1, total_medicines + 1) gives us 1, 2, 3, ... up to total_medicines
for number in range(1, total_medicines + 1):
    print()
    print(f"--- Medicine {number} of {total_medicines} ---")

    # --- Medicine name ---
    while True:
        name = input("Enter medicine name: ").strip()  # strip() removes extra spaces
        if name == "":
            print("Error: Name cannot be empty. Try again.")
        else:
            break

    # --- Available stock (whole number, 0 or more) ---
    while True:
        try:
            stock = int(input("Enter available stock (units): "))
            if stock < 0:
                print("Error: Stock cannot be negative. Try again.")
            else:
                break
        except ValueError:
            print("Error: Please enter a whole number only. Try again.")

    # --- Price per unit (must be more than 0) ---
    while True:
        try:
            price = float(input("Enter price per unit (Rs.): "))
            if price <= 0:
                print("Error: Price must be greater than 0. Try again.")
            else:
                break
        except ValueError:
            print("Error: Please enter a number only. Try again.")

    # --- Quantity sold (whole number, 0 or more) ---
    while True:
        try:
            quantity_sold = int(input("Enter quantity sold (units): "))
            if quantity_sold < 0:
                print("Error: Quantity cannot be negative. Try again.")
            else:
                break
        except ValueError:
            print("Error: Please enter a whole number only. Try again.")

    # --------------------------------------------
    # STEP 4: Check if enough stock is available
    # --------------------------------------------

    if quantity_sold <= stock:
        # Enough stock, so the sale is successful
        sale_amount = quantity_sold * price
        remaining_stock = stock - quantity_sold
        total_revenue = total_revenue + sale_amount   # add this sale to the accumulator
        successful_sales = successful_sales + 1       # increase the counter by 1

        print(f"Sale successful! Sales amount: Rs. {sale_amount:.2f}")
    else:
        # Not enough stock, so the sale is rejected and stock stays the same
        remaining_stock = stock
        rejected_sales = rejected_sales + 1

        print(f"Sale rejected! Only {stock} units available, but {quantity_sold} requested.")

    print(f"Remaining stock of {name}: {remaining_stock} units")

    # --------------------------------------------
    # STEP 5: Low-stock warning
    # --------------------------------------------

    if remaining_stock < 10:
        print(f"WARNING: Low stock for {name}! Please restock.")
        restock_count = restock_count + 1   # count this medicine for restocking

# --------------------------------------------
# STEP 6: Show the final report
# --------------------------------------------

print()
print("=" * 45)
print("          FINAL PHARMACY REPORT")
print("=" * 45)
print("Total medicines processed    :", total_medicines)
print("Successful sales             :", successful_sales)
print("Rejected sales (low stock)   :", rejected_sales)
print(f"Total revenue                : Rs. {total_revenue:.2f}")
print("Medicines needing restocking :", restock_count)
print("=" * 45)
