def sockMerchant(ar):
    sort_socks = sorted(ar)
    seen = set()
    pairs = 0

    for i in range(0, len(sort_socks)):
        if sort_socks[i] not in seen:
            seen.add(sort_socks[i])
        else:
            pairs += 1
            seen.remove(sort_socks[i])
    return pairs

if __name__ == '__main__':
    n = int(input().strip())

    if n < 1 or n > 100:
        raise Exception("The number of socks in pile must be between 1 and 100")

    ar = list(map(int, input().rstrip().split()))

    if len(ar) > n:
        raise Exception("Too many socks in socks pile")

    result = sockMerchant(ar)

    print(result)