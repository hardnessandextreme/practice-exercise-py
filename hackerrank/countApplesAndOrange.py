def countApplesAndOranges(s, t, a, b, apples, oranges):
    # a represents location of apple tree
    # b represents location of orange tree
    # apples array contains apples fallen
    # oranges array contains oranges fallen
    manza = 0
    naran = 0

    for apple in apples:
        apple_fallen = a + (apple)
        if apple_fallen >= s and apple_fallen <= t:
            manza += 1

    for orange in oranges:
        orange_fallen = b + (orange)
        if orange_fallen >= s and orange_fallen <= t:
            naran += 1

    print(manza)
    print(naran)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
