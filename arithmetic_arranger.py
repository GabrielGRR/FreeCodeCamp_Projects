def arithmetic_arranger(list_operations, op_sum=False):
    """ 
    https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
    exercise example: arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True) 
    """

    if len(list_operations) > 5: #ERROR MESSAGE: the limit of operations is five
        raise Exception("Error: Too many problems.")


    first_number = []
    second_number = []
    operators = []

    len_operations = [] #max lenght of a number
    
    for operation in list_operations: #adding the data to lists

        num_1, op, num_2 = operation.split()

        if len(num_1) > 4 or len(num_2) > 4: #ERROR MESSAGE: maximum of 4 digits
            raise Exception("Error: Numbers cannot be more than four digits.")

        try:
            first_number.append(int(num_1))
            second_number.append(int(num_2))
        except: #ERROR MESSAGE: num_1 or num_2 is not an integer
            print("Error: Numbers must only contain digits.")

        operators.append(op) 
        if op != "+" and op!= "-": #ERROR MESSAGE: there shouldnt be any operators except - and +
            raise Exception("Error: Operator must be '+' or '-'.")

        len_op = len(max(operation.split(), key=len))+2 #biggest number in lenght +2, for the operator and a blank space
        len_operations.append(len_op)

    for i in range(len(first_number)): #first line
        print(f"{first_number[i] : >{len_operations[i]}}", end='    ' if i != len(second_number) - 1 else '')#if state doesnt print the blank spaces if its the last loop iteration
    print() # next line

    for i in range(len(second_number)): #second line
        print(operators[i]+f"{second_number[i] : >{len_operations[i]-1}}", end='    ' if i != len(second_number) - 1 else '')
    print() # next line

    for i in range(len(second_number)): #line with dashes to separete results
        print("-"*len_operations[i], end='    ' if i != len(second_number) - 1 else '')
    print() # next line


    results = []
    for i in range(len(second_number)): #results condition
        if operators[i] == "+":
            result = first_number[i] + second_number[i]
        else: 
            result = first_number[i] - second_number[i]
        results.append(result)

    if op_sum == True: #if results must be shown
        for i in range(len(results)): #result line
            print(f"{results[i] : >{len_operations[i]}}", end='    ' if i != len(second_number) - 1 else '')
