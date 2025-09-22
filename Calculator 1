# Ask for user input
calculator_input = input("Please fill out basic calculation in the form of 'x OP y':")

# Check if the input contains the '+' operator
if '+' in calculator_input:
    parts = calculator_input.split('+')
    a = int(parts[0])
    b = int(parts[1])
    calculator_output = a + b           # Perform Addition

# Check if the input contains the '-' operator
elif '-' in calculator_input:
    parts = calculator_input.split('-')
    a = int(parts[0])
    b = int(parts[1])
    calculator_output = a - b           # Perform Subtraction

# Check if the input contains the '*' operator
elif '*' in calculator_input:
    parts = calculator_input.split('*')
    a = int(parts[0])
    b = int(parts[1])
    calculator_output = a * b           # Perform Multiplication

# Check if the input contains the '/' operator
elif '/' in calculator_input:
    parts = calculator_input.split('/')
    a = int(parts[0])
    b = int(parts[1])
    if b == 0:                          # Check for division by 0 first
        calculator_output = "Not possible, dividing by zero is not allowed."
    else:
        calculator_output = a / b       # Perform Division

# Check if the input contain the '^' operator for power/ exponentiation
elif '^' in calculator_input:
    parts = calculator_input.split('^')
    a = int(parts[0])
    b = int(parts[1])
    calculator_output = a ** b          # Perform exponentiation

# If none of the supported operators were found
else:
    calculator_output = "Not possible, received invalid input."

# Print the original user input and the result
print (calculator_input, '=', calculator_output)
