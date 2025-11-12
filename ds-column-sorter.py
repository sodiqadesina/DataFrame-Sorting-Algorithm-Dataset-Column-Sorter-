import pandas as pd

# Loading the dataset
def load_dataset(file_path):
    # Read the CSV file into a DataFrame and take only the first 100 rows
    return pd.read_csv(file_path).head(100)

# Function to check if a column is numeric
def is_numeric(column):
    return pd.to_numeric(column, errors='coerce').notnull().all()

# Quick Sort algorithm for numeric sorting
def quick_sort_numeric(arr, index):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][1]
    left = [x for x in arr if x[1] < pivot]
    middle = [x for x in arr if x[1] == pivot]
    right = [x for x in arr if x[1] > pivot]
    return quick_sort_numeric(left, index) + middle + quick_sort_numeric(right, index)

# Quick Sort algorithm for alphabetical sorting 
def quick_sort_alpha(arr, index):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][1].lower()
    left = [x for x in arr if x[1].lower() < pivot]
    middle = [x for x in arr if x[1].lower() == pivot]
    right = [x for x in arr if x[1].lower() > pivot]
    return quick_sort_alpha(left, index) + middle + quick_sort_alpha(right, index)

# Function to reorder the table based on the specified column
def reorder_table(data, column_name):
    # Check if the column exists in the dataset
    if column_name not in data.columns:
        print(f"Column '{column_name}' does not exist in the dataset.")
        return None
    
    # Extract index and values from the specified column
    indexed_values = list(zip(data.index, data[column_name].tolist()))

    # Check if the column is numeric or alphabetical
    if is_numeric(data[column_name]):
        print(f"Sorting '{column_name}' as numeric data.")
        sorted_indexed_values = quick_sort_numeric(indexed_values, column_name)
    else:
        print(f"Sorting '{column_name}' as alphabetical data.")
        sorted_indexed_values = quick_sort_alpha(indexed_values, column_name)
    
    # Extract the sorted indices
    sorted_indices = [x[0] for x in sorted_indexed_values]

    # Reorder the DataFrame based on the sorted indices
    sorted_data = data.loc[sorted_indices]

    return sorted_data

# File path to shopping_trends.csv 
file_path = r'C:\Users\sina\Desktop\Masters of Appplied Computing\CP 600 Practical Algorithm Design\shopping_trends.csv' 

# Load the dataset and take a sample of the first 100 rows
data = load_dataset(file_path)

# Input column name from the user
column_name = input("Enter the column name to sort by (e.g. 'Age', 'Customer ID', 'Size'): ")

# Reordering the table based on the specified column
sorted_data = reorder_table(data, column_name)

if sorted_data is not None:
    # Displaying sorted table
    print(f"Table sorted by column: {column_name}")
    print(sorted_data.head())  # Displaying the first few rows of the sorted table

    # Saving the sorted table to a new file
    output_file = f"sorted_by_{column_name}_sample.csv"
    sorted_data.to_csv(output_file, index=False)
    print(f"Sorted sample data has been saved to {output_file}")
