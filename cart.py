from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []  # Lista tuple-ova (product, quantity)
    
    def add_to_cart(self, product, quantity):
        # Proveravamo da li je dovoljno proizvoda na stanju
        if quantity <= product.quantity:
            # Proveravamo da li proizvod već postoji u korpi
            for i, (existing_product, existing_quantity) in enumerate(self.cart_items):
                if existing_product.name == product.name:
                    # Ažuriramo količinu ako je ukupna količina <= dostupnoj
                    if existing_quantity + quantity <= product.quantity:
                        self.cart_items[i] = (existing_product, existing_quantity + quantity)
                    else:
                        print(f"Nema dovoljno {product.name} na stanju!")
                    return
            
            # Dodajemo novi proizvod u korpu
            self.cart_items.append((product, quantity))
            print(f"Dodato u korpu: {product.name} x{quantity}")
        else:
            print(f"Nema dovoljno {product.name} na stanju!")
    
    def calculate_total(self):
        total = 0
        for product, quantity in self.cart_items:
            total += product.price * quantity
        return total
    
    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        
        for product, quantity in self.cart_items:
            print(f"{product.name} x{quantity} - {product.price * quantity:.2f}")
