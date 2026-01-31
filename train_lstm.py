from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Wczytanie danych
data_path = os.path.join("data", "sensor_data.csv")

if not os.path.exists(data_path):
    raise FileNotFoundError(f"Plik {data_path} nie istnieje! Wstaw dane do folderu data/")

df = pd.read_csv(data_path)
sensor_columns = [col for col in df.columns if "sensor" in col.lower()]
target_column = "target"

X_data = df[sensor_columns].values
y_data = df[target_column].values

# Przygotowanie danych dla LSTM
time_steps = 10
num_features = len(sensor_columns)

def create_sequences(X, y, time_steps):
    Xs, ys = [], []
    for i in range(len(X) - time_steps):
        Xs.append(X[i:(i + time_steps)])
        ys.append(y[i + time_steps])
    return np.array(Xs), np.array(ys)

X, y = create_sequences(X_data, y_data, time_steps)
print(f"X shape: {X.shape}, y shape: {y.shape}")

# Tworzenie modelu LSTM
model = Sequential()
model.add(LSTM(50, input_shape=(time_steps, num_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Trening modelu
history = model.fit(X, y, epochs=20, batch_size=32, validation_split=0.2)

# Podsumowanie modelu
model.summary()

# Wizualizacja loss
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Trening LSTM - Predictive Maintenance')
plt.legend()
plt.show()

# Zapisanie modelu
model.save("lstm_model.h5")
print("Model zapisany do pliku lstm_model.h5")
