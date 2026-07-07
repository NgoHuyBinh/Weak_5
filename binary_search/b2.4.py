def binary_search(arr, left, right, key):
    if right >= left:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, left, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, right, key)
    else:
        return -1 

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
n = len(arr)

print("Mảng hiện tại:", arr)
print("-" * 30)

# a) Key x = 95
x_a = 95
result_a = binary_search(arr, 0, n - 1, x_a)

print(f"Tìm x = {x_a}")
if result_a != -1:
    print(f" Tìm thấy tại vị trí i = {result_a}")
else:
    print("Không tìm thấy phần tử trong mảng (Kết quả: -1)")

# b) Key x = 5
x_b = 5
result_b = binary_search(arr, 0, n - 1, x_b)

print(f"Tìm x = {x_b}:")
if result_b != -1:
    print(f"Tìm thấy tại vị trí i = {result_b}")
else:
    print("Không tìm thấy phần tử trong mảng (Kết quả: -1)")