class Coffee:
    coffee = {
        'капучино': ['эспрессо', 'молоко'],
        'латте': ['эспрессо', 'молоко', 'молочная пена'],
        'глясе': ['эспрессо', 'мороженое']
    }

    def get_cappuccino(self):
        return self.coffee['капучино']

    def get_latte(self):
        return self.coffee['латте']

    def get_glace(self):
        return self.coffee['глясе']


def print_result():
    coffee = Coffee()
    print(f"Заказываем капучино: " + ' + '.join(coffee.get_cappuccino()))
    print(f"Заказываем латте: " + ' + '.join(coffee.get_latte()))
    print(f"Заказываем глясе: " + ' + '.join(coffee.get_glace()))


print_result()
