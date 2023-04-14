import random
from datetime import datetime, timedelta

# Generate a list of 10 random datetimes
datetimes = []
for i in range(10):
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    random_date = start_date + (end_date - start_date) * random.random()
    datetimes.append(random_date.strftime('%d/%m/%Y %H:%M:%S'))

# Print the datetimes in a column
for dt in datetimes:
    print(dt)