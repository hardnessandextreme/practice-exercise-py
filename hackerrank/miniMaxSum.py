def miniMaxSum(arr):
    sumMax = 0
    sumMin = 0
    aux = []

    for index, numer in enumerate(arr):
        if numer < 1 or numer > pow(10,9):
            raise Exception("Values of list must be higher thab 1 and less than pow(10,9)")

        arr.pop(index)
        numero = sum(arr)
        aux.append(numero)
        arr.insert(index, numer)

    sumMax = max(aux)
    sumMin = min(aux)
    print(sumMin, sumMax)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
