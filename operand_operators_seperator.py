operation_str = 25+5-5*6/2
global operator_array
global operand_array
operator_array =[]
operand_array = []

def operator_operand_separator(operation_string):
    combined_str = ""
    operator = ["+", "-", "*", "/"]
    for pos, char in enumerate(operation_string):
        if char in operator:
            operator_array.append(char)
            operand_array.append(combined_str)
            combined_str = ""
        else:
            combined_str += char

        if(pos == len(operation_string)-1):
            operand_array.append(combined_str)

def get_seperated_operators():
    return operator_array

def get_seperated_operands():
    return operand_array
















