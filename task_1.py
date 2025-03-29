print("\n\tBasic Arithmetic Operations on 2 numbers\n")

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("\n")
print("Addition: ", (first + second))

sub_result = first - second
print("Substraction: " + str(sub_result))

print("Multiplication: %d" %(first * second))

if(second == 0):
    print("Cannot divide by zero, please give a number other than zero")
else:
    print(f"Division: {first/second}")