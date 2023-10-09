#  Linear Search
# iterates through the arr list and compares each element with the target. 
#  If it finds a match, it returns the index of that element. 
# If it doesn't find a match after iterating through the entire list, 
# it returns -1 to indicate that the element was not found. 
# It has linear time O(n)

def linear_search(alist, target):
    # Iterate through the list
    for i in range(len(alist)):
        # If the current element matches the target, return its index
        if alist[i] == target:
            return i
    # If the target is not found, return -1 
    return -1
arr = [4, 7, 2, 9, 1, 5]
target_element = 9 
index = linear_search(arr, target_element)

if index != -1:
    print(f"Element {target_element} found at index {index}.")
else:
    print(f"Element {target_element} not found in the list.")



# Binary Search
# This one  searches for the target element in a sorted list (arr) 
# by repeatedly dividing the search interval in half. 
# It compares the target with the middle element and eliminates 
# half of the search space with each iteration.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2   # Calculate the middle index

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        
        # If the target is less than the middle element, search the left half
        elif arr[mid] > target:
            right = mid - 1
        
        #  If the target is greater than the middle element, search the right half
        else: 
            left = mid + 1
    # If the target is not found, return -1
    return -1 

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target_element = 40
result = binary_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
