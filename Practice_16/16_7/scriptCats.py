from classCat import Cat

cats = [
  {
    "name": "Сэм",
    "gender": "мальчик",
    "age": 2
  },
  {
    "name": "Мурка",
    "gender": "девочка",
    "age": 1
  },
  {
    "name": "Пушок",
    "gender": "мальчик",
    "age": 3
  }
]



for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(cat_obj.name)
    print(cat_obj.gender)
    print(cat_obj.age)
