import json

with open("dados.json", encoding='utf-8') as dados:
    data = json.load(dados)

def getValues():
    data_higher = []
    for i in range(len(data)):
        if (data[i]["valor"] != 0):
             data_higher.append(data[i]["valor"])

    HighestValue = max(int(number) for number in data_higher)
    LowerValue = min(int(number) for number in data_higher)
    Average = (sum(data_higher)) / (len(data_higher))
    HigherBilling = 0
    for i in data_higher:
        if (i > Average):
            HigherBilling += 1

    print(f"O menor valor de faturamento ocorrido em um dia do mês: R$ {LowerValue},00")
    print(f"O maior valor de faturamento ocorrido em um dia do mês: R$ {HighestValue},00")
    print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {HigherBilling} dias")

getValues()
