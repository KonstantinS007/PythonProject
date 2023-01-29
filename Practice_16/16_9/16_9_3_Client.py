class Client:
    def __init__(self, name, family, city, balans):
        self.name = name
        self.family = family
        self.city = city
        self.balans = balans

    def __str__(self):
        return f'"{self.name} {self.family}. {self.city}. Баланс: {self.balans} руб."'


client1 = Client('Иван', 'Петров', 'Москва', 50)
print(client1)
