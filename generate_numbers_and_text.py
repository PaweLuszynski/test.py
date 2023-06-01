import random
import xlsxwriter

# Specify the number of columns and calculate the number of rows
num_cols = 3
num_rows = 200

# Calculate the number of text and numerical columns
num_text_cols = num_cols // 2
num_numeric_cols = num_cols - num_text_cols

# Create a new workbook and add a worksheet
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

# Add headers to the worksheet
headers = ['Field_' + str(i) for i in range(1, num_cols + 1)]
for col, header in enumerate(headers):
    worksheet.write(0, col, header)

# Generate data for each column
for col in range(num_cols):
    start_value = 1 if col >= num_text_cols else col * num_rows + 1
    end_value = start_value + num_rows - 1

    # Generate data based on column type (text or numerical)
    if col < num_text_cols:
        # Generate random text values
        data = [random.choice(['Apple', 'Banana', 'Orange', 'Grapes']) for _ in range(num_rows)]
    else:
        # Generate numerical values in ascending order
        data = list(range(start_value, end_value + 1))

    # Write the data to the worksheet
    for row, value in enumerate(data):
        worksheet.write(row + 1, col, value)

# Close the workbook
workbook.close()
print("File successfully created")