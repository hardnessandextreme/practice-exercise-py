def insertar(lista: list, number: int, index: int) -> None:
    lista.insert(index, number)

def imprimir(lista: list) -> None:
    print(lista)

def remover(lista: list, number: int) -> None:
    lista.remove(number)

def añadir(lista: list, number: int) -> None:
    lista.append(number)

def ordenar(lista: list) -> None:
    lista.sort()

def desaparecer(lista: list) -> None:
    lista.pop()

def reversa(lista: list) -> None:
    lista.reverse()


if __name__ == '__main__':
    N = int(input())
    lista = []
    pusado = []

    for _ in range(N):
        linea = input().split()
        comando = linea[0]

        if comando == "insert":
            index = int(linea[1])
            numero = int(linea[2])
            insertar(lista, numero, index)
        elif comando == "print":
            listo = lista.copy()
            pusado.append(listo)
        elif comando == "remove":
            numero = int(linea[1])
            remover(lista, numero)
        elif comando == "append":
            numero = int(linea[1])
            añadir(lista, numero)
        elif comando == "sort":
            ordenar(lista)
        elif comando == "pop":
            desaparecer(lista)
        elif comando == "reverse":
            reversa(lista)
        
    for i in pusado:
        print(i)

        #print(comando, index, numero)