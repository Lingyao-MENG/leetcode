
def mergesort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == "__main__":
    array = [72, 6, 57, 88, 60, 42, 83, 73, 48, 85]
    n = len(array)
    #mergeSort(array, 0, n - 1)
    array = mergesort(array)
    print("排序后的数组:")
    for i in range(n):
        print("%d" % array[i])

