def quickSort(nums, left, right):
    if left <= right:
        i = left
        j = right
        x = nums[i]
        while i < j:
            while i < j and nums[j] > x:
                j -= 1
            if i < j:
                nums[i] = nums[j]
            while i < j and nums[i] < x:
                i += 1
            if i < j:
                nums[j] = nums[i]
        nums[i] = x
        print(nums)
        quickSort(nums, left, i - 1)
        quickSort(nums, i + 1, right)


if __name__ == "__main__":
    array = [72, 6, 57, 88, 60, 42, 83, 73, 48, 85]
    n = len(array)
    quickSort(array, 0, n - 1)
    print("排序后的数组:")
    for i in range(n):
        print("%d" % array[i])
