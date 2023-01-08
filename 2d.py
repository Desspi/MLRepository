list = list(range(5,15,1))
def secondInaRow(lista1): 
    second = [lista1[index] for index in range(0, len(list), 2)]
    print(second)

secondInaRow(list)