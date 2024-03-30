def repeatedString(s, n):
    if s == 'a':
        return n

    if n > 10**6:
        return s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')

    cadena = s * n
    palabra = cadena[:n]
    contador = palabra.count('a')

    return contador

if __name__ == '__main__':
    s = input()

    if len(s) < 1 or len(s) > 100:
        raise ValueError('The length of the string must be between 1 and 100')

    n = int(input().strip())

    if n < 1 or n > 10**12:
        raise ValueError('The length of the string must be between 1 and 10^12')

    result = repeatedString(s, n)

    print(result)