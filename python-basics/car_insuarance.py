# Car Insurance POS System
# Author: Triza Mwaura
# Date: 24/02/2026

def calculate_premium(car_value, coverage_type):
    if coverage_type == 1:  # Third Party
        rate = 0.03
        coverage_name = "Third Party"
    elif coverage_type == 2:  # Third Party Fire & Theft
        rate = 0.05
        coverage_name = "Third Party Fire & Theft"
    elif coverage_type == 3:  # Comprehensive
        rate = 0.08
        coverage_name = "Comprehensive"
    else:
        rate = 0
        coverage_name = "Unknown"

    premium = car_value * rate
    return premium, coverage_name


def main():
    print("==== CAR INSURANCE POS SYSTEM ====\n")

    client_name = input("Enter client name: ")
    phone = input("Enter phone number: ")
    car_make = input("Enter car make: ")
    car_model = input("Enter car model: ")
    car_value = float(input("Enter car value (KES): "))

    print("\nSelect Coverage Type")
    print("1. Third Party")
    print("2. Third Party Fire & Theft")
    print("3. Comprehensive")

    coverage_type = int(input("Enter option (1-3): "))

    premium, coverage_name = calculate_premium(car_value, coverage_type)

    print("\n===== RECEIPT =====")
    print(f"Client: {client_name}")
    print(f"Phone: {phone}")
    print(f"Car: {car_make} {car_model}")
    print(f"Coverage: {coverage_name}")
    print(f"Car Value: KES {car_value:,.2f}")
    print(f"Premium: KES {premium:,.2f}")
    print("====================")


if __name__ == "__main__":
    main()