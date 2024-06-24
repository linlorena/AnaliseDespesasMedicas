import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('insurance.csv')

df.columns = ['idade', 'sexo', 'imc', 'filhos', 'fumante', 'regiao', 'despesas']

print("Contagem de valores nulos por coluna:")
print(df.isnull().sum())
df.dropna(inplace=True)

df['faixa_etaria'] = pd.cut(df['idade'],
                            bins=[18, 28, 38, 48, 58, 64],
                            labels=['18-27', '28-37', '38-47', '48-57', '58-64'])

medias = df.groupby(['faixa_etaria', 'fumante'], observed=False)['despesas'].mean().unstack()

medias['porcentagem'] = ((medias['yes'] - medias['no']) / medias['no']) * 100

print("\nMédias de DESPESAS MÉDICAS por FAIXA ETÁRIA e HÁBITO DE FUMAR:")
print(medias)

medias[['no', 'yes']].plot(kind='bar', figsize=(10, 6))
plt.title('Despesas entre Fumantes e Não Fumantes por Faixa Etária')
plt.xlabel('Faixa Etária')
plt.ylabel('Despesas Médias')
plt.xticks(rotation=45)
plt.legend(['Não Fumantes', 'Fumantes'])
plt.tight_layout()
plt.show()

fumantes_sexo = df[df['fumante'] == 'yes'].groupby('sexo')['despesas'].mean()
fumantes_sexo.plot(kind='bar', figsize=(8, 5), color=['pink', 'blue'])
plt.title('Despesas Médias de Fumantes por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Despesas Médias')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

nao_fumantes = df[df['fumante'] == 'no']
plt.figure(figsize=(10, 6))
plt.scatter(nao_fumantes['idade'], nao_fumantes['despesas'], color='green', alpha=0.5)
plt.title('Despesas por Idade entre Não Fumantes')
plt.xlabel('Idade')
plt.ylabel('Despesas Médias')
plt.grid(True)
plt.tight_layout()
plt.show()
