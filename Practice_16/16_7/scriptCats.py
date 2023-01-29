import json

from classCat import Cat
with open('jsonCats.json', encoding='utf8') as f:
    cats = json.load(f)


for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(cat_obj.name)
    print(cat_obj.gender)
    print(cat_obj.age)
