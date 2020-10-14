def Heapfy(A, i):
    l = i * 2
    r = i * 2 + 1
    largest = i
    if l <= A[0] and A[l] > A[largest]:  # A[0] = A.heap_size
        largest = l
    if r <= A[0] and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        Heapfy(A, largest)


def BuildHeap(A):
    A[0] = len(A) - 1  # initial heap size
    for i in range(len(A)//2, 0, -1):
        Heapfy(A, i)


def HeapSort(A):
    BuildHeap(A)
    while A[0] > 1:
        A[1], A[A[0]] = A[A[0]], A[1]
        A[0] -= 1
        Heapfy(A, 1)


if __name__ == '__main__':
    import random
    A=[0]
    B=list(range(1000))
    random.shuffle(B)
    A.extend(B)
    print(A)
    HeapSort(A)
    print(A)
