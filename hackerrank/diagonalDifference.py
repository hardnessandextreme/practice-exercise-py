def diagonalDifference(ar: list):
    izq = 0
    dere = 0
    for index, array in enumerate(ar):
        izq = izq + (array[index])
        dere = dere + (array[len(array) - 1 - index])
    if izq > dere:
        result = izq - dere
    elif dere > izq:
        result = dere - izq
    else:
        result = izq - dere
    print(result)

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

    for values in arr:
        for element in values:
            if element > 100 or element < -100:
                raise Exception("The value must be between -100 and 100")

    if len(arr[_]) != n:
        raise Exception("List length must be equals to number")

diagonalDifference(arr)