import geopandas as gpd
import matplotlib.pyplot as plt

path_geo_forestsec1 = r"F:\projects\Forest-Hackathon\data\raw\5. Объединение фрагментированных выделов\Лесосеки-1.geojson"
path_geo_forestsec2 = r"F:\projects\Forest-Hackathon\data\raw\5. Объединение фрагментированных выделов\Лесосеки-2.geojson"
path_geo_area = r"F:\projects\Forest-Hackathon\data\raw\5. Объединение фрагментированных выделов\Выделы под лесосеками.geojson"

def load_geo(path):
    gdf = gpd.read_file(path, engine="pyogrio", use_arrow=True)
    print(f"{path.split(chr(92))[-1]}: {len(gdf)} объектов")
    print("CRS:", gdf.crs)

    # Упрощаем геометрию только для визуализации
    if gdf.crs and gdf.crs.is_geographic:
        tolerance = 0.0001
    else:
        tolerance = 10

    gdf = gdf.copy()
    gdf["geometry"] = gdf.geometry.simplify(
        tolerance=tolerance,
        preserve_topology=True
    )
    return gdf

df_geo_forestsec1 = load_geo(path_geo_forestsec1)
df_geo_forestsec2 = load_geo(path_geo_forestsec2)
df_geo_area = load_geo(path_geo_area)

fig, ax = plt.subplots(figsize=(14, 14))

df_geo_area.plot(
    ax=ax, color="lightblue", edgecolor="none",
    alpha=0.4
)

df_geo_forestsec1.plot(
    ax=ax, color="red", edgecolor="none",
    alpha=0.6
)

df_geo_forestsec2.plot(
    ax=ax, color="green", edgecolor="none",
    alpha=0.6
)

ax.set_title("Лесные данные")
ax.set_aspect("equal")
plt.show()