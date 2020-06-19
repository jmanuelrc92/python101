def bubbleSort(elements):
    i = 0
    while i < len(elements):
        j = i + 1
        while j < len(elements):
            if elements[i] > elements[j]:
                aux = elements[i]
                elements[i] = elements[j]
                elements[j] = aux
            j = j + 1
        i = i + 1
    return elements

print(bubbleSort([1, 3, 4, 9, 10]))
print(bubbleSort([70, 0.5, -2, 9, 10, 6, 9.2]))
print(bubbleSort([70, 9.3, 0.5, -2, 9, 10, 6, 9.2]))