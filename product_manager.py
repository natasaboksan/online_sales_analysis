from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
    
    # Metoda za dodavanje proizvoda u listu
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"Dodat proizvod je: {name}")
    
    # Metoda za prikaz svih proizvoda
    def display_all_products(self):
        if not self.products:
            print("Nema proizvoda u na stanju.")
            return
        
        print("\n=== SVI PROIZVODI ===")
        for product in self.products:
            print(product.display_info())
    
    # Metoda koja racuna ukupnu vrednost svih proizvoda
    def calculate_total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        return total

    # Metoda koja uklanja proizvod prema imenu
    def remove_product_by_name(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"Uklonjen proizvod: {name}")
                return
        print(f"Proizvod sa imenom '{name}' nije pronađen.")
