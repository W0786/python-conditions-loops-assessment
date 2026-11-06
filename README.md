# 🐍 Python Beginner Projects

A collection of two practical Python console applications that demonstrate core programming concepts, conditional logic and loop structures, through real-world scenarios.

| # | Project | File | Core Topic |
|---|---------|------|------------|
| 1 | University Scholarship Eligibility Checker | `scholarship_evaluator.py` | Conditional Statements (`if`, `elif`, `else`) |
| 2 | Pharmacy Inventory and Daily Sales Manager | `pharmacy_manager.py` | Loop Structures (`for`, `range()`, counters, accumulators) |

---

## 📌 Project Introduction and Overview

These projects were built as beginner-level exercises to reinforce fundamental Python concepts. Both programs:

- Run entirely in the command line (terminal).
- Collect user input and apply **input validation**, re-prompting until a valid value is entered.
- Produce a clean, well-formatted **final report**.
- Use only Python's standard built-in features, so no external libraries are required.

---

## 🎓 Program 1: University Scholarship Eligibility Checker

**File:** `scholarship_evaluator.py`

### Overview

This program determines whether a student qualifies for a university scholarship and, if so, which type of scholarship is awarded.

### Eligibility Criteria

A student must satisfy **all three** conditions to be eligible:

| Criterion | Requirement |
|-----------|-------------|
| Academic Marks | At least **80%** |
| Attendance | At least **85%** |
| Monthly Family Income | **Rs. 50,000 or less** |

### Scholarship Categories

| Condition | Outcome |
|-----------|---------|
| Eligible with marks of 90% or above | **Full Scholarship** |
| Eligible with marks from 80% to 89.99% | **Partial Scholarship** |
| Any criterion not met | **No Scholarship** (with the reason(s) listed) |

### Program Flow

1. Collects the student's name, marks, attendance and family income, validating each entry.
2. Evaluates all three eligibility criteria and records the reason for every criterion that fails.
3. If no reasons are recorded, the student is eligible and the scholarship type is determined by marks.
4. Prints a formatted evaluation report.

---

## 💊 Program 2: Pharmacy Inventory and Daily Sales Manager

**File:** `pharmacy_manager.py`

### Overview

This program manages a pharmacy's daily sales and stock levels. The user specifies how many medicines to process, then enters the details for each one.

### Input Per Medicine

- Medicine name
- Available stock (units)
- Price per unit (Rs.)
- Quantity sold (units)

### Business Logic

- **Successful sale:** If `quantity_sold <= stock`, the sale is completed, revenue increases and stock is reduced.
- **Rejected sale:** If the requested quantity exceeds available stock, the sale is rejected and stock remains unchanged.
- **Low-stock warning:** If remaining stock falls **below 10 units**, a restock warning is displayed.

### Final Report Includes

- Total medicines processed
- Number of successful sales
- Number of rejected sales
- Total revenue
- Number of medicines requiring restocking

---

## 🧠 Python Concepts Covered

### Program 1: Scholarship Evaluator

- User input and output with `input()` and `print()`
- Type conversion with `float()`
- Conditional statements: `if`, `elif`, `else`
- Comparison operators: `<`, `>`, `>=`, `==`
- Logical operator: `or`
- `while True` loops with `break` for input validation
- Exception handling with `try` / `except ValueError`
- Lists: `append()` and `len()`
- Iterating over a list with a `for` loop
- String method: `strip()`
- Boolean variables (`eligible = True / False`)

### Program 2: Pharmacy Manager

- `for` loops with `range()`
- Counters and accumulators (`total_revenue`, `successful_sales`, `rejected_sales`, `restock_count`)
- Conditional logic inside loops (`if` / `else`)
- Nested loops (`while` validation loops inside a `for` loop)
- Type conversion with `int()` and `float()`
- Exception handling with `try` / `except ValueError`
- f-strings and number formatting (`:.2f`)
- Arithmetic operators (`*`, `-`, `+`)
- String method: `strip()`

---

## ▶️ How to Run

### Requirements

- Python **3.6 or later** (required for f-string support)
- Download Python from <https://www.python.org/downloads/>

To verify your installation:

```bash
python --version
```

### Steps

1. Clone the repository (or download the files):

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Run the **Scholarship Evaluator**:

   ```bash
   python scholarship_evaluator.py
   ```

3. Run the **Pharmacy Manager**:

   ```bash
   python pharmacy_manager.py
   ```

> 💡 If `python` is not recognized, try `python3` instead.

---

## 🖥️ Sample Input / Output

### Program 1: Scholarship Evaluator

**Example A: Eligible student**

```text
=== University Scholarship Eligibility Checker ===

Enter student name: Ali Khan
Enter academic marks (%): 92
Enter attendance percentage (%): 90
Enter monthly family income (Rs.): 40000

=============================================
      SCHOLARSHIP EVALUATION REPORT
=============================================
Student Name          : Ali Khan
Academic Marks        : 92.0 %
Attendance            : 90.0 %
Monthly Family Income : Rs. 40000.0
---------------------------------------------
Status                : ELIGIBLE
Scholarship           : Full Scholarship
=============================================
```

**Example B: Ineligible student**

```text
=== University Scholarship Eligibility Checker ===

Enter student name: Sara Ahmed
Enter academic marks (%): 75
Enter attendance percentage (%): 80
Enter monthly family income (Rs.): 60000

=============================================
      SCHOLARSHIP EVALUATION REPORT
=============================================
Student Name          : Sara Ahmed
Academic Marks        : 75.0 %
Attendance            : 80.0 %
Monthly Family Income : Rs. 60000.0
---------------------------------------------
Status                : NOT ELIGIBLE
Scholarship           : No Scholarship
Reason(s):
 - Marks are less than 80%.
 - Attendance is less than 85%.
 - Monthly family income is more than Rs. 50,000.
=============================================
```

**Example C: Input validation**

```text
Enter academic marks (%): abc
Error: Please enter a number only. Try again.
Enter academic marks (%): 150
Error: Marks must be between 0 and 100. Try again.
Enter academic marks (%): 85
```

---

### Program 2: Pharmacy Manager

```text
=== Pharmacy Inventory and Sales Manager ===

How many different medicines do you want to process? 3

--- Medicine 1 of 3 ---
Enter medicine name: Panadol
Enter available stock (units): 50
Enter price per unit (Rs.): 10
Enter quantity sold (units): 20
Sale successful! Sales amount: Rs. 200.00
Remaining stock of Panadol: 30 units

--- Medicine 2 of 3 ---
Enter medicine name: Brufen
Enter available stock (units): 15
Enter price per unit (Rs.): 25.5
Enter quantity sold (units): 20
Sale rejected! Only 15 units available, but 20 requested.
Remaining stock of Brufen: 15 units

--- Medicine 3 of 3 ---
Enter medicine name: Amoxil
Enter available stock (units): 12
Enter price per unit (Rs.): 40
Enter quantity sold (units): 5
Sale successful! Sales amount: Rs. 200.00
Remaining stock of Amoxil: 7 units
WARNING: Low stock for Amoxil! Please restock.

=============================================
          FINAL PHARMACY REPORT
=============================================
Total medicines processed    : 3
Successful sales             : 2
Rejected sales (low stock)   : 1
Total revenue                : Rs. 400.00
Medicines needing restocking : 1
=============================================
```

---

## 📁 Project Structure

```text
.
├── scholarship_evaluator.py
├── pharmacy_manager.py
└── README.md
```

---

## 🚀 Future Improvements

- Save reports to a file (CSV or TXT)
- Support batch processing of multiple students or medicines
- Refactor the code into reusable functions for better modularity
- Build a GUI or web-based version

---

## 👤 Author

**<Your Name>**
GitHub: [@<your-username>](https://github.com/<your-username>)

---

⭐ If you find these projects helpful, consider giving the repository a star!
