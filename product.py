vat = 1.21

class Product:
    def __init__(self, product_id, title):
        self.product_id = product_id
        self.title = title
        self.orders = []

    # order format = [amount, unit_price, price_no_vat, order_total]
    def add_order(self, total_price, amount):
        unit_price = round(total_price / amount, 2)
        price_no_vat = round((total_price / vat) / amount, 2)
        order_total = round(total_price, 2)

        # if both are negative, it is a return. preserve the -
        if total_price < 0 and amount < 0:
            unit_price *= -1
            price_no_vat *= -1

        self.orders.append([amount, unit_price, price_no_vat, order_total])

    def get_orders(self):
        return self.orders
    
    def get_report(self):
        amount = 0
        order_total = 0.00

        # for each order, add their values
        for order in self.orders:
            amount += order[0]
            order_total += order[3]

        # finally, calculate the averages
        average_price = round(order_total / amount, 2) if amount != 0 else 0
        average_vatless = round(average_price / 1.21, 2)
        total_vatless = round(order_total / 1.21, 2)


        #print(f"for product id: {self.product_id}. Adding unit price {average_price} for amount {amount} with turnover {order_total}. Turnover == average price * amount is {average_price*amount == order_total}!!")
        return amount, average_price, average_vatless, order_total, total_vatless

    def get_product_id(self):
        return self.product_id
    
    def get_title(self):
        return self.title
    
    def get_total(self):
        sum = 0

        for order in self.orders:
            sum += order[3]

        return round(sum, 2)