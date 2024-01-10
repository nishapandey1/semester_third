
def BinarySearch(array,x):

    low=0

    high=len(array)-1

    mid=0

    while low<=high:

        mid=(high+low)//2

        if array[mid]<x:

            low=mid+1

            # if x is greater,ignore left half

        elif array[mid]>x:

            high=mid-1

        else:

            return mid

    return -1

array=[12,5,7,90,1,6,0,2,3]

x=90

array.sort()

print(array)

result=BinarySearch(array,x)

if result!=-1:

    print("Element is present at index",str(result))

else:

    print("Element is not present in the list of arrays")