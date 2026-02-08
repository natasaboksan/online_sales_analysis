from product_manager import ProductManager
from cart import Cart
import random

def main():
    # Kreiranje instance ProductManager
    manager = ProductManager()
    
    # Dodavanje proizvoda u listu
    manager.add_product("Laptop", 1200.00, 10)
    manager.add_product("Miš", 25.50, 50)
    manager.add_product("Tastatura", 85.00, 30)
    manager.add_product("Monitor", 350.00, 15)
    manager.add_product("Slušalice", 120.00, 40)
    manager.add_product("Web kamera", 65.00, 25)
    
    # Prikaz svih proizvoda
    print("\n" + "="*50)
    manager.display_all_products()
    
    # Prikaz ukupne vrednosti inventara
    total_value = manager.calculate_total_value()
    print(f"\nUkupna vrednost inventara: {total_value:.2f}")

    # Kreiranje instance Cart
    cart = Cart()
    
    # Dodavanje 3 slučajno odabrana proizvoda u korpu
    available_products = manager.get_all_products()
    
    if len(available_products) >= 3:
        random_products = manager.get_random_products(3)
        
        # Dodajemo proizvode u korpu
        for product in random_products:
            cart.add_to_cart(product, 1)  # Dodajemo 1 komad svakog proizvoda
    
    # Prikaz sadržaja korpe
    print("\n" + "="*50)
    print("SADRŽAJ KORPE:")
    cart.display_cart()
    
    # Prikaz iznosa za naplatu
    total_amount = cart.calculate_total()
    print(f"\nUkupan iznos za naplatu: {total_amount:.2f}")

if __name__ == "__main__":
    main()
