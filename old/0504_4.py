def s_s(arr):
    for i in range(len(arr)):
        s_m(arr, i)

def s_m(arr, i):
    min = i
    for j in range(i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

l = [2, 5, 1, 4, 6, 3]
s_s(l)
print(l)