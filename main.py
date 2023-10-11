from Menu import Burger,Pizza,Drinks,Menu
from restaurant import Restaurant
from user import User,Manager,Server,Chef,Customer
from order import Order
def main():
    menu=Menu()
    pizza_1=Pizza('Chicken pizza',700,'Large',['chicken','oil'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('Alur Vorta Pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    ##Add burger
    burger_1=Burger('Naga',700,'chicken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)

    #Add drinks
    coke=Drinks('Coke',35,True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('Capachino', 300, False)
    menu.add_menu_item('drinks', coffee)
    
    #show Menu
    # menu.show_menu()
    #Add employee
    RR=Restaurant("RR Restro",5000,menu)
    manager = Manager('Kala Chan Manager', 5, 'kala@chan.com', 'kaliapur', 1500, 'Jan 1 2020', 'core')
    RR.add_employee('manager',manager)
    chef = Chef('Rustom Baburchi', 6, 'chupa@rustom.com', 'rustomNagar', 3500, 'Feb 1, 2020', 'Chef', 'everything')
    RR.add_employee('chef', chef)
    server = Server('Chotu server', 6, 'nai@jai.com', 'restaurant', 200, 'March 1, 2020', 'server')
    RR.add_employee('server', server)

    #Show employee
    # RR.show_employee()
    customer_1 = Customer('Hande Ercel', 6, 'queen@gmail.com', "Some Where", 100000)
    order_1 = Order(customer_1, [pizza_3, coke, burger_1, pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    RR.add_order(order_1)
    # customer one paying for order_1
    RR.receive_payment(order_1, 20000, customer_1)
    print('revenue and balance after first customer', RR.revenue, RR.balance)
    
    # customer 2 placing an order
    customer_2 = Customer('Rahat', 6, 'kr@gmail.com', "No Where", 100000)
    order_2 = Order(customer_2, [pizza_1, burger_2, burger_1, pizza_2, coffee])
    customer_2.pay_for_order(order_2)
    RR.add_order(order_2)
    # customer one paying for order_1
    RR.receive_payment(order_2, 10000, customer_2)

    print('revenue and balance after second customer', RR.revenue, RR.balance)

    # pay rent
    RR.pay_expense(RR.rent, 'Rent')
    print('after rent', RR.revenue, RR.balance, RR.expense)

    RR.pay_salary(chef)
    print('after salary', RR.revenue, RR.balance, RR.expense)
if __name__ == '__main__':
    main()