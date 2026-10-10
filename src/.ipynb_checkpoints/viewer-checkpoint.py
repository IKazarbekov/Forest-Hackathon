import geopandas as gpd
import matplotlib.pyplot as plt

path_geo_forestsec1 = r"F:\projects\Forest-Hackathon\data\raw\5. Объединение фрагментированных выделов\Лесосеки-1.geojson"
path_geo_forestsec2 = r"F:\projects\Forest-Hackathon\data\raw\5. Объединение фрагментированных выделов\Лесосеки-2.geojson"
path_geo_area = r"F:\projects\Forest-Hackathon\data\raw\5. Объединение фрагментированных выделов\Выделы под лесосеками.geojson"

# Загружаем
df_geo_forestsec1 = gpd.read_file(path_geo_forestsec1)
df_geo_forestsec2 = gpd.read_file(path_geo_forestsec2)
df_geo_area = gpd.read_file(path_geo_area)

# Рисуем
fig, ax = plt.subplots(figsize=(12, 12))

df_geo_area.plot(ax=ax, color='lightblue', edgecolor='black', alpha=0.5, label='Выделы')
df_geo_forestsec1.head().plot(ax=ax, color='red', edgecolor='darkred', alpha=0.5, label='Лесосеки-1')
df_geo_forestsec2.plot(ax=ax, color='green', edgecolor='darkgreen', alpha=0.5, label='Лесосеки-2')

plt.legend()
plt.title("Лесные данные")
plt.show()