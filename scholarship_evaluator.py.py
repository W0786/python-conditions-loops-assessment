# ============================================
# University Scholarship Eligibility Checker
# Topic: Conditional Statements (if, elif, else)
# ============================================

print("=== University Scholarship Eligibility Checker ===")
print()

# --------------------------------------------
# STEP 1: Take input from the user + validate
# --------------------------------------------

# --- Student name ---
# The loop keeps asking until the user types a proper name
while True:
    name = input("Enter student name: ").strip()  # strip() removes extra spaces
    if name == "":
        print("Error: Name cannot be empty. Try again.")
    else:
        break  # name is OK, so stop the loop

# --- Academic marks (must be between 0 and 100) ---
while True:
    try:
        marks = float(input("Enter academic marks (%): "))
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100. Try again.")
        else:
            break
    except ValueError:
        # This runs if the user types letters instead of a number
        print("Error: Please enter a number only. Try again.")

# --- Attendance (must be between 0 and 100) ---
while True:
    try:
        attendance = float(input("Enter attendance percentage (%): "))
        if attendance < 0 or attendance > 100:
            print("Error: Attendance must be between 0 and 100. Try again.")
        else:
            break
    except ValueError:
        print("Error: Please enter a number only. Try again.")

# --- Monthly family income (cannot be negative) ---
while True:
    try:
        income = float(input("Enter monthly family income (Rs.): "))
        if income < 0:
            print("Error: Income cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Error: Please enter a number only. Try again.")

# --------------------------------------------
# STEP 2: Check eligibility conditions
# --------------------------------------------

# This list will store the reasons if the student is NOT eligible
reasons = []

# Condition 1: marks must be at least 80
if marks < 80:
    reasons.append("Marks are less than 80%.")

# Condition 2: attendance must be at least 85
if attendance < 85:
    reasons.append("Attendance is less than 85%.")

# Condition 3: income must be 50,000 or less
if income > 50000:
    reasons.append("Monthly family income is more than Rs. 50,000.")

# --------------------------------------------
# STEP 3: Decide the scholarship
# --------------------------------------------

# If the reasons list is empty, it means the student passed all conditions
if len(reasons) == 0:
    eligible = True
    if marks >= 90:
        scholarship = "Full Scholarship"
    elif marks >= 80:
        scholarship = "Partial Scholarship"
else:
    eligible = False
    scholarship = "No Scholarship"

# --------------------------------------------
# STEP 4: Show the final report
# --------------------------------------------

print()
print("=" * 45)
print("      SCHOLARSHIP EVALUATION REPORT")
print("=" * 45)
print("Student Name          :", name)
print("Academic Marks        :", marks, "%")
print("Attendance            :", attendance, "%")
print("Monthly Family Income : Rs.", income)
print("-" * 45)

if eligible:
    print("Status                : ELIGIBLE")
    print("Scholarship           :", scholarship)
else:
    print("Status                : NOT ELIGIBLE")
    print("Scholarship           :", scholarship)
    print("Reason(s):")
    for reason in reasons:
        print(" -", reason)

print("=" * 45)
