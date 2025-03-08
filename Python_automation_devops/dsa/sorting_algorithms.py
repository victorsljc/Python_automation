
# .............. comparision sorting algorithms ................................

# buble sort applied on small datasets as big(n**2)

def test_buble_sort():
    a=[12,122,3434,2,13,9]
    for x in range(len(a)):
        for y in range(len(a)):
            if a[x]<a[y]:
                a[x],a[y]=a[y],a[x]
                print(a)


def test_selection_sort():
    arr = [64, 25, 12, 22, 11]
    print("\nOriginal array:", arr)
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)


def test_insertion_sort():
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1  # Start comparing with the previous element

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key in its correct position
        arr[j + 1] = key
    print("Sorted array:", arr)


def quick_sort(arr):
    # Base case: if the array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (here we choose the last element)
    pivot = arr[-1]

    # Partition the array into two sub-arrays
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    # Recursively apply quick_sort to the sub-arrays and combine the results
    return quick_sort(left) + [pivot] + quick_sort(right)

def test_merge_sort():
    def merge_sort(arr):
        if len(arr) > 1:
            # Find the middle point and divide the array into two halves
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Recursively sort both halves
            merge_sort(left_half)
            merge_sort(right_half)

            # Merge the sorted halves
            i = j = k = 0

            # Copy data to temp arrays left_half[] and right_half[]
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Check if any element was left in left_half
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            # Check if any element was left in right_half
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    # Example usage
    arr = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr)
    print("Sorted array is:", arr)