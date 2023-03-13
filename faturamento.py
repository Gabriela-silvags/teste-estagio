# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

menor_faturamento = dados[0]['valor']
maior_faturamento = dados[0]['valor']

soma_faturamento = 0
for dia in dados:
    soma_faturamento += dia['valor']

media_faturamento = soma_faturamento / len(dados)

dias_acima_media = 0
for dia in dados:
    if dia['valor'] > media_faturamento:
        dias_acima_media += 1

    if dia['valor'] < menor_faturamento:
        menor_faturamento = dia['valor']
    if dia['valor'] > maior_faturamento:
        maior_faturamento = dia['valor']


print(f"Menor valor de faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento diário acima da média mensal: {dias_acima_media}")
