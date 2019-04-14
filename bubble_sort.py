def bubble_sort(alist):
    for numbers in range(len(alist)-1,0,-1):
        for number in range(numbers):
            if alist[i]>alist[i+1]:
                 alist[i],alist[i+1] = alist[i+1],alist[i]
