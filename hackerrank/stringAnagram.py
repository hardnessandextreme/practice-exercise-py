from collections import Counter

def contar_anagramas(lista1, lista2):
    resultado = []
    for palabra2 in lista2:
        contador_palabra2 = Counter(palabra2)
        contador_anagramas = 0
        for palabra1 in lista1:
            if Counter(palabra1) == contador_palabra2:
                contador_anagramas += 1
        resultado.append(contador_anagramas)
    return resultado

# Ejemplo de uso
list1 = ['najo', 'popo', 'oopp', 'broli', 'ppoo']
list2 = ['jona', 'poop', 'libro']
devolver = contar_anagramas(list1, list2)
print(devolver)  # Salida: [1, 3, 1]
