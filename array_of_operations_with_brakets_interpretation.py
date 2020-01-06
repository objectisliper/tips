list_of_values = ['(','2','+','4','+','(','15','*','(','28','+','6',')','+','3','*','(','8','*','(','23','/','2',')',')',')','+','5',')']

print(' '.join(list_of_values))

def base_operations(first_value: int, operator: str, second_value: int):
    return {
        '+': first_value + second_value,
        '-': first_value - second_value,
        '*': first_value * second_value,
        '/': first_value / second_value
    }[operator]
    
operations_priorities = ['*', '/', '+', '-']

def get_open_close_brakers_index(list_of_brakers: list):
    open_braker = list_of_brakers.index('(')
    
    open_brakers_count = list_of_brakers.count('(')
    
    if open_brakers_count > 1:
        path_braker_count = 0
        for index, char in enumerate(list_of_brakers):
            if index < list_of_brakers.index('('):
                continue

            if char == ')':
                path_braker_count -= 1
            elif char == '(':
                path_braker_count += 1
                
            if path_braker_count == 0:
                return open_braker, index
                
    else:
        last_braker = list_of_brakers.index(')')
    
    return open_braker, last_braker


def recursively_calculate(arg_list: list) -> int:
    print(' '.join(arg_list))
    if len(arg_list) < 1:
        raise ValueError('Given list is empty')
        
    while '(' in arg_list and ')' in arg_list:
    
        first_index, last_index = get_open_close_brakers_index(arg_list)
    
        subArray = arg_list[first_index + 1: last_index]
        del arg_list[first_index: last_index + 1]
        arg_list.insert(first_index, recursively_calculate(subArray))
                
    while len(arg_list) > 1:
        print(arg_list)
        for operand in operations_priorities:
            while operand in arg_list:
                operand_index = arg_list.index(operand)
                result_value = base_operations(float(arg_list[operand_index-1]), operand, float(arg_list[operand_index+1]))
                del arg_list[operand_index-1: operand_index+2]
                arg_list.insert(operand_index-1, result_value)
                
        
    return arg_list.pop()
        
            
            
    
    
    
print(recursively_calculate(list_of_values))
