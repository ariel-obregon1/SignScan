import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Cargar datos
df = pd.read_csv("datos.csv", header=None)

# Separar X (datos) y y (etiquetas)
X = df.iloc[:, 1:]  # coordenadas
y = df.iloc[:, 0]   # letra

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Modelo
model = RandomForestClassifier(n_estimators=200, max_depth=10)
model.fit(X_train, y_train)

# Evaluación
accuracy = model.score(X_test, y_test)
print(f"Precisión: {accuracy*100:.2f}%")

# Guardar modelo
with open("modelo.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modelo guardado")
