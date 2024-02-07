def calculate_concrete_volume(building_type, length, width):
    depth = 0.25 if building_type.lower() == 'residential' else 0.5
    return length * width * depth

def main():
    total_volume = 0

    while True:
        building_type = input("Enter building type (residential or commercial), or 'X' to exit: ").lower()

        if building_type == 'x':
            break

        length, width = float(input("Enter length in meters: ")), float(input("Enter width in meters: "))
        volume = calculate_concrete_volume(building_type, length, width)

        if volume is not None:
            total_volume += volume
            print(f"The volume of concrete required for a slab with a length of {length} meters, width of {width} meters, and depth of {volume:.2f} meters is {volume:.2f} cubic meters.")

    print(f"\nTotal concrete needed for the day: {total_volume:.2f} cubic meters.")

if __name__ == "__main__":
    main()
