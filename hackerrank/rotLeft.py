def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))

    x = ' '.join(map(str, a))
    return x

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)