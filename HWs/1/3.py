def calculate(my_input):
    
    my_input = my_input.split()
    
    if len(my_input) != 3:
        print('please use the correct form of input')
    
    num_1, sign, num_2 = int(my_input[0]), my_input[1], int(my_input[2])
    
    if sign == '+':
        return num_1 + num_2
    
    elif sign == '-':
        return num_1 - num_2
    
    elif sign == '*':
        return num_1 * num_2
    
    elif sign == '/':
        return num_1 / num_2
    
    elif sign == '**':
        return num_1 ** num_2
    
    elif sign == '%':
        return num_1 % num_2
    
    else:
        return 'the input sign in not valid'


my_input_1 = input()
print(calculate(my_input_1))