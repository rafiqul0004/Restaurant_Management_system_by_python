class Food:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
        self.cooking_time=15
class Burger(Food):
    def __init__(self, name, price,meat,ingredients) -> None:
        super().__init__(name, price)
        self.meat=meat
        self.ingredients=ingredients
class Pizza(Food):
    def __init__(self, name, price,size,toppings) -> None:
        super().__init__(name, price)
        self.size=size
        self.toppings=toppings
class Drinks(Food):
    def __init__(self, name, price,iscold=True) -> None:
        super().__init__(name, price)
        self.iscold=iscold
class Menu:
    def __init__(self) -> None:
        self.burgers=[]
        self.pizzas=[]
        self.drinks=[]
    def add_menu_item(self,item_type,item):
        if item_type=='burger':
            self.burgers.append(item)
        elif item_type=='pizza':
            self.pizzas.append(item)
        elif item_type=='drinks':
            self.drinks.append(item)
    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
    def show_menu(self):
        for burger in self.burgers:
            print(f'Name : {burger.name} Price : {burger.price}')
        for pizza in self.pizzas:
            print(f'Name : {pizza.name} Price : {pizza.price}')
        for drink in self.drinks:
            print(f'Name : {drink.name} Price : {drink.price}')