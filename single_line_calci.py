import operand_operators_seperator

operation_str = "10*4/2+5-2"
operand_operators_seperator.operator_operand_separator(operation_str)
operators = operand_operators_seperator.get_seperated_operators()
operands = operand_operators_seperator.get_seperated_operands()
division_multiplication= ['*', '/']
addition_subtraction= ['+', '-']

def performOperation(operator):
    operator_position= operators.index(operator)
    operand1= operands[operator_position]
    operand2= operands[operator_position+1]

    if(operator == "/"):
        result1 = int(operand1) / int(operand2)
    elif(operator == "*"):
        result1 = int(operand1) * int(operand2)
    elif(operator == "-"):
        result1 = int(operand1) - int(operand2)
    elif(operator == "+"):
        result1 = int(operand1) + int(operand2)

    operators.pop(operator_position)
    operands.pop(operator_position)
    operands.pop(operator_position)
    operands.insert(operator_position, result1)
    print("After "+operator+"  Operation: ", operands)

while len(operands) > 1:
    while '/'in operators:
        performOperation("/")
    
    while '*'in operators:
        performOperation("*")

    
    while '-' in operators:
        performOperation("-")

    
    while '+' in operators:
        performOperation("+")
    
print(operands)


