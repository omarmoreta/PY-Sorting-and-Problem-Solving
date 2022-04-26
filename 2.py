# Write your solution for algorithm 2 below
unsorted_numerical_list = [6, 1, 9, 2, 5, 3, 8, 7, 4]

unsorted_numerical_list.sort()
print(unsorted_numerical_list)

unsorted_numerical_list_two = [6, 1, 9, 2, 5, 3, 8, 7, 4]

def sorting_method():
    print(sorted(unsorted_numerical_list_two))

sorting_method()

unsorted_numerical_list_three = [6, 1, 9, 2, 5, 3, 8, 7, 4]

new_list = sorted(unsorted_numerical_list_three, reverse=True)
print(new_list)