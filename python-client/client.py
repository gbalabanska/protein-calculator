from zeep import Client

def main():
    print("Welcome to the Protein Intake Calculator!")
    print("This tool will help you estimate your daily protein needs based on your weight and training intensity.")
    print("Training intensity options:")
    print("  - L (low): Light activity or minimal training")
    print("  - M (moderate): Regular training with moderate effort")
    print("  - H (high): Intense training or heavy physical activity\n")

    wsdl_url = 'http://127.0.0.1:8000/?wsdl'
    client = Client(wsdl_url)

    intensity_map = {
        'l': 'low',
        'm': 'moderate',
        'h': 'high'
    }

    while True:
        weight_input = input("Please enter your weight in kilograms (or type 'exit' to quit): ").strip()
        if weight_input.lower() == 'exit':
            print("Thank you for using the Protein Intake Calculator. Goodbye!")
            break
        
        try:
            weight = float(weight_input)
            if weight <= 0:
                print("Weight must be a positive number. Please try again.")
                continue
        except ValueError:
            print("That doesn’t look like a valid number. Please enter your weight in kilograms.")
            continue

        intensity_input = input(
            "How would you describe your training intensity?\n"
            "Type 'L' for low, 'M' for moderate, or 'H' for high intensity: "
        ).strip().lower()

        while intensity_input not in intensity_map:
            intensity_input = input("Please type only 'L', 'M', or 'H' to describe your training intensity: ").strip().lower()

        intensity = intensity_map[intensity_input]

        protein = client.service.get_protein(weight, intensity)

        print(f"\nBased on a weight of {weight:.1f} kg and '{intensity}' training intensity,")
        print(f"your recommended daily protein intake is approximately {protein:.2f} grams.\n")

if __name__ == "__main__":
    main()
