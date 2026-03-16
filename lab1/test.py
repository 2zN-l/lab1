# Тесты для 0 задания (distance.py) _____________________________________________________________________________________________________________________________________________

import pytest
from distance import sites, calculate_distances

# Проверка, что результат это именно словарь
def test_calculate_distances_returns_dict():
    result = calculate_distances(sites)
    assert isinstance(result, dict)


#Проверка, что расстояние - положительное число
def test_positive_distances():
    result = calculate_distances(sites)
    for city in result:
        for target in result[city]:
            assert result[city][target] > 0
            
#Проверка, что расстояния от А до Б равно расстоянию от Б до А
def test_symmetry():
    result = calculate_distances(sites)
    assert result['Moscow']['London'] == result['London']['Moscow']
    assert result['Moscow']['Paris'] == result['Paris']['Moscow']
    assert result['London']['Paris'] == result['Paris']['London']
    
    
# Тесты для 1 задания (circle.py) _____________________________________________________________________________________________________________________________________________

from circle import PI, RADIUS, calculate_area, length_comparison, point_1, point_2

#Проверка правильности подсчёта площади, используя разные радиусы
def test_area_with_different_radius():
    assert calculate_area(radius=10) == round(PI * 100, 4)
    assert calculate_area(radius=1) == round(PI, 4)

#Проверка правильность вычисления расстояния
def test_distance_calculation():
    # Точка (3, 4) должна быть на расстоянии 5 от центра
    point = (3, 4)
    assert length_comparison(point, radius=5.1) == True
    assert length_comparison(point, radius=4.9) == False
    
#Тест с отрицательным радиусом (точка никогда не может быть внутри)
def test_negative_radius():
    point = (1, 1)
    assert length_comparison(point, radius=-1) == False


# Тесты для 2 задания (operations.py) _____________________________________________________________________________________________________________________________________________


from operations import result, find_expression

#Проверка что числа 1, 2, 3, 4, 5 есть
def test_print_contains_numbers(capsys):
    find_expression()
    captured = capsys.readouterr()
    output = captured.out
    assert "1" in output
    assert "2" in output
    assert "3" in output
    assert "4" in output
    assert "5" in output
    
    
# Тесты для 3 задания (favorite_movies.py) _____________________________________________________________________________________________________________________________________________

from favorite_movies import my_favorite_movies


#Проверка на то, что строка не пустая
def test_movies_string_not_empty():
    assert len(my_favorite_movies) > 0
    
    
# Тесты для 4 задания (my_family.py) _____________________________________________________________________________________________________________________________________________

from my_family import my_family_height


#Проверка на то, что рост - положительное число
def test_positive_height():
    for person in my_family_height:
        assert person[1] > 0

#Проверка, что в списке есть папа
def test_father_exists():
    fathers = [p for p in my_family_height if p[0] == 'Папа']
    assert len(fathers) == 1
    
# Тесты для 5 задания (zoo.py) _____________________________________________________________________________________________________________________________________________

from zoo import run_zoo


#Проверка, что лев в 1 клетке
def test_lion_cell(capsys):
    run_zoo()
    captured = capsys.readouterr()
    assert "Лев сидит в клетке №1" in captured.out


#Проверка, что жаворонок в 7 клетке
def test_lark_cell(capsys):
    run_zoo()
    captured = capsys.readouterr()
    assert "Жаворонок сидит в клетке №7" in captured.out

#Проверка на правильность результата
def test_final_zoo():
    result = run_zoo() 
    assert result == ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
    
# Тесты для 6 задания (songs_list.py) _____________________________________________________________________________________________________________________________________________

from songs_list import violator_songs_list

#Проверка на сумму трёх песен из списка
def test_first_three_songs_time():
    songs_list = violator_songs_list
    time = 0
    for song in songs_list:
        if song[0] in ['Halo', 'Enjoy the Silence', 'Clean']:
            time += song[1]
    
    expected = round(4.9 + 4.20 + 5.83, 2)
    assert round(time, 2) == expected
    
# Тесты для 7 задания (secret.py) _____________________________________________________________________________________________________________________________________________

from secret import secret_message, word1


#Проверка, что в сообщении 5 строк
def test_secret_message_length():
    assert len(secret_message) == 5

#Проверка, что первое слово - буква
def test_first_word_length():
    assert len(word1) == 1
    

# Тесты для 8 задания (garden.py) _____________________________________________________________________________________________________________________________________________

from garden import garden, meadow

#Проверка, что объединение множества прошло верно
def test_union_correct():
    garden_set = set(garden)
    meadow_set = set(meadow)
    union = garden_set | meadow_set
    
    expected = {'ромашка', 'роза', 'одуванчик', 'гладиолус', 'подсолнух', 'клевер', 'мак'}
    assert union == expected
    
#Проверка пересечения множест
def test_intersection_correct():
    garden_set = set(garden)
    meadow_set = set(meadow)
    intersection = garden_set & meadow_set
    
    expected = {'ромашка', 'одуванчик'}
    assert intersection == expected
    
# Тесты для 9 задания (shopping.py) _____________________________________________________________________________________________________________________________________________

from shopping import shops, sweets

#Проверка, что для печенья выбраны магазины с минимальными ценами
def test_cookie_min_prices():
    all_prices = []
    for shop_name, products in shops.items():
        for product in products:
            if product['name'] == 'печенье':
                all_prices.append((shop_name, product['price']))
    
    all_prices.sort(key=lambda x: x[1])
    
    cheapest_two = [p[0] for p in all_prices[:2]]
    
    selected_shops = [s['shop'] for s in sweets['печенье']]
    assert set(selected_shops) == set(cheapest_two)

#Проверка, что пирожное только в пятерочке и в магните
def test_cake_shops():
    cake_shops = [s['shop'] for s in sweets['пирожное']]
    assert 'пятерочка' in cake_shops
    assert 'магнит' in cake_shops
    assert 'ашан' not in cake_shops
    
# Тесты для 10 задания (store.py) _____________________________________________________________________________________________________________________________________________

from store import goods, store

#Проверка на правильный расчёт для лампы
def test_lamp_calculation():
    lamp_code = goods['Лампа']
    lamp_item = store[lamp_code][0]
    lamp_quantity = lamp_item['quantity']
    lamp_price = lamp_item['price']
    lamp_cost = lamp_quantity * lamp_price
    
    assert lamp_quantity == 27
    assert lamp_price == 42
    assert lamp_cost == 27 * 42
    
    
#Проверка на правильный расчёт для стула
def test_chair_calculation():
    chair_code = goods['Стул']
    chair_batch1 = store[chair_code][0]
    chair_batch2 = store[chair_code][1]
    chair_batch3 = store[chair_code][2]
    
    chair_quantity_total = (chair_batch1['quantity'] + 
                            chair_batch2['quantity'] + 
                            chair_batch3['quantity'])
    chair_cost_total = (chair_batch1['quantity'] * chair_batch1['price'] + 
                        chair_batch2['quantity'] * chair_batch2['price'] + 
                        chair_batch3['quantity'] * chair_batch3['price'])
    
    assert chair_quantity_total == 50 + 12 + 43
    assert chair_cost_total == 50*100 + 12*95 + 43*97

#Проверка, что количество - целые числа
def test_quantities_are_ints():
    for code in store:
        for batch in store[code]:
            assert isinstance(batch['quantity'], int)