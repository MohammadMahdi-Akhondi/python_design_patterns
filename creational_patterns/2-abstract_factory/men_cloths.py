from abc import ABC, abstractmethod


class Shirt(ABC):
    @abstractmethod
    def create_cotton(self): pass

    @abstractmethod
    def create_li(self): pass


class TShirt(Shirt):
    def create_li(self):
        print('TShirt', end=" ")
        return Li()

    def create_cotton(self):
        print('TShirt', end=" ")
        return Cotton()


class DressShirt(Shirt):
    def create_li(self):
        print('DressShirt', end=" ")
        return Li()

    def create_cotton(self):
        print('DressShirt', end=" ")
        return Cotton()


class Fabric(ABC):
    @abstractmethod
    def name(self): pass


class Cotton(Fabric):
    def name(self):
        print('cotton')


class Li(Fabric):
    def name(self):
        print('li')


def customer_li(shirt: Shirt):
    shirt_obj = shirt.create_li()
    shirt_obj.name()


def customer_cotton(shirt: Shirt):
    shirt_obj = shirt.create_cotton()
    shirt_obj.name()


if __name__ == '__main__':
    print('App Launched with the customer li and TShirt:')
    customer_li(TShirt())

    print('-' * 50)

    print('App Launched with the customer cotton and DressShirt:')
    customer_cotton(DressShirt())
