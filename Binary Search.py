# Binary search
n = int(input("Enter the size of list: "))
lst = []
flag = False
print("Enter the elements")
for i in range(0, n):
    lst.append(int(input()))
print(lst)
x = int(input("Enter the element to search"))
low = 0
high = n-1
mid = (low + high) // 2
while low <= high:
    if lst[mid] == x:
        print("Element is found")
        break
    elif lst[mid] < x:
        low = mid +1
    else:
        high = mid - 1
    mid = (low + high) // 2
if low > high:
    print("Element is not found")


# thanks for watching
# like, share & subscribe to
# Dream2Code
