rate = {'bicycling': 200, 'jogging': 475, 'swimming': 275}
kg = 3500

bicycling_hours = float(input("Enter the number of hours spent bicycling: "))
jogging_hours = float(input("Enter the number of hours spent jogging: "))
swimming_hours = float(input("Enter the number of hours spent swimming: "))


total_calories_burned = (
    bicycling_hours * rate['bicycling'] +
    jogging_hours * rate['jogging'] +
    swimming_hours * rate['swimming']
)

weight_loss_kg = total_calories_burned / kg

print(f"The weight loss is approximately {weight_loss_kg:.3f} kilograms.")

