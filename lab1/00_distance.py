# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

for site1, coords1 in sites.items():
    city_distances = {}
    for site2, coords2 in sites.items():
        if site1 != site2:
            x1, y1 = coords1
            x2, y2 = coords2
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            city_distances[site2] = round(distance,2)
    
    distances[site1] = city_distances

print(distances)



