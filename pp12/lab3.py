print("Obliczenie wskaźnika BMI")
def get_data():
    weight_in_kg = float(input("Podaj swoją wagę w kg: "))
    hight_in_cm = float(input("Podaj swój wzrost w cm: "))
    return [weight_in_kg, hight_in_cm]

def calculate_bmi(weight_in_kg, hight_in_m):
    return  weight_in_kg / hight_in_m ** 2


def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Niedowaga"
    elif bmi < 25:
        return "Waga prawidłowa"
    elif bmi < 30:
        return "Nadwaga"
    else:
        return "Otyłość"

weight_in_kg, hight_in_cm = get_data()
bmi = calculate_bmi(weight_in_kg, hight_in_cm * .01)
category = determine_bmi_category(bmi)

print("Wskaźnik BMI: ", round(bmi, 2))
print("Kategoria: ", category)