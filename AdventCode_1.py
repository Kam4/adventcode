import math

#Read file
input_file = open(r'path to file..')
mass_s = input_file.readlines()

#conver to int
mass = list(map(int, mass_s))

total_fuel = 0

for i in range(len(mass)):
    total_fuel += math.floor((mass[i] / 3) - 2)

print (total_fuel)
