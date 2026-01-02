import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Original Array:", arr)

print("First element:", arr[0])
print("second element:", arr[1])
print("Last element:", arr[-1])

print("Elements from index 2 to 5:", arr[2:6])
print("First four elements:", arr[:4])
print("Elements from index 4 to end:", arr[4:])
print("Every second element:", arr[::2])

arr[1] = 25
print("Array after modification:", arr)

arr[2:5] = [35, 48, 56]
print("Array after slice modification:", arr)
print("minimum:",np.min(arr))
print("maximum:",np.max(arr))
print("mean:",np.mean(arr))
print("standard deviation:",np.std(arr))
print("shape:",arr.shape)
print("size:",arr.size)
print("sum:",np.sum(arr))
