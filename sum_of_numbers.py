def find_sum(arr, m):
    if len(arr) < 2:
        return
    else:
        for i in range(len(arr) - 1):
            if m - arr[i] in arr:
                return arr.index(arr[i]), arr.index(m - arr[i])
