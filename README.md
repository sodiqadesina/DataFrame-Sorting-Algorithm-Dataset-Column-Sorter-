# 📊 Dataset Column Sorter using Custom QuickSort

This repository implements a **custom data-sorting algorithm** capable of reordering any tabular dataset by a specified column — **without relying on built-in sorting functions** like `sort()`, `sorted()`, or Pandas `.sort_values()`.  
The solution demonstrates **algorithmic thinking applied to data analytics**.

---

## 🧠 Problem Overview

We have been provided with a retail dataset - [Customer Shopping Trends Dataset (Kaggle)](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset) — containing 19 columns with mixed data types (numeric, categorical, and text).  
The task is to:

> “Write a program that sorts the entire dataset based on any column specified by the user.”

Example:  
If the user inputs **"Age"**, the output should be the dataset reordered by customer ages (ascending).

---

## ⚙️ Implementation Highlights

- Implemented **Quick Sort** from scratch for both numeric and alphabetical data.
- Detects whether a column is **numeric** or **textual** before sorting.
- Handles any column dynamically via user input.
- Saves results as a new CSV file (e.g., `sorted_by_Age_sample.csv`).
- Uses Pandas only for **data loading and storage**, not for sorting.

---

## 🧩 Algorithm Logic

### 1️⃣ Column Type Detection
The algorithm checks if the column can be safely converted to numeric values:
```python
def is_numeric(column):
    return pd.to_numeric(column, errors='coerce').notnull().all()
```
### 2️⃣ Custom Quick Sort

For numeric columns:
```python
def quick_sort_numeric(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][1]
    left = [x for x in arr if x[1] < pivot]
    middle = [x for x in arr if x[1] == pivot]
    right = [x for x in arr if x[1] > pivot]
    return quick_sort_numeric(left) + middle + quick_sort_numeric(right)
```
For textual columns, case-insensitive comparison is used:
```python
def quick_sort_alpha(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][1].lower()
    left = [x for x in arr if x[1].lower() < pivot]
    middle = [x for x in arr if x[1].lower() == pivot]
    right = [x for x in arr if x[1].lower() > pivot]
    return quick_sort_alpha(left) + middle + quick_sort_alpha(right)
```
### 📂 Usage Instructions

🧰 Prerequisites

Python 3.12+

pandas library

Install dependencies:
```bash
pip install pandas
```
```bash
python ds-column-sorter.py
```
Sample Input:
```bash
Enter the column name to sort by (e.g. 'Age', 'Customer ID', 'Size'): Age
```
Sample Output:
```bash
Sorting 'Age' as numeric data.
Table sorted by column: Age
Sorted sample data has been saved to sorted_by_Age_sample.csv
```
### 💡 Example Results
| Input Column  | Detected Type | Output File                        | Sorting Basis      |
| ------------- | ------------- | ---------------------------------- | ------------------ |
| `Age`         | Numeric       | `sorted_by_Age_sample.csv`         | Ascending values   |
| `Size`        | Categorical   | `sorted_by_Size_sample.csv`        | Alphabetical order |
| `Customer ID` | Numeric       | `sorted_by_Customer ID_sample.csv` | Ascending IDs      |

### ⏱️ Performance Notes
| Dataset               | Rows     | Sorting Type | Avg Time (s) |
| --------------------- | -------- | ------------ | ------------ |
| `shopping_trends.csv` | 100 rows | Numeric      | ~0.04        |
| `shopping_trends.csv` | 100 rows | Alphabetical | ~0.06        |

### 🧩 Key Learnings

Algorithm adaptability: Quick Sort logic can be reused for various data types.

Dynamic column handling: Automatically distinguishes between numeric and text fields.

Real-world data relevance: Bridges the gap between algorithm design and analytics tasks.

### 🧰 Tools & Environment

Language: Python 3.12

Library: pandas (for data I/O only)

Dataset: Customer Shopping Trends Dataset (Kaggle)

Platform: Windows 11 / VS Code

### 🏁 Future Enhancements

Add descending order toggle

Integrate Merge Sort and Heap Sort for comparison

Add benchmark visualizations

Extend to handle multi-column sorting
