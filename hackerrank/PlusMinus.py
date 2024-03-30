def plusMinus(arr):
    proportionalPositive = 0
    proportionalNegative = 0
    proportionalZero = 0

    for element in arr:
        if element < -100 or element > 100:
            raise Exception("Element must be between -100 and 100")

        if element == 0:
            proportionalZero += 1
        elif element > 0:
            proportionalPositive += 1
        else:
            proportionalNegative += 1

    divi = len(arr)
    result1, result2, result3 = (proportionalPositive / divi,
                                 proportionalNegative / divi,
                                 proportionalZero / divi)

    print(f"{result1:.6f}")
    print(f"{result2:.6f}")
    print(f"{result3:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    if n < 0 or n > 100:
        raise Exception("Value must be between 0 and 100")

    arr = list(map(int, input().rstrip().split()))

    if len(arr) > n:
        raise Exception("Lenght of list must be equals to n")

    plusMinus(arr)
