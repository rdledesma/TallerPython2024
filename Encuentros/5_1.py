# Cargar el fichero
import pandas as pd
import numpy as np
file_path = 'temp.csv'

data = pd.read_csv(file_path, delimiter=';')

# Display the first few rows and columns
data.head(), data.columns


# Replace commas with dots and convert to numeric for applicable columns
for column in ['promedio', 'máx', 'mín']:
    data[column] = data[column].str.replace(',', '.').astype(float)

# Convert "Fecha / Hora" to datetime
data['date'] = pd.to_datetime(data['Fecha / Hora'])

# Verify the cleaned data
data.info(), data.head()



# Convertimos las columnas a arrays de NumPy
promedio_np = data['promedio'].values
max_np = data['máx'].values
min_np = data['mín'].values

# Estadísticas básicas
stats = {
    'Columna': ['promedio', 'máx', 'mín'],
    'Media': [np.mean(promedio_np), np.mean(max_np), np.mean(min_np)],
    'Mediana': [np.median(promedio_np), np.median(max_np), np.median(min_np)],
    'Desviación Estándar': [np.std(promedio_np), np.std(max_np), np.std(min_np)]
}

stats_df = pd.DataFrame(stats)
print(stats_df)


import matplotlib.pyplot as plt

# Gráfico de tendencias
plt.figure(figsize=(12, 6))
plt.plot(data['date'], promedio_np, label='Promedio', color='blue')
plt.title('Tendencia de Promedio a lo largo del tiempo')
plt.xlabel('Fecha / Hora')
plt.ylabel('Promedio')
plt.legend()
plt.grid()
plt.show()




# Agregar día de la semana
data['Día Semana'] = data['date'].dt.dayofweek  # 0 = Lunes, 6 = Domingo

# Pivot table
heatmap_data = data.pivot_table(values='promedio', index='Día Semana', columns='Hora', aggfunc='mean')

# Heatmap
plt.figure(figsize=(12, 6))
plt.imshow(heatmap_data, cmap='coolwarm', aspect='auto')
plt.colorbar(label='Promedio')
plt.title('Promedio por Día de la Semana y Hora')
plt.xlabel('Hora del Día')
plt.ylabel('Día de la Semana')
plt.xticks(ticks=range(24), labels=range(24))
plt.yticks(ticks=range(7), labels=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
plt.show()


