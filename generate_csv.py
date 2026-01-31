import numpy as np
import pandas as pd
import os

# Parametry danych
num_samples = 1000  # liczba wierszy
num_sensors = 3     # liczba czujników

# Generowanie losowych danych czujników (0-1)
np.random.seed(42)
sensors = np.random.rand(num_samples, num_sensors)

# Generowanie targetu (0 = brak awarii, 1 = awaria)
# Założenie, że awaria pojawia się gdy suma czujników > 2.0
target = (sensors.sum(axis=1) > 2.0).astype(int)

# Tworzymy DataFrame
columns = [f"sensor{i+1}" for i in range(num_sensors)]
df = pd.DataFrame(sensors, columns=columns)
df["target"] = target

# Tworzy folder data/ jeśli nie istnieje
os.makedirs("data", exist_ok=True)

# Zapis do CSV
df.to_csv("data/sensor_data.csv", index=False)

print("Plik data/sensor_data.csv został wygenerowany!")
