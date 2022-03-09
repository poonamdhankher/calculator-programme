import operand_operators_seperator

operation_str = "10*4/2+5-2"
operand_operators_seperator.operator_operand_separator(operation_str)
operators = operand_operators_seperator.get_seperated_operators()
operands = operand_operators_seperator.get_seperated_operands()
division_multiplication= ['*', '/']
addition_subtraction= ['+', '-']

while len(operands) > 1:
    while '/'in operators:
        operator_position= operators.index('/')
        operand1= operands[operator_position]
        operand2= operands[operator_position+1]
        result1 = int(operand1) / int(operand2)
        operators.pop(operator_position)
        operands.pop(operator_position)
        operands.pop(operator_position)
        operands.insert(operator_position, result1)
        print("After / Operation: ", operands)

    
    while '*'in operators:
        operator_position= operators.index('*')
        operand1= operands[operator_position]
        operand2= operands[operator_position+1]
        result1 = int(operand1) * int(operand2)
        operators.pop(operator_position)
        operands.pop(operator_position)
        operands.pop(operator_position)
        operands.insert(operator_position, result1)
        print("After * Operation: ", operands)

    
    while '-' in operators:
        operator_position= operators.index('-')
        operand1= operands[operator_position]
        operand2= operands[operator_position+1]
        result1 = int(operand1) - int(operand2)
        operators.pop(operator_position)
        operands.pop(operator_position)
        operands.pop(operator_position)
        operands.insert(operator_position, result1)
        print("After - Operation: ", operands)

    
    while '+' in operators:
        operator_position= operators.index('+')
        operand1= operands[operator_position]
        operand2= operands[operator_position+1]
        result1 = int(operand1) + int(operand2)
        operators.pop(operator_position)
        operands.pop(operator_position)
        operands.pop(operator_position)
        operands.insert(operator_position, result1)
        print("After + Operation: ", operands)
    
print(operands)