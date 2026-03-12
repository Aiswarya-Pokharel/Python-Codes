def main_menu():
    while True:
        print("==== Menu ====")
        print("1. BMI Calculator")
        print("2. Taxation System")
        print("3. Currency Converter")
        print("4. Remittance")
        print("5. Lagani Kosh")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
              print("BMI calculator : https://github.com/bidhyabhattarai/BMI_calculator")
        elif choice == "2":
            print("Taxation system : https://github.com/Anujakhatri/Taxation-system-nepal")
        elif choice == "3":
            print("Currency converter: https://github.com/sneharitas/currency_converter")
        elif choice == "4":
            print("Remittance calculator: https://github.com/binisha77/nepal_remittance_calculator")
        elif choice == "5":
            print("Lagani Kosh: https://github.com/kopiladevkota/nepal_lagani_kosh")
        elif choice == "6":
            print("Invalid")
            break
        else:
            print("Invalid choice")
main_menu()