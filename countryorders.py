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
        for product_id in self.products:
            print(f"{product_id} totals: {self.products[product_id].get_report()}")


