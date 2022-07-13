import statistics

my_input_list = [int(x) for x in input("enter: ").split()]

result_dict = {"max":max(my_input_list),
               "min":min(my_input_list),
               "mean":statistics.mean(my_input_list),
               "median":statistics.median(my_input_list)}

print(result_dict)