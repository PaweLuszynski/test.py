import random

# List of car names
car_names = ["Toyota", "Ford", "Honda", "Chevrolet", "Nissan", "Hyundai", "Kia", "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "Ferrari", "Lamborghini", "Porsche", "Maserati", "Tesla", "Jaguar", "Land Rover", "Jeep", "Dodge"]

# Generate a list of 10 random car names
random_cars = random.sample(car_names, k=10)

# Print the car names in a column
for car in random_cars:
    print(car)
