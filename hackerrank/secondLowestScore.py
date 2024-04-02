def secondLowestScore(lista: list[float]) -> str:
    v = {i[0]:i[1] for i in lista}
    l = sorted(list(set(v.values())))

    for i in sorted(v.keys()):
        if v[i] == l[1]:
            print(i)


if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name, score])
    
    
    secondLowestScore(lista)