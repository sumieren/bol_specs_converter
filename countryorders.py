from product import Product

class CountryOrders:
    def __init__(self, country):
        self.country = country
        self.products = {}

    def add_order(self, product_id, title, unit_price, amount):
        if product_id not in self.products:
            self.products[product_id] = Product(product_id, title)

        self.products[product_id].add_order(unit_price, amount)

    def report(self):
        print(f"{self.country} total: {self.get_country_total()}")
        for product_id in self.products:
            print(f"{product_id} totals: {self.products[product_id].get_report()}")

    def get_country_total(self):
        sum = 0

        for product_id in self.products:
            sum += self.products[product_id].get_total()

        return round(sum, 2)
    
    def get_orders(self, product_id):
        print(self.products[product_id].get_orders())


