def hourglassSum(arr):
    fila = len(arr) - 2
    columna = len(arr[0]) - 2
    vacio = []

    for i in range(fila):
        for j in range(columna):
            arriba = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            medio = arr[i + 1][j + 1]
            bajo = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

            suma = arriba + medio + bajo
            vacio.append(suma)

    return max(vacio)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)