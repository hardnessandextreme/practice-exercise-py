def countingValleys(steps, path):
    sea_level = 0
    count_valleys = 0
    hike = 0

    for step in path:
        if step == "U":
            hike += 1
        elif step == "D":
            hike -= 1
        else:
            raise Exception("Step must be U or D")

        if hike == 0 and step == "U":
            count_valleys += 1
    return count_valleys

if __name__ == '__main__':
    steps = int(input().strip())

    if steps < 2 or steps > pow(10,6):
        raise Exception("Steps must be higher than 2 and lower than pow(10,6)")

    path = input()

    if len(path) != steps:
        raise Exception("Paths length must be equals to number os steps")

    result = countingValleys(steps, path)

    print(result)