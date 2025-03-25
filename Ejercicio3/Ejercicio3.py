def magia_numerica(lista):
    # Eliminar los elementos duplicados
    lista_sin_duplicados = list(set(lista))
    
    # Ordenar la lista de mayor a menor
    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
    
    # Eliminar todos los números impares
    lista_pares = [num for num in lista_ordenada if num % 2 == 0]
    
    # Sumar todos los números que quedan
    suma = sum(lista_pares)
    
    # Colocar esta suma como el primer elemento de la lista
    lista_final = [suma] + lista_pares
    
    # Verificar que la suma de todos los números a partir del segundo elemento es igual al primer número de la lista
    assert suma == sum(lista_final[1:]), "La suma de los elementos no coincide con el primer elemento"
    
    return lista_final

# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 8, 6]
resultado = magia_numerica(lista)
print(resultado)