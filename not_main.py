def nested_while(max_1, max_2):
    current_1 = 0
    current_2 = 0
    while current_1 <= max_1:
        while current_2 <= max_2:
            print(current_1, current_2)
            current_2 += 1
        current_2 = 0
        current_1 += 1


def nested_for(max_1, max_2):
    for i in range(max_1):
        for j in range(max_2):
            print(i, j)


nested_while(5, 5)
