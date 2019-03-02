from enums.enums import Currency
from product.configurable_product import ConfigurableProduct
from product.product import Product
from attribute.attributes import *

image1 = Image("https://salt.tikicdn.com/cache/75x75/ts/product/image_a.jpg")
image2 = Image("https://salt.tikicdn.com/cache/75x75/ts/product/image_b.jpg")
image3 = Image("https://salt.tikicdn.com/cache/75x75/ts/product/image_c.jpg")


class App:
    def create_iphoneX_64gb_black(self):
        iphoneX_64_black = Product("Iphone X 64Gb Black", 999, 1099, Currency.Dollar)
        iphoneX_64_black.add_image(image1)
        iphoneX_64_black.add_image(image2)
        iphoneX_64_black.add_image(image3)
        iphoneX_64_black.set_default_image(image2)

        iphoneX_64_black.add_attributes([
            Color("Black"),
            Storage(64, StorageUnit.Gb),
            Description(
                "Điện hoại iPhone X 64GB là chiếc điện thoại hoàn toàn mới của Apple vừa mới ra mắt tuần vừa qua"),
            Origin("Trung Quoc"),
            FactoryDate(2018, 10, 12),
            Weight(174, WeightUnit.G)
        ])

        return iphoneX_64_black

    def create_iphoneX_128gb_yellow(self):
        iphoneX_128_yellow = Product("Iphone X 128Gb Yellow", 950, 1050, Currency.Dollar)
        iphoneX_128_yellow.add_image(image1)
        iphoneX_128_yellow.add_image(image2)
        iphoneX_128_yellow.add_image(image3)
        iphoneX_128_yellow.set_default_image(image2)

        iphoneX_128_yellow.add_attributes([
            Color("Yellow"),
            Storage(128, StorageUnit.Gb),
            Description(
                "Điện Thoại iPhone X 128GB là chiếc điện thoại hoàn toàn mới của Apple vừa mới ra mắt tuần vừa qua"),
            Origin("Trung Quoc"),
            FactoryDate(2018, 10, 14),
            Weight(174, WeightUnit.G)
        ])

        return iphoneX_128_yellow


app = App()
if __name__ == '__main__':
    iphoneX_64_Black = app.create_iphoneX_64gb_black()
    iphoneX_128_yellow = app.create_iphoneX_128gb_yellow()
    iphoneX = ConfigurableProduct("Iphone X", iphoneX_64_Black, iphoneX_128_yellow)
    print(iphoneX)
