import math

def binarySearch (elements, key):
    endIndex = len(elements) - 1
    middle = math.ceil(endIndex / 2)

    if (endIndex < 0):
        return False

    if (elements[middle] == key):
        return key
    elif (elements[middle] > key):
        return binarySearch(elements[0:middle], key)
    elif (elements[middle] < key):
        return binarySearch(elements[middle + 1 :endIndex + 1 ], key)

print(binarySearch([4, 12, 16, 17, 19.5, 21, 57], 17))
print(binarySearch([4, 12, 16, 17, 19.5, 21, 57], 4))
print(binarySearch([4, 12, 16, 17, 19.5, 21, 57], 57))
print(binarySearch([4, 12, 16, 17, 19.5, 21, 57], 18))
print(binarySearch([4, 12, 16, 17, 19.5, 21, 57], 1))
print(binarySearch([4, 12, 16, 17, 19.5, 21, 57], 60))
print(binarySearch([4, 12, 16, 17, 19.5, 21, 57], 13))
print(binarySearch([], 13))