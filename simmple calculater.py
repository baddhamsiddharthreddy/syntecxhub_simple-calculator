def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    current_result = None

    while True:
        print("\n--- Simple Calculator ---")
        if current_result is not None:
            print(f"Current Result: {current_result}")
        print("Operations: + | - | * | / | clear | exit")

        choice = input("Choose an operation: ").strip().lower()

        if choice == "exit":
            print("Exiting calculator. Goodbye!")
            break
        elif choice == "clear":
            current_result = None
            print("Calculator cleared.")
            continue
        elif choice not in ("+", "-", "*", "/"):
            print("Invalid operation. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "+":
                current_result = add(num1, num2)
            elif choice == "-":
                current_result = subtract(num1, num2)
            elif choice == "*":
                current_result = multiply(num1, num2)
            elif choice == "/":
                current_result = divide(num1, num2)

            print(f"Result: {num1} {choice} {num2} = {current_result}")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()