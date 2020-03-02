def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) >> 1
        #min = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

if __name__ == '__main__':
    ret = binary_search([1, 2, 3, 4, 5, 6, 7], 18)
    print(ret)