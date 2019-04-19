def bubble_sort(alist):
    for numbers in range(len(alist)-1, 0, -1):
        for number in range(numbers):
            if alist[number] > alist[number + 1]:
                temp = alist[number]
                alist[number] = alist[number + 1]
                alist[number + 1] = temp
