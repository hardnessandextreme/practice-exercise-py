def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps

if __name__ == '__main__':
    n = int(input().strip())

    if n > 100 or n < 2:
        raise Exception("The number of clouds must be between 2 and 100")

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)