my_family = ['Я','Сестра','Мама','Папа','Бабушка','Дедушка','Тётя','Дядя']


my_family_height = [
    ['Я', 173],
    ['Сестра', 160],
    ['Мама', 168],
    ['Папа', 178],
    ['Бабушка', 165],
    ['Дедушка', 170],
    ['Тётя', 164],
    ['Дядя', 177]
]

for i in my_family_height:
    if i[0] == 'Папа':
        print(f'Рост отца - {i[1]} см')
        break


Allheight = 0
for j in my_family_height:
    Allheight += j[1]

print(f'Общий рост моей семьи - {Allheight} см')