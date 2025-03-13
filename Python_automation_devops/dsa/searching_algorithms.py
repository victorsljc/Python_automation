
def test_binary_search():
    def binary_search(numbers, val):
        first = 0
        last = len(numbers) - 1
        index = -1
        while (first <= last) and (index == -1):
            mid = (first + last) // 2
            if numbers[mid] == val:
                index = mid
            else:
                if val < numbers[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return index

    a = binary_search([12, 1, 134, 45, 7, 23423, 8], 45)
    print(a)

