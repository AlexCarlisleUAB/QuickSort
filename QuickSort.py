import time
def Quicksort(A,p,r):
    if p < r:
        q = Part(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A, q + 1, r)        
def Part (A,p,r):
    pivot = A[r] #setting a pivot value
    i = p - 1 #The pointer for the split between < pivot and > pivot 
    for j in range (p, r-1): #J pointer is for the index where we have seen and have not seen yet
        if A[j] <= pivot: #each value that is less than pivot will be moved to left of i pointer
            i = i + 1 #increment  i pointer to adjust for new elm added to left of pointer
            temp = A[j] #holding value of A[j]
            A[j] = A[i] #place we're looking at receives the A[i] value
            A[i] = temp #place where the i pointer is receives the A[j] value stored in temp
    temp2 = A[r] #using temp variable to hold the pivot value
    A[r] = A[i + 1] #pivot place becomes the value on the right of i pointer
    A[i + 1] = temp2 #place to the right of the i pointer receives the pivot value   
    return i + 1
def ReadFile(name):
    file = open(name)
    A = file.read().split()
    return A

B = ["100.txt", "1000.txt", "5000.txt", "50000.txt", "100000.txt", "500000.txt"] #input files
for i in B:
    f = ReadFile(i)
    y = len(f) - 1
    start = time.time()
    Quicksort(f, 0, y)
    end = time.time()
    t = end-start
    yHalf = int(y/2) 
    median = f[yHalf]
    print(i, " time: ", t)
    print(i, " median: ", median)



        
            