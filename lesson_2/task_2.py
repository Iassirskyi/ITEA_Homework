class Shop:

    sales = 0


    def __init__(self, name, products):

        self.name = name
        self.products = products


    def update_products(self, new_products):

        self.products += new_products
        self.update_sales(self.products)


    def get_sales(self):
        self.update_sales(self.products)


    @classmethod
    def update_sales(cls, products):
        cls.sales += products


my_shop = Shop('ATB', 200)
my_shop.get_sales()
print(f'Total sales {Shop.sales}')

next_shop = Shop('Silpo', 600)
next_shop.update_products(100)
print(f'Total sales {Shop.sales}')

third_shop = Shop('Novus', 100)
third_shop.get_sales()
print(f'Total sales {Shop.sales}')

