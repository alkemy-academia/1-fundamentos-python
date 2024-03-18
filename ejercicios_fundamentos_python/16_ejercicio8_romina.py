data = [{'name':'Virgin Islands(British)', 'languages':['English']},
        {'name':'Cameroon', 'languages':['English', 'French']},
        {'name':'Argentina', 'languages':['Spanish', 'Guarani']},
        {'name': 'Spain', 'languages':['Spanish']},
        {'name':'United States', 'languages':['English']}]


def conteo_lenguajes(lista):
    lenguajes = []
    for i in data:
        for j in i['languages']:
            lenguajes.append(j)
    recuento = {}
    for i in set(lenguajes):
        recuento[i] = lenguajes.count(i)
    recuento = dict(sorted(recuento.items(), key=lambda x: x[1], reverse=True))
    return recuento


print(conteo_lenguajes(data))
