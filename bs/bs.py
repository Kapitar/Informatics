arr = [1, 5, 62, 57, 123, 6, 125]
arr.sort()

def bs(arr, n):
    l = 0
    r = len(arr) - 1
    while r - l > 1:
        m = (r + l) // 2

        if arr[m] > n:
            r = m
        else:
            l = m

    return r
print(arr)
print(bs(arr, 1))