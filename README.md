# TargetSistemas
 
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
### IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

## Solução - 2 - Fibonacci.py
```
guess = int(input("Digite um número: "))

LastTerm, LastButOne = 0, 1
while True:
    Fibonacci = LastTerm + LastButOne
    LastButOne = LastTerm
    LastTerm = Fibonacci
    if guess == Fibonacci:
        print(f"Your guess was in the sequel: {guess}")
        break
    elif Fibonacci > guess:
        print("Your guess was out of sequence!!")
        break
```

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
### IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

## Solução - 3 - Invoicing.py
```
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
```

4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

## Solução - 4 - PercentageOfRepresentation.py
```
data = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53}

class Invoicing():
    def Sum(self):
        total = 0
        for i in data:
             total = data[i] +  total
        return  total
    
    def Percent(self, data): 
        value = {}
        total = Invoicing.Sum(self)
        for i in data:
            value[i] = ((data[i] / total) * 100) 
        return value
    
    def getPercent(self, data):
        result = ""
        value = Invoicing.Percent(self, data)
        for i in value:
            result += (f"{i}: {value[i]:.2f}%\n")
        if not result:
            result = "Não há dados de faturamento!"
        else:
            result = "Percentual de faturamento mensal por Estado de uma distribuidora:\n" + result 
        return result

FaturamentoTarget = Invoicing()
try:
    print(FaturamentoTarget.getPercent(data))
except:
    print("Erro! Problema ao ler os dados de faturamento!")
```

5) Escreva um programa que inverta os caracteres de um string.

### IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

## Solução - 5 - InvertString.py
```
def reverseText(text):
    reverse = ""
    for i in range(len(text)-1, -1, -1):
        reverse += text[i]
    return reverse

try:
    text = str(input("Insert text: "))
    reverse = reverseText(text)
    print(reverse)
except:
    print("Unable to identify text!")
```
