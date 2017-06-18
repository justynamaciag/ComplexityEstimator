#this is example program to test function

from random import randint

    
def cleaner():
    return
    #print("Cleaning")


def struct(n):
    tablica = []
    for i in range(0, n):
        tablica.append(randint(1, 50))
    return tablica

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)

def insertionsort( aList ):
 for i in range( 1, len( aList ) ):
   tmp = aList[i]
   k = i
   while k > 0 and tmp < aList[k - 1]:
       aList[k] = aList[k - 1]
       k -= 1
   aList[k] = tmp
   return aList

