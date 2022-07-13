my_list = list(input().split())
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

print([int(i) for i in my_list if (i % 3 == 0 and my_list.index(i) % 3 == 0)])