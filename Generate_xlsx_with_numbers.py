import xlsxwriter

# Specify the number of rows, columns, and values
num_rows = 600
num_cols = 12
num_values = num_rows

# Create a new workbook and add a worksheet
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

# Add headers to the worksheet
headers = ['Field_' + str(i) for i in range(1, num_cols+1)]
for i, header in enumerate(headers):
    worksheet.write(0, i, header)

# Generate data for each column
for col in range(num_cols):
    data = [i+1 for i in range(num_values)]
    for row, value in enumerate(data):
        worksheet.write(row+1, col, value)

# Close the workbook
workbook.close()
print("File successfully created")