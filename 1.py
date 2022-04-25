# Write your solution for algorithm 1 below

def bubble_sort(alist):
    
    for i in range(len(alist)-1):
        swapped = False
        print(f"iteration ")
        for j in range(len(alist)-1):
            print(f"comparing {alist[j], alist[j+1]}")
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                swapped = True

        if not swapped:
            return
    
    return alist

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")