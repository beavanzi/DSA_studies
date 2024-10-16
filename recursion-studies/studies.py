# write a function that takes a number and prints it
# print first 5 numbers: 1 2 3 4 5

def mostrarNumeros(n):
    # Last Valid Input
    if n == 1:
        print(1)  
        return 1
    print(n)
    mostrarNumeros(n-1)
        
#mostrarNumeros(5)

def mostrarNumeros2(n):
    # First Invalid Input
    if n < 1:
        return 
    print(n)    
    mostrarNumeros2(n-1)

mostrarNumeros(5)
mostrarNumeros2(5)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n*factorial(n-1)

print(factorial(5))


def quicksort(array):
    if len(array) < 2:
        return array
    
    pivotInd = len(array)//2
    pivot = array[pivotInd]
    
    menores = [i for i in array if i < pivot]
    mid =  [i for i in array if i == pivot]
    maiores = [i for i in array if i > pivot]
    
    return quicksort(menores) + mid + quicksort(maiores)

print(quicksort([8,5,10,2,9]))