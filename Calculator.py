print("Calculator For Practice")
num1 = float(input("ENTER THE FIRST DIGIT: "))
num2 = float(input("ENTER THE SECOND DIGIT: "))

print("CHOOSE ANY ONE FROM THE OPTIONS BELOW:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Subtraction")
print("5. Floor Division")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 * num2)
elif choice == 3:
    print("Result:", num1 / num2)
elif choice == 4:
    print("Result:", num1 - num2)
elif choice == 5:
    print("Result:", num1 // num2)
else:
    print("Invalid choice 💀")
