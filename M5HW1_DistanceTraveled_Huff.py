# CTI-110
# Distance Traveled
# Jesse Huff
# 10/25/2017

# Get inputs
vehicleSpeed = float(input("What is the speed of the vehicle in mph?: "))
timeTraveled = int(input("How many hours has it travled?"))

# define

print()

# Print Graph
print("Hour","\tDistance Traveled")
for currentHour in range(1, timeTraveled + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print(currentHour,"\t",distanceTraveled) 
