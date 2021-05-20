# Os números são a soma dos números imediatamente anteriores na sequencia
def função(lst, soma, x):
    tamanho = len(lst)
    while x < tamanho:
        lst[x] = soma
        return função(lst, soma+lst[x-1], x+1)

x = int(input('Digite o valor de n: '))

lista = [0]*x
lista[0] = 1
função(lista, lista[0], 1)
print(lista[-1])
print(lista)