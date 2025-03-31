import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_excel('data/dados.xlsx', header=None, names=['Categoria', 'Valor'], engine='openpyxl')

print(dados.head())

plt.figure(figsize=(10, 6))
plt.bar(dados['Categoria'], dados['Valor'], color='blue')
plt.title('Gráfico de Barras')
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()