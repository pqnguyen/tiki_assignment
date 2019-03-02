from product.product import Product


class ConfigurableProduct:
    def __init__(self, name: str, product_a: Product, product_b: Product):
        self.name = name
        self.combinations = [product_a, product_b]

    def combine(self, product: Product):
        self.combinations.append(product)

    def __str__(self):
        print("Configurable Product: ", self.name)
        for product in self.combinations:
            print("========================{product_name}========================".format(product_name=product.name))
            print(product)

        return ""
