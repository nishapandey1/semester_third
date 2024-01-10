# # Linear Search in Python

def linearSearch(array, n, x):

    for i in range(0, n):

        if (array[i] == x):

            return i

    return -1

   

array = [1,7,44,24, 41, 31, 11, 9,23]

x = 41

n = len(array)

result = linearSearch(array, n, x)

if(result == -1):

    print("Element not found")

else:

    print("Searched Element is Present at Index Position: ", result)