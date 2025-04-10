from car import Car

cars=[]
with open("cars.txt") as file:
    for line in file:
        line=line.strip().split()
        car=Car(line[0],line[1],int(line[2]),int(line[3]))
        cars.append(car)

#Driving on car 0
print(cars[0])
print(Car.get_gas_tank(cars[0]))
print(Car.get_odometer(cars[0]))
Car.drive(cars[0])
print(Car.get_gas_tank(cars[0]))
print(Car.get_odometer(cars[0]))

#Driving on car 1
print(cars[1])
print(Car.get_gas_tank(cars[1]))
print(Car.get_odometer(cars[1]))
Car.drive(cars[1])
print(Car.get_gas_tank(cars[1]))
print(Car.get_odometer(cars[1]))


