def bubbleSort(input_array):
    
    sorted_flag = False
    
    for i in range(len(input_array) - 1):
        for j in range(0, len(input_array) - i - 1):
            
            if input_array[j] > input_array[j + 1]:
                sorted_flag = True
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]
         
        if not sorted_flag:
            return
 

my_list = list(input().split())
for i in range(len(my_list)):
    my_list[i] = float(my_list[i])
 
bubbleSort(my_list)
print(my_list)