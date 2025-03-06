
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

