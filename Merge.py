def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    """ Merge helper
        Complexity: O(n)
    """

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # Add the left overs if there's any left to the result
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    # Add the left overs if there's any left to the result
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    # Return result
    return merged


if __name__ == "__main__":
    array = [75, 12, 34, 45, 0, 123, 32, 56, 32, 99, 123, 11, 86, 33]
    res = merge_sort(array)
    print(res)
