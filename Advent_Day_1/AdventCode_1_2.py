import math

#Read file
input_file = open(r'C:\Users\kmudy\Documents\Python Scripts\data\input.txt')
mass_s = input_file.readlines()


mass = list(map(int, mass_s))
total_fuel = 0
new_fuel = 0
new_total = 0

for i in range(len(mass)):
    fuel = mass[i]

    while fuel > 0:
        new_fuel = math.floor(fuel / 3 - 2)
        fuel = new_fuel
        if(fuel > 0):
            total_fuel += fuel 
        else:
            break
    
    new_total += total_fuel
    total_fuel = 0


print (new_total)
    
    
         


#fuel = 1969
#fuel_total = 0

#while fuel > 0 :
        
#        new_fuel = math.floor(fuel / 3 - 2)
#        fuel = new_fuel
#        if(fuel > 0):
#            fuel_total += fuel 
#        else:
#            break
#        print (fuel)
        
#print(fuel_total)