class FoodOrder:
    def __init__(self,customer_name,item,price):
        self.customer_name = customer_name
        self.item = item
        self.price = price
    def show_order(self):
        print("Customer Name: {}".format(self.customer_name))
        print("Item: {}".format(self.item))

order1 = FoodOrder("Aiswarya","Pizza",100)
order2 = FoodOrder("Ayushma","Momo",200)
order3 = FoodOrder("Sima","Burger",300)
print("Order-1:\n",order1.customer_name,order1.item,order1.price)
print("Order-2:\n",order2.customer_name,order1.item,order1.price)
print("Order-3:\n",order3.customer_name,order1.item,order1.price)
order1.show_order()
order2.show_order()
order3.show_order()
