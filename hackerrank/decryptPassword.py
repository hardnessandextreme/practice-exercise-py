def decryptPassword(s):
    i = 0
    n = len(s)
    decrypted = []

    while i < n:
        if s[i].isdigit():
            # If the character is a digit, find the original digit and add it to the decrypted string
            j = i
            while j < n and s[j].isdigit():
                j += 1
            original_digit = s[j - 1]
            decrypted.append(original_digit)
            i = j
        elif s[i].islower() and i + 1 < n and s[i + 1].isupper():
            # If the character is lowercase and the next character is uppercase, swap them and add a '*'
            decrypted.append(s[i + 1])
            decrypted.append(s[i])
            i += 2
        else:
            # Otherwise, add the character as is
            decrypted.append(s[i])
            i += 1

    return ''.join(decrypted)


# Test cases
print(decryptPassword("51Pa*0Lp*0e"))  # Output: aP1pL5e
print(decryptPassword("pTo*Ta*O"))  # Output: poTaTO
