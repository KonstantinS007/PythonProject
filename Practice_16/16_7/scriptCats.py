from classCat import Cat
with open('dict_cats.json') as jcats:
    cats = json.load(jcats)

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(cat_obj.name)
    print(cat_obj.gender)
    print(cat_obj.age)
