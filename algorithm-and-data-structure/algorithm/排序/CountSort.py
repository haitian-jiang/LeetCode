def CountSort(A, k):
    counter = [0 for _ in range(k)]
    sorted_A = [0 for _ in A]
    for i in range(len(A)):
        counter[A[i]] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    for i in range(len(sorted_A)-1, -1, -1):
        sorted_A[counter[A[i]]-1] = A[i]  # counter[A[i]]-1 because A and sorted_A starts from index 0
        counter[A[i]] -= 1
    return sorted_A


if __name__ == '__main__':
    import random
    length = 1000
    A = list(range(length))
    random.shuffle(A)
    print(A)
    check = list(range(length))
    A = CountSort(A, length)
    print(A)
    print(A == check)
