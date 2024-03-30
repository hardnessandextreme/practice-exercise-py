# s = Squares of chocolate
# d = Day (result of sum the squares)
# m = Month (number of squares)

def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if i + m <= len(s):
            n = s[i:i+m]
            if sum(n) == d:
                count += 1
    return count

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)