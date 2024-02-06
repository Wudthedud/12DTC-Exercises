m = int(input("Enter a number of meters for conversion: "))
conversions = [[1000, "millimeters"], [100, "centimeters"], [0.001, "kilometers"], [39.3701, "inches"], [3.28084, "feet"], [0.000621371, "miles"], [1.09361, "yards"]]
print(f"{m} meters is: ")
[print(f"{m * i[0]} {i[1]}") for i in conversions]