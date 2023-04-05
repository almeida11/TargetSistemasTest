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