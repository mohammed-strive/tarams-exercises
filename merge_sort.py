def mergeSort(items):

    if len(items) > 1:
        mid = len(items) // 2
        leftHalf = items[:mid]
        rightHalf = items[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=j=k=0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                items[k] = leftHalf[i]
                i += 1
            else:
                items[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            items[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
           items[k]  = rightHalf[j]
           j += 1
           k += 1


if __name__ == '__main__':
    items = [5, 10, 9, 10, 1, 2, 45]
    mergeSort(items)
    print(items)
