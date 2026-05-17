def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def main():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Celsius → Fahrenheit")
        print("2. Celsius → Kelvin")
        print("3. Fahrenheit → Celsius")
        print("4. Fahrenheit → Kelvin")
        print("5. Kelvin → Celsius")
        print("6. Kelvin → Fahrenheit")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        try:
            value = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == "1":
            print("Result:", celsius_to_fahrenheit(value), "°F")
        elif choice == "2":
            print("Result:", celsius_to_kelvin(value), "K")
        elif choice == "3":
            print("Result:", fahrenheit_to_celsius(value), "°C")
        elif choice == "4":
            print("Result:", fahrenheit_to_kelvin(value), "K")
        elif choice == "5":
            print("Result:", kelvin_to_celsius(value), "°C")
        elif choice == "6":
            print("Result:", kelvin_to_fahrenheit(value), "°F")
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()