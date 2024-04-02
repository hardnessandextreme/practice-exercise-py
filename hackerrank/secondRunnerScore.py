def secondRunnerScore(scores: list) -> int:
    a = set(scores)
    a = sorted(list(a))
    return a[-2]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(secondRunnerScore(arr))