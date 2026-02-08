from product_manager import ProductManager

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
