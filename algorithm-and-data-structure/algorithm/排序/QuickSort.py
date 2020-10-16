def Partition(A, start, end):
    left_ptr = start + 1
    right_ptr = end
    while True:
        while left_ptr <= right_ptr and A[left_ptr] <= A[start]:
            left_ptr += 1
        while right_ptr >= left_ptr and A[right_ptr] >= A[start]:
            right_ptr -= 1
        if left_ptr > right_ptr:
            break
        else:
            A[left_ptr], A[right_ptr] = A[right_ptr], A[left_ptr]
    A[right_ptr], A[start] = A[start], A[right_ptr]
    return right_ptr


def Partition_CLRS(A, start, end):
    i = start - 1
    for j in range(start, end):
        if A[j] < A[end]:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[end], A[i+1] = A[i+1], A[end]
    return i+1


def quickSort(A, start, end):
    if start < end:
        mid = Partition(A, start, end)
        quickSort(A, start, mid - 1)
        quickSort(A, mid + 1, end)


if __name__ == '__main__':
    import random
    n=1000
    A = list(range(n))
    random.shuffle(A)
    print(A)
    quickSort(A, 0, len(A) - 1)
    print(A == list(range(n)))
