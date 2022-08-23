

def binary_search(L, X):
    left, right = 0, len(L) - 1
    while left <= right:
        mid = (left + right) // 2

        if L[mid] == X:
            return mid

        if L[mid] < X:
            left = mid + 1

        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 5
    position = binary_search(L, x)
    if position == -1:

        if x in L:
            print(x, " Is in L , but function returned -1  ")
        else:
            print(x, " Not in list ")
    else:
        if L[position] == x:
            print(x, "found ")
        else:
            print("Binary search search returned ", position,
                  " for ", x, " which is incorrect ")
    print("Program terminated")
