vat = 1.21

class Product:
    def __init__(self, product_id, title):
        self.product_id = product_id
        self.title = title
        self.orders = []

    # order format = [amount, unit_price, price_no_vat, order_total]
    def add_order(self, unit_price, amount):
        price_no_vat = round(unit_price / vat, 2)
        order_total = amount * unit_price

        self.orders.append([amount, unit_price, price_no_vat, order_total])
        print(f"added order")

    def get_orders(self):
        return self.orders
    
    def get_report(self):
        amount = 0
        prices = []
        prices_no_vat = []
        order_total = 0.00

        # for each order, add their values
        for order in self.orders:
            amount += order[0]
            prices.append(order[1])
            prices_no_vat.append(order[2])
            order_total += order[3]

        # finally, calculate the averages
        average_price = round(sum(prices) / len(prices), 2)
        average_vatless = round(sum(prices_no_vat) / len(prices_no_vat), 2)

        return [amount, average_price, average_vatless, order_total]

    def get_product_id(self):
        return self.product_id