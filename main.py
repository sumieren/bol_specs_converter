import csv, sys
from product import Product
from countryorders import CountryOrders


def main():
    # check if a single file was input
    if len(sys.argv) == 1:
        raise Exception("no file provided")
    if len(sys.argv) > 2:
        raise Exception("too many arguments provided")

    data = None

    # import the csv
    try:
        # File operations within the with block
        with open(sys.argv[1], "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data = list(csv_reader)
    except FileNotFoundError:
        print(f"Error: Could not find file '{sys.argv[1]}'")
        return
    except PermissionError:
        print(f"Error: No permission to read '{sys.argv[1]}'")
        return
    except Exception as e:
        print(f"Exception occurred: {e}. Did you save the CSV in unicode?")
        return

    # turns the read data into a list we can use
    header = data[0]
    rows = data[1:]

    nl_orders = CountryOrders("NL")
    be_orders = CountryOrders("BE")

    convert_data(data, nl_orders, be_orders)

    #be_orders.get_orders(8718101100902)

    nl_orders.report()
    be_orders.report()

# takes the raw data from the CSV and turns it into something useful.. and readable 
# data structure = dictionary with product id as key. Inside is the title and a list of orders
def convert_data(data, nl_data, be_data):
    # only use these rows, ignore the rest
    useful_types = ["Correctie verkoopprijs artikel(en)", "Verkoopprijs artikel(en), ontvangen van kopers en door bol.com door te storten"]

    for row in data:
        if row[0] in useful_types:
            product_id = int(row[2])
            title = row[3]
            total_price = -float(row[12])
            amount = int(row[6])

            country = row[13]

            # if its a return, set amount to negative
            if row[0] == "Correctie verkoopprijs artikel(en)":
                amount *= -1

            if country == "NL":
                nl_data.add_order(product_id, title, total_price, amount)
            elif country == "BE":
                be_data.add_order(product_id, title, total_price, amount)
            else:
                raise Exception("no valid country in provided row")





main()