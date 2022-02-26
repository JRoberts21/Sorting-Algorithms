"""
Jonathan Roberts
This program generates 10000 integers in the range of 0-1000000 and stored
The integers are then sorted through either selection sort, merge sort, or bubble sort
"""
from random import seed
from random import randint
import time

list1=[]


#generate 10000 integers
for _ in range(10000):
    value = randint(0,1000000)
    list1.append(value)



#selection sort
def selectionSort (arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
            
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
   

#merge sort
def mergeSort(arr):
    
    
    if len(arr) > 1:
        
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
              
            else:
                arr[k] = R[j]
                j += 1
                
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

       
#bubbleSort            
def bubbleSort(arr):
    n = len(arr)
  

    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
               


def printArrays():
    val = input("Enter selection, merge, or bubble: ")

    if (val == "selection"):
        tic = time.perf_counter()
        selectionSort(list1)
        toc = time.perf_counter()
        print ("Sorted array")
        for i in range(len(list1)):
            print("%d" %list1[i]),
        print(f"Sorted the integers in {toc - tic:0.4f} seconds")
    
    if (val == "merge"):
        tic = time.perf_counter()
        mergeSort(list1)
        toc = time.perf_counter()
        print (list1)
        print(f"Sorted the integers in {toc - tic:0.4f} seconds")

        #bubble sort takes a very long time
    if (val == "bubble"):
        tic = time.perf_counter() 
        bubbleSort(list1)
        toc = time.perf_counter() 
        print ("Sorted array is:")
        for i in range(len(list1)):
            print ("%d" %list1[i]),

printArrays()
