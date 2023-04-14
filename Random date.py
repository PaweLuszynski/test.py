import random
from datetime import datetime, timedelta

# Generate a list of 10 random dates
dates = []
for i in range(10):
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    random_date = start_date + (end_date - start_date) * random.random()
    dates.append(random_date.strftime('%d/%m/%Y'))

# Print the dates in a column
for date in dates:
    print(date)