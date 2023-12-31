class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name=name
        self.chef=None
        self.server=None
        self.manager=None
        self.orders=[]
        self.rent=rent
        self.menu=menu
        self.revenue=0
        self.expense=0
        self.balance=0
        self.profit=0

    def add_employee(self,employee_type,employee):
        if employee_type =='chef':
            self.chef=employee
        elif employee_type=='server':
            self.server=employee
        elif employee_type == 'manager':
            self.manager=employee
    def receive_payment(self,order,amount,customer):
        if amount>=order.bill:
            self.revenue+=order.bill
            self.balance+=order.bill
            customer.due_amount=0
            return amount-order.bill
        else:
            print("Not Enough Money, Pay More")
    def add_order(self,order):
        self.orders.append(order)
    def pay_expense(self,amount,description):
        if amount< self.balance:
            self.expense+=amount
            self.balance-=amount
            print(f'Expense {amount} for {description}')

    def pay_salary(self,employee):
        print(f'Paying salary for {employee.name} salary {employee.salary}')
        if employee.salary<self.balance:
            self.balance-=employee.salary
            self.expense+=employee.salary
            employee.receive_salary()
    def show_employee(self):
        print("-------------Showing Employee---------------")
        if self.chef is not None:
            print(f'Chef : {self.chef.name} with Salary : {self.chef.salary}')
        if self.server is not None:
            print(f'Server : {self.server.name} with Salary : {self.server.salary}')
        if self.manager is not None:
            print(f'Manager : {self.manager.name} with Salary : {self.manager.salary}')