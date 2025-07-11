import pandas as pd
import numpy as np

# Criando dados fictícios de alunos
np.random.seed(123)

dados = {
    'Aluno': [f'Aluno_{i}' for i in range(1, 21)],
    'Matemática': np.random.randint(0, 11, 20),
    'Português': np.random.randint(0, 11, 20),
    'História': np.random.randint(0, 11, 20),
    'Faltas': np.random.randint(0, 10, 20)
}

df = pd.DataFrame(dados)
print("DataFrame original:")
print(df.head())

df['Média'] = df[['Matemática', 'Português', 'História']].mean(axis=1).round(1)

df['Situação'] = np.where(df['Média'] >= 7, 'Aprovado', 'Reprovado')

print("\n=== Estatísticas Descritivas ===")
print(df.describe())

print("\n=== Top 5 Melhores Médias ===")
print(df.sort_values('Média', ascending=False).head())

print("\n=== Alunos Reprovados ===")
print(df[df['Situação'] == 'Reprovado'][['Aluno', 'Média']])

print("\n=== Correlação entre Faltas e Média ===")
correlação = df['Faltas'].corr(df['Média'])
print(f"Correlação: {correlação:.2f}")
print("(Quanto mais próximo de -1, mais as faltas afetam negativamente a média)")
