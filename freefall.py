
# Program for calculating the free fall time w/o air resistance at 9.8 m/s given the distance.

def falltime(d):
    x = float(d)/4.9
    t = pow(x, (1/2))
    return t

print("This program calculates the time for free fall based on the distance given.")
distance = input("Insert the distance for the fall:")

time = falltime(distance)
print("The fall will take " + str(time) + " seconds.")

#end program
