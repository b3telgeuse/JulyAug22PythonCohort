#countdown
def countdown(num):
    for i in range(num, 0, -1):
        print(i)

#print and return
def print_and_return(arr):
    print(arr[0])
    return arr[1]

# first plus length
def first_plus_length(arr):
    return arr[0] + len(arr)

#values greater than second
def values_greater_than_second(arr):
    newArr = []
    if len(arr) <= 1:
        return False
    for i in arr:
        if arr[i] > arr[1]:
            newArr.append(arr[i])
            print(len(newArr))
            return newArr

#this length, that value
def lengthAndValue(size, value):
    newArr = []
    for i in range(0, size):
        newArr.append(value)
        return newArr