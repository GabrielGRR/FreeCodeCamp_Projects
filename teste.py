import copy

original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)

shallow_copy.remove(1)
print(original_list)  # [1, 2, [99, 4]]
print(shallow_copy)
""" 
print("-----------teste")

teste1 = [1, 2, [3, 4]]
teste2 = teste1

teste2[2][0] = 99
print(teste1)  # [1, 2, [99, 4]]
print(teste2) """

""" 
import copy
x = [1, 2, [3, 4]]
y = copy.copy(x)

y.append(5)

teste1 = [1, 2, [3, 4]]
teste2 = teste1

teste1.append(5)

print(x)
# [1, 2, [3, 4], 5]
print(y)
# [1, 2, [3, 4]]
print("----separação")
print(teste1)
print(teste2) """