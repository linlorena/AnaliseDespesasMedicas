# Análise de Despesas Médicas com Pandas e Matplotlib

Este projeto realiza uma análise exploratória das despesas médicas com base em um conjunto de dados de seguros de saúde. Utiliza as bibliotecas `pandas` para manipulação de dados e `matplotlib` para visualização. A análise foca em identificar diferenças nas despesas médicas entre fumantes e não fumantes, bem como a influência da faixa etária e do sexo.

## Conjunto de Dados

O conjunto de dados utilizado é o `insurance.csv`, que contém as seguintes colunas:

- `idade`: Idade do indivíduo
- `sexo`: Sexo do indivíduo (masculino ou feminino)
- `imc`: Índice de Massa Corporal (IMC)
- `filhos`: Número de filhos que o indivíduo possui
- `fumante`: Indica se o indivíduo é fumante (yes ou no)
- `regiao`: Região onde o indivíduo reside
- `despesas`: Despesas médicas do indivíduo

## Pré-processamento dos Dados

1. **Renomeação das colunas**:
    ```python
    df.columns = ['idade', 'sexo', 'imc', 'filhos', 'fumante', 'regiao', 'despesas']
    ```

2. **Verificação e remoção de valores nulos**:
    ```python
    print("Contagem de valores nulos por coluna:")
    print(df.isnull().sum())
    df.dropna(inplace=True)
    ```

3. **Criação de faixas etárias**:
    ```python
    df['faixa_etaria'] = pd.cut(df['idade'],
                                bins=[18, 28, 38, 48, 58, 64],
                                labels=['18-27', '28-37', '38-47', '48-57', '58-64'])
    ```

## Análise

### Médias de Despesas Médicas por Faixa Etária e Hábito de Fumar

As médias das despesas médicas foram calculadas para diferentes faixas etárias e hábitos de fumar:
```python
medias = df.groupby(['faixa_etaria', 'fumante'], observed=False)['despesas'].mean().unstack()

medias['porcentagem'] = ((medias['yes'] - medias['no']) / medias['no']) * 100

print("\nMédias de DESPESAS MÉDICAS por FAIXA ETÁRIA e HÁBITO DE FUMAR:")
print(medias)
