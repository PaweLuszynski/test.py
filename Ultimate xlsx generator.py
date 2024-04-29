import random
import datetime
import xlsxwriter
import string

# Specify the number of rows and columns
num_rows = 500  # Change the number of rows as needed
num_cols = 10 # Change the number of columns as needed

# Names for the "List" column
names = ['chamal', 'joshua', 'ethan', 'kiara']

def generate_excel_file(num_rows, num_cols):
    # List of car manufacturers for the URL column
    car_manufacturers = ['Toyota', 'Ford', 'Chevrolet', 'Volkswagen', 'BMW', 'Mercedes-Benz', 'Audi', 'Nissan', 'Mercedes-Benz', 'Honda', 'Nissan', 'Tesla', 'Volvo', 'Hyundai', 'Kia', 'Mazda', 'Subaru', 'Ferrari', 'Lamborghini', 'Porsche', 'Jaguar', 'Land Rover']

    # Generate the filename based on the number of columns
    filename = f'{num_cols}columns{num_rows}rows.xlsx'

    # Create a new workbook and add a worksheet
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Define data types for the columns
    data_types = [
        "Boolean", "Date", "DateTime", "Integer", "Number", "Text", "Integer", "List", "URL", "Percent"
    ]

    # Generate the column headers and data for each row
    for col in range(num_cols):
        header = f'Field_{col + 1}'
        data_type = data_types[col % len(data_types)]  # Cycle through data types

        # Add headers to the worksheet
        worksheet.write(0, col, header)

        # Generate data for each row
        for row in range(num_rows):
            if data_type == "Boolean":
                data_value = random.choice([True, False])
            elif data_type == "Date":
                start_date = datetime.date(1900, 1, 1)
                end_date = datetime.date(2100, 12, 31)
                random_date = datetime.date.fromordinal(random.randint(start_date.toordinal(), end_date.toordinal()))
                data_value = random_date.strftime('%Y-%m-%d')  # Change the format to 'dd/mm/yyyy'
            elif data_type == "DateTime":
                random_date = datetime.datetime(
                    random.randint(1900, 2100),
                    random.randint(1, 12),
                    random.randint(1, 28),
                    random.randint(0, 23),
                    random.randint(0, 59)
                )
                data_value = random_date.strftime('%Y-%m-%dT%H:%M:%S.000Z')  # Change the format to 'dd/mm/yyyy hh:mm AM/PM'
            elif data_type in ["Integer", "Number"]:
                data_value = random.randint(1, 1000) if data_type == "Integer" else random.uniform(1, 1000)
            elif data_type == "Text":
                data_value = 'Text ' + ''.join(random.choices(string.ascii_letters, k=5))
            elif data_type == "List":
                data_value = random.choice(names)  # Use the provided names
            elif data_type == "URL":
                data_value = random.choice(car_manufacturers)
            elif data_type == "Percent":
                data_value = random.randint(0, 100)

            # Write the data to the worksheet
            worksheet.write(row + 1, col, data_value)

    # Close the workbook
    workbook.close()
    print(f"File '{filename}' successfully created")

# Example usage:
generate_excel_file(num_rows, num_cols)  # Creates a file with the specified number of rows and columns
