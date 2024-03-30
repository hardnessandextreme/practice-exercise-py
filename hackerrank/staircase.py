def staircase(n):
    for times in range(1,n+1):
        string = "#" * times
        print(string.rjust(n," "))

if __name__ == '__main__':
    n = int(input().strip())

    if n < 0 or n > 100:
        raise Exception("Value must be between 0 and 100")

    staircase(n)