def calculate_bmi(weight, height):
    """
    Calculate BMI based on weight (in kilograms) and height (in meters).
    BMI Formula: BMI = weight / (height ** 2)
    """
    return weight / (height ** 2)

def classify_bmi(bmi):
    """
    Classify BMI into categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_user_input():
    """
    Prompt users for their weight and height.
    """
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    return weight, height

def main():
    print("Welcome to the BMI Calculator!")

    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
