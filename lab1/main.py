
import distance
import circle
import operations
import favorite_movies
import my_family
import zoo
import songs_list
import secret
import garden
import shopping
import store


def main():
    print('ВЫБЕРИТЕ ЗАДАНИЕ:')
    print('0 - Рассчёт расстояния между городами(distance)')
    print('1 - Рассчёт площади круга, определение нахождения точки относительно круга(circle)')
    print('2 - Расставление знаков операции для вычисления выражения(operations)')
    print('3 - Выведение названий фильмов в конкретной последовательности(favorite_movies)')
    print('4 - Вывести рост отца и рост семьи(my_family)')
    print('5 - Рассадить животных по условиям (zoo)')
    print('6 - Рассчёт общего времени звучания песен (songs_list)')
    print('7 - Рассшифрование послания (secret)')
    print('8 - Работа с множествами цветов(garden)')
    print('9 - Создание словаря sweets (shopping)')
    print('10 - Рассчёт общего количества и общей стоимости каждого товара на складе (store)')

    choice = (input('Введите число:'))

    if choice == '0':
        distance.task_0()
    elif choice == '1':
        circle.task_1()
    elif choice == '2':
        operations.find_expression()
    elif choice == '3':
        favorite_movies.task_3()
    elif choice == '4':
        my_family.task_4()
    elif choice == '5':
        zoo.run_zoo()
    elif choice == '6':
        songs_list.task_6()
    elif choice == '7':
        secret.task_7()
    elif choice == '8':
        garden.task_8()
    elif choice == '9':
        shopping.task_9()
    elif choice == '10':
        store.task_10()
    else:
        print('Нет такого числа')

main()

