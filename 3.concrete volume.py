
total_volume = 0

while True:
    building_type = input("Enter building type - residential (R) or commercial (C), or 'X' to exit: ").lower()
    if building_type.lower() == 'residential' or building_type.lower() == 'r':
        depth = 0.25 
    else:
        depth = 0.5

    
    if building_type == 'x':
        break

    length = float(input("Enter length in meters: "))
    width = float(input("Enter width in meters: "))
    volume = length * width * depth

    if volume is not None:
        total_volume += volume
        print(f"The volume of concrete required for a slab with a length of {length} meters, width of {width} meters, and depth of {depth:.2f} meters is {volume:.2f} cubic meters.")

print(f"\nTotal concrete volume: {total_volume:.2f} cubic meters.")

