class Client:

    def __init__(self, name, family, city, balans):
        self.name = name
        self.family = family
        self.city = city
        self.balans = balans

    def file_client(self):
        return f'{self.name} {self.family}. {self.city}.'


clients1 = Client('Иван', 'Петров', 'Москва', 50)
clients2 = Client('Вася', 'Пупкин', 'Воркута', 0)
clients3 = Client('Изольда', 'Незабалуй', 'Пятигорск', 0)

posetiteli = [clients1, clients2, clients3]

for bilet in posetiteli:
    print(bilet.file_client())
