def aVeryBigSum(ar:list):
    n = sum(ar)
    return n


count = int(input().strip())
ar = list(map(int, input().rstrip().split()))

if len(ar) > count:
    raise Exception("Array lenght must be less than or equal to numbers")

resultado = aVeryBigSum(ar)

print(resultado)