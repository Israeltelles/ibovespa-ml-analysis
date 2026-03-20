import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import os

df = pd.read_csv("D:/Python/ibovespa-ml-analysis/data/all_ibovespa.csv")
df = df[df['sigla_acao'] == 'ITUB4']

df['data_pregao'] = pd.to_datetime(df['data_pregao'])

df['lag1'] = df['preco_fechamento'].shift(1)
df['lag2'] = df['preco_fechamento'].shift(2)
df['lag3'] = df['preco_fechamento'].shift(3)

df['ma5'] = df['preco_fechamento'].rolling(5).mean()
df['ma21'] = df['preco_fechamento'].rolling(21).mean()

df = df.dropna()

X = df[['lag1', 'lag2', 'lag3', 'ma5', 'ma21']]
y = df['preco_fechamento']

X_train = X.iloc[0:600]
X_test = X.iloc[600:700]

y_train = y.iloc[0:600]
y_test = y.iloc[600:700]

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

mlp = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=2000, early_stopping=True, random_state=42)
mlp.fit(X_train_scaled, y_train)
y_pred_mlp = mlp.predict(X_test_scaled)

r2_lr = r2_score(y_test, y_pred_lr)
mae_lr = mean_absolute_error(y_test, y_pred_lr)

r2_mlp = r2_score(y_test, y_pred_mlp)
mae_mlp = mean_absolute_error(y_test, y_pred_mlp)

'''print("\n" + "="*50)
print("📊 COMPARAÇÃO DE MODELOS - ITUB4")
print("="*50)

print("\n🔵 Regressão Linear")
print(f"R²   : {r2_lr:.4f} ({r2_lr*100:.2f}%)")
print(f"MAE  : {mae_lr:.4f}")

print("\n🟣 Rede Neural (MLP)")
print(f"R²   : {r2_mlp:.4f} ({r2_mlp*100:.2f}%)")
print(f"MAE  : {mae_mlp:.4f}")

print("\n📈 Melhor modelo:", "Regressão Linear" if r2_lr > r2_mlp else "Rede Neural")

print("\nCoeficientes da Regressão Linear:")
for i, coef in enumerate(lr.coef_):
    print(f"Feature {i+1}: {coef:.4f}")'''

plt.figure(figsize=(12,6))
plt.plot(y_test.values, label="Real")
plt.plot(y_pred_lr, label="Regressão Linear")
plt.plot(y_pred_mlp, label="Rede Neural")
plt.legend()
plt.title("Comparação de Modelos - ITUB4")
plt.xlabel("Tempo")
plt.ylabel("Preço")
plt.show()

resultado = pd.DataFrame({
    'data': df['data_pregao'].iloc[600:700].values,
    'preco_real': y_test.values,
    'previsao_linear': y_pred_lr,
    'previsao_mlp': y_pred_mlp
})

resultado = pd.DataFrame({
    'data': df['data_pregao'].iloc[600:700].values,
    'preco_real': y_test.values,
    'previsao_linear': y_pred_lr,
    'previsao_mlp': y_pred_mlp
})

resultado['acao'] = df['sigla_acao'].iloc[600:700].values

try:
    resultado.to_csv("D:/Python/ibovespa-ml-analysis/data/resultado_modelo.csv", index=False)
    print("Arquivo 'resultado_modelo.csv' criado com sucesso!")
except Exception as e:
    print("Erro ao salvar o arquivo:")
    print(e)

if os.path.exists("resultado_modelo.csv"):
    print("Arquivo confirmado no diretório.")