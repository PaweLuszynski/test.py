import random
import datetime
import xlsxwriter
import string

# Specify the number of rows and columns
num_rows = 100000
num_cols = 10

# List of fruits for the list column and header column
fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Strawberry', 'Grapes', 'Watermelon', 'Pineapple', 'Kiwi', 'Peach', 'Pear', 'Cherry', 'Plum', 'Blueberry', 'Raspberry', 'Lemon', 'Lime', 'Coconut', 'Avocado', 'Pomegranate']

# List of car manufacturers for the URL column
car_manufacturers = ['Toyota', 'Ford', 'Chevrolet', 'Volkswagen', 'BMW', 'Mercedes-Benz', 'Audi', 'Nissan', 'Mercedes-Benz', 'Honda', 'Nissan', 'Tesla', 'Volvo', 'Hyundai', 'Kia', 'Mazda', 'Subaru', 'Ferrari', 'Lamborghini', 'Porsche', 'Jaguar', 'Land Rover']

# Create a new workbook and add a worksheet
workbook = xlsxwriter.Workbook('10columns100k.xlsx')
worksheet = workbook.add_worksheet()

# Generate the column headers
headers = ['Field_' + str(i + 1) for i in range(num_cols)]

# Add headers to the worksheet
for col, header in enumerate(headers):
    worksheet.write(0, col, header)

# Generate data for each row
for row in range(num_rows):
    boolean_value = random.choice([True, False])
    filepath_value = random.choice(car_manufacturers)
    header_value = random.choice(fruits)

    # Generate a random date between 1900 and 2100
    start_date = datetime.date(1900, 1, 1)
    end_date = datetime.date(2100, 12, 31)
    random_date = datetime.date.fromordinal(random.randint(start_date.toordinal(), end_date.toordinal()))

    integer_value = row + 1
    list_value = random.choice(fruits)
    numerical_value = row + 1
    percent_value = random.randint(0, 100)
    text_value = 'Text ' + str(row + 1)
    url_value = random.choice(car_manufacturers)

    # Write the data to the worksheet
    worksheet.write(row + 1, 0, boolean_value)
    worksheet.write(row + 1, 1, filepath_value)
    worksheet.write(row + 1, 2, header_value)
    worksheet.write(row + 1, 3, random_date.strftime('%d/%m/%Y'))
    worksheet.write(row + 1, 4, integer_value)
    worksheet.write(row + 1, 5, list_value)
    worksheet.write(row + 1, 6, numerical_value)
    worksheet.write(row + 1, 7, percent_value)
    worksheet.write(row + 1, 8, text_value)
    worksheet.write(row + 1, 9, url_value)

# Close the workbook
workbook.close()
print("File successfully created")