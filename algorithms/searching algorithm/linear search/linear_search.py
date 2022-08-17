# Implement linear search algorithm


# In General way --
def linear_search(L, X):
    n = len(L)
    i = 0
    while i < n:
        if L[i] == X:
            return X
        i += 1

    i = -1

    return i


NumberOfList = [1, 2, 3, 4, 5, 6, 7, 99]

print(linear_search(NumberOfList, 2))


#  Apply programming language features to write less code but same performance
def Linear_Search(L, X):
    n = len(L)

    for i in range(n):
        if L[i] == X:
            return "Number found ", X

    return -1


NumberOfList = [1, 2, 3, 4, 5, 6, 7, 99]

print(Linear_Search(NumberOfList, 99))


"""
-- Space Complexity O(1) -- Because the the algorithm is not part of the list ,, it will take by default

-- Time Complexity O(n) -- Worst Case 

-- Time Complexityh O(1) -- Best Case 
"""
