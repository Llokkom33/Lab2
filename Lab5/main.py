def number_to_word(number):
    words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    return words.get(number, "Invalid number")

def main():
    print("Welcome!")
    while True:
        try:
            number = int(input("Enter a number (or 'q' to quit): "))
            print(number_to_word(number))
        except ValueError:
            choice = input("Invalid input. Do you want to quit? (y/n): ")
            if choice.lower() == 'y':
                break

    print("Goodbye!")

if __name__ == "__main__":
    main()
