def countSort(arr):
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]
    ans = [0 for _ in arr]
    for i in arr:
        count[ord(i)] += 1
    for i in range(256):
        count[i] += count[i - 1]
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


def count_sort(array):
    max_value = max(array)
    min_value = min(array)
    len_count = max_value - min_value + 1
    count = [0 for _ in range(len_count)]
    result = [0 for _ in range(len_count)]
    for index, value in enumerate(array):
        index = value - min_value
        count[index] += 1
    for i in range(1, len_count):
        count[i] += count[i-1]
    for value in array:
        result[count[value-min_value] -1] = value
        count[value-min_value] -= 1
    return result


if __name__ == "__main__":
    array = [72, 6, 57, 88, 60, 42, 83, 73, 48, 85]
    #array = "wwwrunoobcom"
    n = len(array)
    array = count_sort(array)
    print("排序后的数组:")
    for i in range(n):
        print(array[i])

