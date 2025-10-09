import csv

filename = input("Enter CSV file name: ")
with open(filename, newline='') as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        for col_index, cell in enumerate(row):
            if "ai" in cell.lower():
                print(f"'ai' found at Row {row_index+1}, Column {col_index+1}")