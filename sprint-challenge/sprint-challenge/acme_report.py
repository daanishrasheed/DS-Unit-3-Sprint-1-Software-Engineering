from random import randint, sample, uniform, choice
from acme import Product


# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        first = choice(ADJECTIVES)
        second = choice(NOUNS)
        name = Product(" ".join([first, second]))
        weight = randint(5,100)
        price = randint(5,100)
        flammability = uniform(0.0,2.5)
        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):
  names_list = [prod.name for prod in products]
  names_total = len(list(set(names_list)))
  price_list = [prod.price for prod in products]
  price_avg = sum(price_list) / len(price_list)
  weight_list = [prod.weight for prod in products]
  weight_avg = sum(weight_list) / len(weight_list)
  flammy_list = [prod.flammability for prod in products]
  flammy_avg = sum(flammy_list) / len(flammy_list)
  print("ACME CORP. OFFICIAL INVENTORY REPORT")
  print("Unique product names:", {names_total})
  print("Average price:", {price_avg})
  print("Average weight:", {weight_avg})
  print ("Average flammability:", {flammy_avg})

if __name__ == '__main__':
    inventory_report(generate_products())