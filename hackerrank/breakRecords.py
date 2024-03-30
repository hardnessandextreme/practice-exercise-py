
def breakingRecords(scores):
    highest = []
    lowest = []
    alto = scores[0]
    bajo = scores[0]

    for i in range(len(scores)):
        if scores[i] > alto:
            alto = scores[i]
            highest.append(alto)
        elif scores[i] < bajo:
            bajo = scores[i]
            lowest.append(bajo)
        else:
            pass

    x = [len(highest),len(lowest)]
    x = ' '.join(map(str, x))
    return x

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)