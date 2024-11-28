class Food(object):
    def drink(self):
        return ['Water', 'Cola']

    def allergen(self):
        return []


class Meat(Food):
    def drink(self):
        return ['Red wine'] + super(Meat, self).drink()


class Milk(Food):
    def allergen(self):
        return ['Milk-protein'] + super(Milk, self).allergen()


class Flour(Food): pass


class Rabbit(Meat):
    def drink(self):
        return ['Novello wine'] + super(Rabbit, self).drink()


class Pork(Meat):
    def drink(self):
        return ['Sovinion wine'] + super(Pork, self).drink()

    def allergen(self):
        return ['Pork-protein'] + super(Pork, self).allergen()


class Pasty(Milk, Flour): pass


class Pie(Rabbit, Pork, Pasty):
    def drink(self):
        return ['Mineral water'] + super().drink()


if __name__ == "__main__":
    pie = Pie()
    print(pie.__class__.mro())
    print(Pie.__mro__)

    # print('List of allergens: ')
    # for allergen in pie.allergen():
    #     print(' - ' + allergen)

    print('List of recommended drinks: ')
    for drink in pie.drink():
        print(' - ' + drink)
